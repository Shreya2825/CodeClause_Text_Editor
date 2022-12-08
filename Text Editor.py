from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title('TEXT EDITOR- python')
root.geometry("800x700")


global open_status_name
open_status_name = False

global selected
selected= False

#Create New File Function
def new_file():
    my_text.delete('1.0', END)
    root.title('New File !')
    status_bar.config(text="New File     ")
    global open_status_name
    open_status_name = False


#Open Files
def open_file():
    my_text.delete('1.0', END)
    text_file = filedialog.askopenfilename(parent=root, initialdir="./examples", title='Open File', filetypes=(('Text Files', '*.txt'),('HTML Files', '*.html'),('Python Files', '*.py'), ('All Files','*.')))
    if text_file:
            global open_status_name
            open_status_name = text_file
  
    name = text_file
    status_bar.config(text=f'{name}  ')
    name.replace("./examples","")
    root.title(f'{name}- text editor')

   #Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

 # save_as_file
def save_as_file():
    text_file =filedialog.asksaveasfilename(defaultextension=".*", initialdir="./example", title='Save File', filetypes=(('Text Files', '*.txt'),('HTML Files', '*.html'),('Python Files', '*.py'), ('All Files','*.')))
    if text_file:
        name= text_file
        status_bar.config(text=f'Saved: {name}  ')
        name= name.replace("./examples","")
        root.title(f'{name}- text editor')

        text_file =open(text_file, 'w')
        text_file.write(my_text.get(1.0,END))

        text_file.close()  

# Save File
def save_file():
   global open_status_name
   if open_status_name:
    text_file = open(open_status_name,'w')
    text_file.write(my_text.get(1.0,END))
    text_file.close()
    status_bar.config(text=f'Saved: {open_status_name}  ')
   else:
    save_as_file()
    #popup code

#cut the text     
def cut_text(e):
   global selected
   if my_text.selection_get():
    selected =my_text.selection_get()
    my_text.delete("sel.first","sel.last")

#copy the text
def copy_text(e):
    global selected

    if my_text.selection_get():
        selected =my_text.selection_get()

#paste the text
def paste_text(e):
    if selected:
     position = my_text.index(INSERT)
     my_text.insert(position, selected)

def bold_text():
    bold_font= font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    my_text.tag_configure("bold",font=bold_font)

    current_tags= my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove("bold","sel.first","sel.last")
    else:
        my_text.tag_add("bold","sel.first","sel.last")

def italics_text():
    italic_font= font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    my_text.tag_configure("italic",font=italic_font)

    current_tags= my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove("italic","sel.first","sel.last")
    else:
        my_text.tag_add("italic","sel.first","sel.last")

def text_color():
    #pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
     status_bar.config(text=my_color)
     color_font= font.Font(my_text, my_text.cget("font"))

    my_text.tag_configure("colored",font=color_font, foreground=my_color)

    current_tags= my_text.tag_names("sel.first")

    if "colored" in current_tags:
        my_text.tag_remove("colored","sel.first","sel.last")
    else:
        my_text.tag_add("colored","sel.first","sel.last")

def bg_color():
  my_color = colorchooser.askcolor()[1]
  if my_color:
    my_text.config(bg=my_color)

def All_text_color():
     my_color = colorchooser.askcolor()[1]
     if my_color:
      my_text.config(fg=my_color)
#create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#create our scrollbar For the Text Box
text_scroll =Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


#horizontal scrollbar
hor_scroll = Scrollbar(my_frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

#create Text Box
my_text =Text(my_frame, width=97, height=25, font=("helvetica",16), selectbackground="red", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand= hor_scroll.set)
my_text.pack()

#configure our Scrollbar
text_scroll.config(command=my_text.yview)
text_scroll.config(command=my_text.xview)

#create Menu
my_menu =Menu(root)
root.config(menu=my_menu)

file_menu =Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command= open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As',command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit')

edit_menu =Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy',command=lambda: copy_text(False),accelerator='(ctrl+C)')
edit_menu.add_command(label='Cut',command=lambda: cut_text(False),accelerator='ctrl+X')
edit_menu.add_command(label='Paste',command=lambda: paste_text(False),accelerator='(ctrl+V)')
edit_menu.add_separator()
edit_menu.add_command(label='Undo',command= my_text.edit_undo,accelerator='(ctrl+z)')
edit_menu.add_command(label='Redo',command= my_text.edit_redo,accelerator='(ctrl+y)')

design_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Design',menu=design_menu)
design_menu.add_command(label='Bold',command=bold_text)
design_menu.add_command(label='Italic',command=italics_text)
design_menu.add_command(label='Text Color',command=text_color)
design_menu.add_command(label='All text select',command=All_text_color)
design_menu.add_command(label='Change Background',command=bg_color)




#Add Status Bar TO Bottom Of App
status_bar =Label(root, text='GO     ',anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


root.mainloop()