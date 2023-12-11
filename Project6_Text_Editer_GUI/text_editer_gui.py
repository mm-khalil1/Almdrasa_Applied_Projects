from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not file_path:
        return
    
    text_edit.delete("1.0", END)
    with open(file_path, "r") as in_file:
        text = in_file.read()
        text_edit.insert(END, text)
    file_var.set(file_path)

def save_file():
    file_path = asksaveasfilename(
        defaultextension = "txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not file_path:
        return
    
    with open(file_path, "w") as out_file:
        text = text_edit.get("1.0", END)
        out_file.write(text)
    file_var.set(file_path)

window = Tk()
window.title("Text Editor")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

file_var = StringVar()

frame_buttons = Frame(master=window)
open_button = Button(frame_buttons, text="Open File", command = open_file)
save_button = Button(frame_buttons, text="Save File", command = save_file)

frame_buttons.grid(column=0, row=0, sticky='ns', padx=1, pady=1)
open_button.grid(column=0, row=1, sticky='ew')
save_button.grid(column=0, row=2, sticky='ew')


frame_text = Frame(master=window)
frame_text.grid_rowconfigure(0, weight=1)
frame_text.grid_columnconfigure(0, weight=1)
text_edit = Text(master=frame_text)

frame_text.grid(column=1, row=0, sticky='nsew', padx=3, pady=3)
text_edit.grid(column=0, row=0, sticky='nsew')

window.mainloop()
