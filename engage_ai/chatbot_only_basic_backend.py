import os
import sqlite3
from groq import Groq
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the actual key from environment
api_key = os.getenv("GROQ_API_KEY")

# Optional: strip to remove whitespace/newlines
api_key = api_key.strip()

# Initialize the client with the actual API key
client = Groq(api_key=api_key)

database = sqlite3.connect("May25.db")
cursor = database.cursor()

sql_assistant_prompt = (
    "You are an intelligent SQL assistant who can generate SQL queries from natural language. "
    "Ignore case differences and generalize wordings like 'high income', 'income category is high', etc. "
    " the table name is 'May25table' in 'May25.db'. "
    "Only return the SQL query without any explanation."
    "Ignore the uppercase or lowercase."
    "i am telling you about the some columns in the table: "
    "issue_date meaning the date when the loan was issued, "
    "final_date meaning the date when the loan was finalized, "
    "employment_length meaning the length of employment in years, "
    "annual_income meaning the annual income of the borrower, "
    "debt_to_income_ratio meaning the ratio of debt to income, "
    "income_category meaning the category of income which is divided into high, medium and low, "
    "loan_amount meaning the amount of the loan, "
    "term meaning the term of the loan in months, "
    "application_type meaning the type of application, "    
    "purpose meaning the purpose of the loan, "
    "loan_condition meaning the condition of the loan, "
    "interest_rate meaning the interest rate of the loan, "
    "grade meaning the grade of the loan, "
    "loan_condition, interest_rate and grade are interdependent as the condition of loan decides the grade and grade decides the interest rate, "
    "total_payment meaning the total payment borrower will return to bank or system, "
    "total_principle_to_recover meaning the total principle amount to be recovered, "
    "total_recoveries meaning the total amount of recoveries, "
    "installment meaning the installment amount to be paid by the borrower, "
    "region meaning the region of the borrower, "             
    "mortage loan is for buinding or buying a house, "   
    "following dictionary shows the column name as key and it's unique values as value: "
    "'home_ownership': ['RENT', 'MORTGAGE', 'OWN', 'OTHER', 'NONE'], "
    "'income_category': ['HIGH', 'MEDIUM', 'LOW'], "
    "'application_type': ['INDIVIDUAL', 'JOINT'], "
    "purpose': ['other','debt_consolation','credit_card','small_business','major_purchase','moving','car','home_improvement','vacation','wedding','medical','house','educational','renewable_energy'], "
    
    "'loan_condition': ['Good loan','bad loan'], "
    "'grade': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], "
    "'region': ['Delhi','Uttar Pradesh','Punjab','Assam','Rajasthan'] }"  
    "ignore the uppercase or lowercase.use LOWER function to convert the column names to lowercase and use it in the query. "    
    "only generate sql query nothing else, do not give any explanation or output of the query. "                                                                         
)

nl_response_prompt = (
    "You are an assistant that can turn raw SQL query results into clear, conversational English for non-technical users. "
)








# to get dataSet info
# get question from user
def get_question():
    global latest_question 
    while True:
        question = input("Ask your question: ")
        if question.lower() in ["exit", "end", "quit"]:
            break
        latest_question= question
        get_sql_query(question)

# convert nl to sql query
def get_sql_query(nL_query):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": sql_assistant_prompt},
                {"role": "user", "content": nL_query}
            ],
            max_tokens=150,
            temperature=0.2
        )
        sql_query = response.choices[0].message.content.strip()
        #print("\nGenerated SQL Query:", sql_query)
        cursor.execute(sql_query)
        test_rows = cursor.fetchall()
        #print("TEST Raw SQL Output:", test_rows)  # For debugging

        processing(sql_query)

    except Exception as e:
        print("Error during SQL generation:", str(e))

# fetch data from database
def processing(squery):
    try:
        cursor.execute(squery)
        sql_output = cursor.fetchall()

        if sql_output is None:
            print("No data found.")
            return
        
        else:
            result_str = "\n".join([", ".join(map(str, row)) for row in sql_output])

            #print("SQL Result:", result_str)
            get_nl_response(latest_question,result_str)

    except Exception as e:
        print("SQL execution error:", str(e))

# convert sql output to natural language
def get_nl_response(nl_question, sql_output_str):
    try:
        prompt = (
            f"You are an assistant that helps users understand SQL output in plain English.\n"
            f"Question: {nl_question}\n"
            f"SQL Result: {sql_output_str}\n"
            f"Respond in a conversational, user-friendly way explaining the result based on the question."
            f"just give the answer of te question asked nothing more , do not need to show sql query and the output must be a simple answer"
        )
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": nl_response_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.2
        )
        nl_response = response.choices[0].message.content.strip()
        nl_output(nl_response)

    except Exception as e:
        print("Error during NL response:", str(e))


# show nl output
def nl_output(nl_response):
    print("Natural Language Response:", nl_response)

# start the process
get_question()
