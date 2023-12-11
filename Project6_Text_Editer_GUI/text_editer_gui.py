from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def openFile():
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not file_path:
        return
    
    text_edit.delete("0.1 ", END)
    with open(file_path, "r") as in_file:
        text = in_file.read()
        text_edit.insert(END, text)

def saveFile():
    file_path = asksaveasfilename(
        defaultextension = "txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not file_path:
        return
    
    with open(file_path, "w") as out_file:
        text = text_edit.get("1.0", END)
        out_file.write(text)

window = Tk()
window.title("Text Editor")

frame_buttons = Frame(master=window)
label_buttons = Label(master=frame_buttons, text="Options")
open_button = Button(frame_buttons, text="Open File", command = openFile)
save_button = Button(frame_buttons, text="Save File", command = saveFile)

frame_buttons.grid(column=0, row=0, sticky='ns', padx=1, pady=1)
label_buttons.grid(column=0, row=0, sticky='ew')
open_button.grid(column=0, row=1, sticky='ew')
save_button.grid(column=0, row=2, sticky='ew')


frame_text = Frame(master=window)
label_text = Label(master=frame_text, text="Text")
text_edit = Text(master=frame_text)

frame_text.grid(column=1, row=0, sticky='ns', padx=3, pady=3)
label_text.grid(column=0, row=0, sticky='ew')
text_edit.grid(column=0, row=1, sticky='nsew')

window.mainloop()
