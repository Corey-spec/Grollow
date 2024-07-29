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
    
    prompt = "Please recommend 25 anime"
    language = language_dropdown.get()
    prompt += "The Genere is" + language + "."
    difficulty = difficulty_value.get()
    prompt += "The anime length should be " + difficulty + "."

    if checkbox1.get():
        prompt += "The reccommendations should only include newer anime. "
    if checkbox2.get():
        prompt += "The reccommendations should only include older anime."

    print(prompt)
    client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o",
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

frame = ctk.CTkFrame(master=root, width=2000, height=195, fg_color="purple", border_color="white")
frame.pack(padx=10, pady=(0,20))

logo_image = ctk.CTkImage(Image.open('grim.png'), size=(200, 200))

lo_lbl = ctk.CTkLabel(root, text="", image=logo_image)
lo_lbl.place(x=365, y=-5)

ctk.set_appearance_mode("dark")


label = ctk.CTkLabel(root, text="rollow", fg_color="purple",font=ctk.CTkFont(size=100, weight="bold"))
label.place(x=570, y=30)
title_label = ctk.CTkLabel(root, text="Anime Idea Generator", fg_color="purple",
                          font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(10,10))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame, fg_color="purple")
language_frame.pack(padx=100, pady=(20, 5),  fill="both")
language_label = ctk.CTkLabel(
     language_frame, text="Genere", font=ctk.CTkFont(weight="bold"))
language_label.pack()
language_dropdown = ctk.CTkComboBox(
    language_frame, values=["Action", "Fantasy", "Adventure", "Sports", "Supernatural", "Thriller",])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame, fg_color="purple")
difficulty_frame.pack(padx=100, pady=5, fill="both")
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Time length", font=ctk.CTkFont(weight="bold", ))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value="short")
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="short", variable=difficulty_value, value="short")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text="medium", variable=difficulty_value, value="medium")
radiobutton2.pack(side="left", padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text="long", variable=difficulty_value, value="long")
radiobutton3.pack(side="left", padx=10, pady=10)

features_frame = ctk.CTkFrame(frame, fg_color="purple")
features_frame.pack(padx=100, pady=5, fill="both")
features_label = ctk.CTkLabel(
    features_frame, text="Features", font=ctk.CTkFont(weight="bold"))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="Upcoming Anime Results")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(features_frame, text="Older Anime Result")
checkbox2.pack(side="left", padx=50, pady=10)

button = ctk.CTkButton(frame, text="Generate Possible Anime", fg_color="purple", command=generate)
button.pack(pady=10, fill="x", padx=(5, 20))


result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)


root.mainloop()


