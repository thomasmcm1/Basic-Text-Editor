import tkinter as tk
from tkinter import filedialog, messagebox

# widget = GUI element, such as a button or label
# windows = GUI element that contains other widgets (container for widgets)

window = tk.Tk() # instantiate a window
window.geometry("600x400") # set window size
window.title("Text Editior") # set window 

text_area = tk.Text(window, wrap="word", undo=True) # create a text area widget
text_area.pack(expand=True, fill="both") # add text area to window and make it expand to fill the window

#Functions
current_file = None

def new_file():
    global current_file
    current_file = None
    text_area.delete(1.0, tk.END) # clear the text area
    window.title("Untitled - Text Editor") # set window title to "Untitled"

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]) # open file dialog to select a file
    if file_path:
        current_file = file_path
        with open(current_file, "r") as file:
            text_area.delete(1.0, tk.END) # clear the text area
            text_area.insert(tk.END, file.read()) # insert the content of the file into the text area
        window.title(f"{current_file} - Text Editor") # set window title to the name of the opened file

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END)) # write the text area content to the file

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END)) # write the text area content to the file

def exit_editor():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy() # close the window

#menu bar
menu_bar = tk.Menu(window) # create a menu bar
#file menu
file_menu = tk.Menu(menu_bar, tearoff=0) # create a file menu
file_menu.add_command(label="New", command=lambda: new_file()) # add new file option to file menu 
file_menu.add_command(label="Open", command=lambda: open_file()) # add open file option to file menu
file_menu.add_command(label="Save", command=lambda: save_file()) # add save file option to file menu
file_menu.add_command(label="Save As", command=lambda: save_as_file()) # add save as file option to file menu
file_menu.add_separator() # add a separator line in the file menu
file_menu.add_command(label="Exit", command=lambda: exit_editor()) # add exit option to file menu

menu_bar.add_cascade(label="File", menu=file_menu) # add file menu to menu bar

window.config(menu=menu_bar) # set window menu bar

icon = tk.PhotoImage(file="Text Editor.png") # load icon image
window.iconphoto(True, icon) # set window icon
window.configure(bg="#000000") # set window background colour


window.mainloop() # display window

