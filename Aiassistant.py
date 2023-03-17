import openai
API_KEY="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"
openai.api_key = API_KEY
messages =[]
system_msg=input("Enter type of chatbot would you like to create : ")
messages.append({"role":"system","content":system_msg})

print("Your new assistant is ready!")
while input !="quit()":
    message = input()
    messages.append({"role":"system","content":message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    print("\n"+reply+"\n")
    