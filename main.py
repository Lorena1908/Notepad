from tkinter import *
from tkinter import filedialog
import pickle

width = 600

root = Tk()
root.geometry(str(width) + 'x' + str(width))
root.title('Notepad')
root.iconbitmap('notepad_icon.ico')

text = Text(root)
text.pack(ipady=width, ipadx=width)

def save_file():
    # This is a file dialog box for saving files
    file_name = filedialog.asksaveasfilename(initialdir='/Users/lorel/Desktop', title='Save File', filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
    if file_name:
        if file_name.endswith('.txt'):
            pass
        else:
            file_name = f'{file_name}.txt'
        
        content = text.get("1.0","end-1c")
        out_file = open(file_name, 'w')
        out_file.write(content)
        out_file.close()

def open_file():
    text.delete('1.0', END)
    file_name = filedialog.askopenfilename(initialdir='/Users/lorel/Dektop', title='Open File', filetypes=(('Text', '*.txt'), ('All Files', '*.*')))

    if file_name:
        file = open(file_name)
        content = file.readlines()
        
        for line in content:
            text.insert(END, line)

        file.close()

menu = Menu(root) # Create the menu
root.config(menu=menu) # Add is as the root menu
file_menu = Menu(root, tearoff=False) # Create file menu
# Add 'File' to the main menu. The top bar will only show up because of this line
menu.add_cascade(label='File', menu=file_menu) 
file_menu.add_command(label='Save File', command=save_file) # Add save file function
file_menu.add_command(label='Open File', command=open_file) # Add open file function

root.mainloop()