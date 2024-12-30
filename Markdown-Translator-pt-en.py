import tkinter as tk
from tkinter import filedialog, messagebox
from googletrans import Translator
import os

def select_input_file():
    filepath = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    if filepath:
        input_path.set(filepath)

def select_output_folder():
    folderpath = filedialog.askdirectory()
    if folderpath:
        output_path.set(folderpath)

def translate_file():
    input_file = input_path.get()
    output_folder = output_path.get()

    if not input_file:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo de entrada.")
        return

    if not output_folder:
        messagebox.showerror("Erro", "Por favor, selecione uma pasta de saída.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        translator = Translator()
        translated_content = translator.translate(content, src="pt", dest="en").text

        output_file = os.path.join(output_folder, os.path.basename(input_file).replace(".md", "_en.md"))

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(translated_content)

        messagebox.showinfo("Sucesso", f"Arquivo traduzido com sucesso para: {output_file}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Criando a interface
root = tk.Tk()
root.title("Tradutor de Markdown")

input_path = tk.StringVar()
output_path = tk.StringVar()

# Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Caminho do arquivo de entrada
label_input = tk.Label(frame, text="Arquivo de Entrada:")
label_input.grid(row=0, column=0, sticky="e")
entry_input = tk.Entry(frame, textvariable=input_path, width=50)
entry_input.grid(row=0, column=1, padx=5)
button_input = tk.Button(frame, text="Selecionar", command=select_input_file)
button_input.grid(row=0, column=2)

# Caminho da pasta de saída
label_output = tk.Label(frame, text="Pasta de Saída:")
label_output.grid(row=1, column=0, sticky="e")
entry_output = tk.Entry(frame, textvariable=output_path, width=50)
entry_output.grid(row=1, column=1, padx=5)
button_output = tk.Button(frame, text="Selecionar", command=select_output_folder)
button_output.grid(row=1, column=2)

# Botão de traduzir
button_translate = tk.Button(root, text="Traduzir", command=translate_file)
button_translate.pack(pady=10)

root.mainloop()
