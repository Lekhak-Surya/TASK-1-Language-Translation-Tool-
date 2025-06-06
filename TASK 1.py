import tkinter as tk
from tkinter import ttk
from googletrans import Translator  # pip install googletrans==4.0.0-rc1

# Mapping full language names to language codes
language_map = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-cn"
}

def translate_text():
    src = language_map.get(source_lang.get())
    dest = language_map.get(target_lang.get())
    text = input_text.get("1.0", tk.END)
    translator = Translator()
    try:
        result = translator.translate(text, src=src, dest=dest)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.text)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")

root = tk.Tk()
root.title("Language Translation Tool")

tk.Label(root, text="Enter Text:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

frame = tk.Frame(root)
frame.pack()

# Language options (full names)
language_names = list(language_map.keys())

tk.Label(frame, text="Source Lang:").grid(row=0, column=0)
source_lang = ttk.Combobox(frame, values=language_names)
source_lang.set("English")
source_lang.grid(row=0, column=1)

tk.Label(frame, text="Target Lang:").grid(row=0, column=2)
target_lang = ttk.Combobox(frame, values=language_names)
target_lang.set("Hindi")
target_lang.grid(row=0, column=3)

tk.Button(root, text="Translate", command=translate_text).pack()
tk.Label(root, text="Translated Text:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()
