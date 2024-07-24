import os
import customtkinter as ctk
from openai import OpenAI
from dotenv import load_dotenv
import PIL
from PIL import Image

load_dotenv()

import customtkinter as ctk 


# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 

def generate():
    prompt = "Please generate 10 ideas for coding projects"
    language = language_dropdown.get()
    prompt += "The programing language is " + language + "."
    difficulty = difficulty_value.get()
    prompt += "The difficulty is " + difficulty + "."

    if checkbox1.get():
        prompt += "The projects should include a database. "
    if checkbox2.get():
        prompt += "The projects should include an API."

    print(prompt)
    client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": prompt}
        ]
    )      
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)



root = ctk.CTk()
root.geometry("750x550")
root.title("ChatGPT Projects Idea Generator")

image = PIL.Image.open('bg.jpg')
background_image = ctk.CTkImage(image, size=(1500, 1100))

bg_lbl = ctk.CTkLabel(root, text="", image=background_image)
bg_lbl.place(x=0, y=0)

frame = ctk.CTkFrame(master=root, width=2000, height=210)
frame.pack(padx=10, pady=(0,20))

logo_image = ctk.CTkImage(Image.open('grim.png'), size=(200, 200))

lo_lbl = ctk.CTkLabel(root, text="", image=logo_image)
lo_lbl.place(x=365, y=10)

ctk.set_appearance_mode("dark")


label = ctk.CTkLabel(root, text="rollow", fg_color="transparent",font=ctk.CTkFont(size=100, weight="bold"))
label.place(x=600, y=50)
title_label = ctk.CTkLabel(root, text="Anime Idea Generator",
                          font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(10,10))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100, pady=(20, 5), fill="both")
language_label = ctk.CTkLabel(
     language_frame, text="Genere", font=ctk.CTkFont(weight="bold"))
language_label.pack()
language_dropdown = ctk.CTkComboBox(
    language_frame, values=["Action", "Fantasy", "Adventure", "Sports", "Supernatural", "Thriller",])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Easy", variable=difficulty_value, value="Easy")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text="Medium", variable=difficulty_value, value="Medium")
radiobutton2.pack(side="left", padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text="Hard", variable=difficulty_value, value="Hard")
radiobutton3.pack(side="left", padx=10, pady=10)

features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100, pady=5, fill="both")
features_label = ctk.CTkLabel(
    features_frame, text="Features", font=ctk.CTkFont(weight="bold"))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(features_frame, text="API")
checkbox2.pack(side="left", padx=50, pady=10)

button = ctk.CTkButton(frame, text="Generate Ideas", command=generate)
button.pack(pady=10, fill="x", padx=(5, 20))

result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)

textbox = ctk.CTkTextbox(root)

textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
textbox.pack(pady=10, fill="x", padx=100)

root.mainloop()


