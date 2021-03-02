# Imports
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk
 


# Screen
root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Code Editor - Untitled.txt")  # Edit name when 



# Global OpenStatusName - used for finding name and status of opened file and use it for saving file and etc
global OpenFileStatusName
OpenFileStatusName = False



# Global SelectedText - used for storing any selected text and then pasting text into textbox
global SelectedText
SelectedText = False
 

 
# File Menu Option Functions
# New File Function
# Make New tab when this function is passed
def NewFile(*args):
    global OpenFileStatusName
    OpenFileStatusName = False
    # Create a New Tab when new file function occurs
    TextBox.delete("1.0", END)
    StatusBar.config(text="Code Editor - Untitled.txt")
root.bind('<Control-n>', NewFile)
 

 
# Open File Function
def OpenFile(*args):
    # Ask user for which file they want to open
    FilePath = filedialog.askopenfilename(initialdir="C:/gui/", title="Open a File", filetypes=(
    ("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"),("JavaScript Files", "*.js"), ("Python Files", "*.py")))
    # Check to see if there is a file opened, then find the name and status of the file and use it in code for other things like saving a file and accessing it later
    if FilePath:
        global OpenFileStatusName
        OpenFileStatusName = FilePath
    # Set a name for the File Path
    FileName = FilePath
    # Configure the title and Replace the directory with the file name
    FileName = FileName.replace("C:/gui/", "")
    TextBox.delete("1.0", END)
    # Open File and Insert File Content into Editor
    FilePath = open(FilePath, 'r')
    FileContent = FilePath.read()
    TextBox.insert(END, FileContent)
    FilePath.close()
root.bind('<Control-o>', OpenFile)
 
 

# Save File Function
def SaveFile(*args):
    global OpenFileStatusName
    # If File has been opened then save
    if OpenFileStatusName:
        FilePath = open(OpenFileStatusName, "w")
        FilePath.write(TextBox.get(1.0, END))
        FilePath.close()
        # Add a asterisk (*) when file isnt saved - and when file is saved then remove asterisk - NO ASTERISK FOR AUTOSAVE - DISABLE ASTERISK WHEN AUTOAVE FEATURE IS RAN
    # If the file does not exist, then save this file as a file
    else:
        SaveFileAs()
root.bind('<Control-s>', SaveFile)
 

 
# Save File As Function
def SaveFileAs(*args):
    FilePath = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/", title="Save File As",
                                            filetypes=(
                                            ("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"),
                                            ("CSS Files", "*.css"), ("JavaScript Files", "*.js"),
                                            ("Python Files", "*.py")))
    if FilePath:
        FileName = FilePath
        FileName = FileName.replace("C:/gui/", "")
        # Save the File
        FilePath = open(FilePath, "w")
        FilePath.write(TextBox.get(1.0, END))
        FilePath.close()
root.bind('<Control-Shift-S>', SaveFileAs)
 
 

# Edit Menu Option Functions
# Cut selected text Function
def CutText(e):
    global SelectedText
    # Check to see if keyboard shortcut was used
    if e:
        SelectedText = root.clipboard_get()
    else:
        # Grab selected text - then copy that text and remove it from Text Box
        if TextBox.selection_get():
            SelectedText = TextBox.selection_get()
            TextBox.delete("sel.first", "sel.last")
            # If copy option is used from edit menu and clear clipboard
            root.clipboard_clear()
            root.clipboard_append(SelectedText)
root.bind("<Control-Key-x>", CutText)
 

 
# Copy selected text Function
def CopyText(e):
    global SelectedText
    # Check to see if the keyboard shortcut was used
    if e:
        SelectedText = root.clipboard_get()
    # Check to see if there is selected text - if there is then copy it
    if TextBox.selection_get():
        SelectedText = TextBox.selection_get()
        # If copy option is used from edit menu and clear clipboard
        root.clipboard_clear()
        root.clipboard_append(SelectedText)
root.bind("<Control-Key-c>", CopyText)
 
 

