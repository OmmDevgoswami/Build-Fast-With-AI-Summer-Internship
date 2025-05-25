import pandas as pd
import random
import json

data = pd.read_csv("Built Fast with AI\\Data Cleaning\\cleaned_output.csv")

messages = []

joined_templates = [
    "Hey {name}, thanks for joining our recent session! As a {job}, you might enjoy our growth tools tailored for early-stage ventures. Want to be part of our pilot?",
    "Hi {name}, it was awesome having you at the event! As a {job}, we think you'll find our upcoming visualization tools game-changing. Interested in a sneak peek?",
    "Hello {name}, great to see you in our session! Your experience in {job} makes you a perfect fit for our beta testing group. Want early access?",
    "Hey {name}, thanks for attending! As someone working in {job}, you might love our AI tools for more engagement. Want to try them out before launch?"
]

not_joined_templates = [
    "Hi {name}, sorry we missed you at the last session! We're hosting a new one tailored for {job} like you. Want us to send you the invite?",
    "Hello {name}, we noticed you couldn't make it to the event. No worries — we're planning a {job}-focused session soon. Should we reserve your spot?",
    "Hey {name}, we missed you at the event! But good news — a new product walkthrough is coming up that's perfect for {job} like you.",
    "Hi {name}, couldn't catch you at the last session. But we're preparing a custom workshop for {job}. Want to be on the early invite list?"
]

for _, row in data.iterrows():
    name = row['name']
    job = row['Job Title']
    joined = row['has_joined_event']

    if joined:
        template = random.choice(joined_templates)
        message = "🎉 Joined the event:\n" + template.format(name=name, job=job)
    else:
        template = random.choice(not_joined_templates)
        message = "🙈 Didn't join:\n" + template.format(name=name, job=job)

    messages.append({
        "email": row['email'],
        "message": message
})

# print(messages)

message_details = pd.DataFrame(messages)
message_details.to_csv("Built Fast with AI\\Message Creation\\message_details.csv", index=False)

for row in messages:
    row['message'] = row['message'].replace("🎉 Joined the event:\n", "").replace("🙈 Didn't join:\n", "")

with open("Built Fast with AI\\Message Creation\\message_details.txt", 'w') as file:
    file.write("email,message\n")
    for mesg in messages:
        file.write(f"{mesg['email']},{mesg['message']}\n")

try:
    with open("Built Fast with AI\\Message Creation\\message_details.json", "r") as file:
        old_data = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    old_data = []

all_data = old_data + messages

with open("Built Fast with AI\\Message Creation\\message_details.json", "w") as file:
    json.dump(all_data, file, indent=4)

print("Message Creation Done")