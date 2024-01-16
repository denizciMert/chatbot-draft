import openai

openai.api_key = ""

dialog = []
system_msg = input("Asistanının karakterini kısaca tanımla."+"\n")
dialog.append({"role": "system", "content": system_msg})

print("Yeni asistanın hazır!")
while input != "quit()":
    message = input()
    dialog.append({"role": "user", "content": message})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = dialog)
    reply = response.choices[0].message.content
    dialog.append({"role": "assistant","content": reply})
    print("\n"+ reply+ "\n")