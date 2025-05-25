import pandas as pd

data = pd.read_csv("Built Fast with AI\\Data Cleaning\\Data - Sheet1.csv")
# print(data.columns)
# print(data.shape)
# print(data.size)
# print()
# print(data.head())
# print()
# print(data.tail())

data.drop_duplicates(subset="email", inplace=True)

cleaned_rows = []

for index, row in data.iterrows():
    linkedin = str(row["What is your LinkedIn profile?"]).strip()
    job = str(row["Job Title"]).strip()

    if "linkedin.com" not in linkedin or not linkedin.startswith(("http", "www")):
        flag = "LinkedIn Missing/Incomplete"
    elif job == "" or job.lower() == "nan":
        flag = "Job Title Missing"
    else:
        flag = ""
        
    cleaned_values = {
        "name": row["name"],
        "first_name": row["first_name"],
        "last_name": row["last_name"],
        "email": row["email"],
        "created_at": row["created_at"],
        "approval_status": row["approval_status"],
        "has_joined_event": True if row["has_joined_event"] == "Yes" else False,
        "amount": row["amount"],
        "amount_tax": row["amount_tax"],
        "amount_discount": row["amount_discount"],
        "currency": row["currency"],
        "ticket_name": row["ticket_name"],
        "Job Title": row["Job Title"],
        "What is your LinkedIn profile?": row["What is your LinkedIn profile?"],
        "Flag": flag
    }

    cleaned_rows.append(cleaned_values)
    
cleaned_output = pd.DataFrame(cleaned_rows)
cleaned_output.to_csv("Built Fast with AI\\Data Cleaning\\cleaned_output.csv", index=False)
# print(cleaned_output.head())
# print()
# print(cleaned_output.tail())
print("Clean Data Creation Finished")