# Paste selected text Function
def PasteText(e):
    global SelectedText
    # Check to see if shortcut is used
    if e:
        SelectedText = root.clipboard_get()
    else:
        # Paste the Selected Text into the Cursor Position
        if SelectedText:
            CursorPosition = TextBox.index(INSERT)
            TextBox.insert(CursorPosition, SelectedText)
root.bind("<Control-Key-v>", PasteText)
 

 
# Select All Function
def SelectAll(e):
    TextBox.tag_add("sel", 1.0, "end")
root.bind("<Control-Key-a>", SelectAll)
 
 

# Tools Menu Option
def WordWrap():
    # If there is no word wrap then add word wrap
    if TextBox.cget("wrap") == "none":
        TextBox.configure(wrap="word")
    # If there is word wrap then take out word wrap
    elif TextBox.cget("wrap") == "word":
        TextBox.configure(wrap="none")
 


# Integrate Auto Save feature in the Code Editor Menu
# Auto Save Declaration Function
def AutoSaveDeclare():
    global OpenFileStatusName
    if OpenFileStatusName:
        FileContentData = TextBox.get("1.0", END)
        with open(OpenFileStatusName, "w") as saveWrite:
            saveWrite.write(FileContentData)



# Initialize Auto Save Function
def AutoSaveInit():
    AutoSaveDeclare()
    TextBox.after(1, AutoSaveInit)



# Tab Control --- place for adding new tab
TabControl = ttk.Notebook(root)
TabControl.pack()



# Add stuff like word count, character count, what the location of the mouse is like for eg: Ln 22, Col 2
# Status Bar
StatusBar = Label(root, text="Code Editor", bg="dodgerblue", anchor=W)
StatusBar.pack(fill=X, side=BOTTOM, ipady=2)



# Create Main Frame - For Placing Scrollbars and TextBox
MainFrame = Frame(root)
MainFrame.pack()



# Vertical Scrollbar
VerticalScrollbar = Scrollbar(MainFrame)
VerticalScrollbar.pack(side=RIGHT, fill=Y)



# Horizontal Scrollbar
HorizontalScrollbar = Scrollbar(MainFrame, orient="horizontal")
HorizontalScrollbar.pack(side=BOTTOM, fill=X)



# Text Box               Change width to fit rest
TextBox = Text(MainFrame, width=500, font=("Monaco", 16), selectbackground="skyblue", undo=True, wrap="none",
              yscrollcommand=VerticalScrollbar.set, xscrollcommand=HorizontalScrollbar.set)
TextBox.pack(fill=BOTH)



# Configuring the Vertical Scrollbar
VerticalScrollbar.config(command=TextBox.yview)



# Configure the Horizontal Scroll Bar
HorizontalScrollbar.config(command=TextBox.xview)



# Menu Bar
MenuBar = Menu(root)
root.config(menu=MenuBar)
MenuBar.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1,
              font=('Monaco', 11))



# File Option for Menu Bar
FileOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="File", menu=FileOption, underline=0)
FileOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1,
                 font=('Monaco', 11))
FileOption.add_command(label="New File", command=NewFile, accelerator="Ctrl+N")
FileOption.add_command(label="Open File", command=OpenFile, accelerator="Ctrl+O")
FileOption.add_command(label="Open Folder", command=None, accelerator="Ctrl+Shift+O")
# Make this a drop down and list the names of the files that were recently opened:
#FileOption.add_command(label="Open Recent", command=None)
FileOption.add_separator()
FileOption.add_command(label="Save File", command=SaveFile, accelerator="Ctrl+S")
FileOption.add_command(label="Save As", command=SaveFileAs, accelerator="Ctrl+Shift+S")
FileOption.add_separator()
FileOption.add_command(label="Auto Save", command=AutoSaveInit)

# Preferences Option for File Menu             
PreferencesMenu = Menu(FileOption, tearoff=False)
PreferencesMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1,
               font=('Monaco', 11))
