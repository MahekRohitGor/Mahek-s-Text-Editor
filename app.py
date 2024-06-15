from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os  # For file path manipulation

# Flag to track if the file is saved
is_saved = False

# Undo/redo stack (using a list)
undo_stack = []
redo_stack = []

# Clipboard simulation
clipboard = ""

def new_file():
    global text_area, is_saved, undo_stack, redo_stack  # Declare variables as global
    text_area.delete(1.0, END)  # Clear the text area
    root.title("Untitled - Simple Text Editor")
    is_saved = False
    undo_stack = []
    redo_stack = []  # Clear undo/redo stacks for new file

def open_file():
    global text_area, is_saved, undo_stack, redo_stack
    filename = filedialog.askopenfilename(title="Open a File")

    if filename:
        with open(filename, "r") as f:
            text_area.delete(1.0, END)
            text_area.insert(END, f.read())
            root.title(os.path.basename(filename) + " - Simple Text Editor")
            is_saved = True
            undo_stack = []
            redo_stack = []  # Clear undo/redo stacks for opened file

def save_file():
    global text_area, is_saved, undo_stack, redo_stack
    filename = filedialog.asksaveasfilename(title="Save File")

    if filename:
        with open(filename, "w") as f:
            f.write(text_area.get(1.0, END))
            root.title(os.path.basename(filename) + " - Simple Text Editor")
            is_saved = True

def close_window():
    global text_area, is_saved, undo_stack, redo_stack
    if text_area.get(1.0, END) != "" and not is_saved:
        answer = messagebox.askquestion(title="Save Changes", message="Do you want to save the changes?")
        if answer.lower() == "yes":
            save_file()
    root.destroy()

def print_file():
    content = text_area.get(1.0, END).strip()
    if content:
        messagebox.showinfo("Print Preview", content)
    else:
        messagebox.showinfo("Print Preview", "Nothing to print")

def undo():
    global text_area, undo_stack, redo_stack
    if undo_stack:
        redo_stack.append(text_area.get(1.0, END))  # Push current state to redo stack before undo
        text_area.delete(1.0, END)
        text_area.insert(END, undo_stack.pop())  # Restore previous state from undo stack

def redo():
    global text_area, undo_stack, redo_stack
    if redo_stack:
        undo_stack.append(text_area.get(1.0, END))  # Push current state to undo stack before redo
        text_area.delete(1.0, END)
        text_area.insert(END, redo_stack.pop())  # Restore state from redo stack

def cut():
    global text_area, clipboard
    try:
        selected_text = text_area.selection_get()
        text_area.delete(SEL_FIRST, SEL_LAST)  # Remove selected text
        clipboard = selected_text
        update_undo_stack()
    except TclError:
        pass

def copy():
    global text_area, clipboard
    try:
        selected_text = text_area.selection_get()
        clipboard = selected_text
    except TclError:
        pass

def paste():
    global text_area, clipboard
    text_area.insert(INSERT, clipboard)  # Insert clipboard content at the current cursor position
    update_undo_stack()

def update_undo_stack(event=None):
    global undo_stack
    undo_stack.append(text_area.get(1.0, END))
    redo_stack.clear()

def on_key_press(event):
    global is_saved
    is_saved = False

root = Tk()
root.title("Untitled - Simple Text Editor")
root.geometry("600x400")

text_area = Text(root, undo=True, wrap=WORD)
text_area.pack(expand=True, fill=BOTH)
text_area.bind('<KeyPress>', on_key_press)
text_area.bind('<<Modified>>', update_undo_stack)

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Print", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close_window)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# Keyboard shortcuts
root.bind('<Control-n>', lambda event: new_file())
root.bind('<Control-o>', lambda event: open_file())
root.bind('<Control-s>', lambda event: save_file())
root.bind('<Control-p>', lambda event: print_file())
root.bind('<Control-z>', lambda event: undo())
root.bind('<Control-y>', lambda event: redo())
root.bind('<Control-x>', lambda event: cut())
root.bind('<Control-c>', lambda event: copy())
root.bind('<Control-v>', lambda event: paste())

root.protocol("WM_DELETE_WINDOW", close_window)
root.mainloop()