PreferencesMenu.add_command(label="Keyboard Shortcuts", command=None)
PreferencesMenu.add_command(label="Color Theme", command=None)
# Cascade the Preferences menu to the File Menu
FileOption.add_cascade(label="Preferences", menu=PreferencesMenu)
# The Remaining options for the File Menu
FileOption.add_separator()
FileOption.add_command(label="Close Editor", command=None)
FileOption.add_command(label="Exit", command=root.quit)



# Edit Option for Menu Bar
EditOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Edit", menu=EditOption, underline=0)
EditOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1,
                 font=('Monaco', 11))
EditOption.add_command(label="Undo", command=TextBox.edit_undo, accelerator="Ctrl+Z")
EditOption.add_command(label="Redo", command=TextBox.edit_redo, accelerator="Ctrl+Y")
EditOption.add_separator()
EditOption.add_command(label="Cut", command=lambda: CutText(False), accelerator="Ctrl+X")
EditOption.add_command(label="Copy", command=lambda: CopyText(False), accelerator="Ctrl+C")
EditOption.add_command(label="Paste", command=lambda: PasteText(False), accelerator="Ctrl+V")
EditOption.add_separator()
EditOption.add_command(label="Find", command=None, accelerator="Ctrl+F")
EditOption.add_command(label="Replace", command=None, accelerator="Ctrl+H")
EditOption.add_separator()
EditOption.add_command(label="Select All", command=lambda: SelectAll(True), accelerator="Ctrl+a")



# View Option for Menu Bar
ViewOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="View", menu=ViewOption, underline=0)
ViewOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1,
                 font=('Monaco', 11))
ViewOption.add_command(label="Appearance", command=None)  # Add dropdown
ViewOption.add_command(label="Maximize", command=None)
ViewOption.add_command(label="Minimize", command=None)



# Tools Option for Menu Bar
ToolsOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Tools", menu=ToolsOption, underline=0)
ToolsOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1,
                  font=('Monaco', 11))
ToolsOption.add_command(label="Toggle Word Wrap", command=WordWrap)



# Settings Option for Menu Bar
SettingsMenu = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Settings", menu=SettingsMenu, underline=0)
SettingsMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black",
                   activeborderwidth=1, font=('Monaco', 11))

# Help Option for Settings Menu             
HelpMenu = Menu(SettingsMenu, tearoff=False)
HelpMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1,
               font=('Monaco', 11))
HelpMenu.add_command(label="Documentation", command=None)
HelpMenu.add_command(label="Release Notes", command=None)
HelpMenu.add_command(label="View License", command=None)
HelpMenu.add_command(label="Get Started", command=None)
HelpMenu.add_command(label="About", command=None)
# Cascade the help menu to the Settings Menu
SettingsMenu.add_cascade(label="Help", menu=HelpMenu)
# The remaining settings options
SettingsMenu.add_command(label="Add more settings", command=None)



# Right Click Menu
RightClickMenu = Menu(TextBox, tearoff=False)
RightClickMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black",
                     activeborderwidth=1, font=('Monaco', 11))
RightClickMenu.add_command(label="Undo", command=TextBox.edit_undo, accelerator="Ctrl+z")
RightClickMenu.add_command(label="Redo", command=TextBox.edit_redo, accelerator="Ctrl+y")
RightClickMenu.add_separator()
RightClickMenu.add_command(label="Cut", command=lambda: CutText(False), accelerator="Ctrl+x")
RightClickMenu.add_command(label="Copy", command=lambda: CopyText(False), accelerator="Ctrl+c")
RightClickMenu.add_command(label="Paste", command=lambda: PasteText(False), accelerator="Ctrl+v")
RightClickMenu.add_separator()
RightClickMenu.add_command(label="Select All", command=lambda: SelectAll(True), accelerator="Ctrl+a")
 
# Right Click Menu Popup Function
def RightClickMenuPopUp(e):
    RightClickMenu.tk_popup(e.x_root, e.y_root)
# Binding for Right Click and Menu Popup
root.bind("<Button-3>", RightClickMenuPopUp)



# Mainloop
root.mainloop()
