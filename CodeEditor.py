# Imports
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk
import speech_recognition as sr
 


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
# Empty File Function
# Make New tab when this function is passed
def EmptyFile(*args):
    global OpenFileStatusName
    OpenFileStatusName = False
    # Create a New Tab when new file function occurs
    TextBox.delete("1.0", END)
    StatusBar.config(text="Code Editor - Untitled.txt")
root.bind('<Control-n>', EmptyFile)
 

 
# Open File Function
def OpenFile(*args):
    # Ask user for which file they want to open
    FilePath = filedialog.askopenfilename(initialdir="C:/gui/", title="Open a File", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"),("JavaScript Files", "*.js"), ("Python Files", "*.py")))
    
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

    # Add a asterisk (*) when file isnt saved - and when file is saved then remove asterisk - NO ASTERISK FOR AUTOSAVE - DISABLE ASTERISK WHEN AUTOSAVE FEATURE IS RAN
    # If the file does not exist, then save this file as a file
    else:
        SaveFileAs()
root.bind('<Control-s>', SaveFile)
 

 
# Save File As Function
def SaveFileAs(*args):
    FilePath = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/", title="Save File As", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("JavaScript Files", "*.js"), ("Python Files", "*.py")))
    if FilePath:
        FileName = FilePath
        FileName = FileName.replace("C:/gui/", "")
        # Save the File
        FilePath = open(FilePath, "w")
        FilePath.write(TextBox.get(1.0, END))
        FilePath.close()
root.bind('<Control-Shift-S>', SaveFileAs)
 

 
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



# Preferences Drop Down Menu in File Menu



# Keyboard Shortcuts Function
def ColorTheme():
    # For Future Versions - place functions in seperate file called CodeEditorThemes.py
    # Add commands and place functions in this function
    ColorThemeWindow = Toplevel(root)
    ColorThemeWindow.geometry("300x300")
    ColorThemeWindow.title("Color Theme")
    
    # Default Theme
    def DefaultTheme():
        TextBox.config(bg="White", fg="Black")
        MenuBar.config(bg="White", fg="Black")
        StatusBar.config(bg="dodgerblue")

    DefaultThemeBtn = Button(ColorThemeWindow, text="Default Theme", command=DefaultTheme)
    DefaultThemeBtn.pack()

    # Light Theme
    def LightTheme():
        TextBox.config(bg="Whitesmoke", fg="Black")
        MenuBar.config(bg="White", fg="Black")
        StatusBar.config(bg="White")

    LightThemeBtn = Button(ColorThemeWindow, text="Light Theme", command=LightTheme)
    LightThemeBtn.pack()

    # Dark Theme
    def DarkTheme():
        TextBox.config(bg="Black", fg="White")
        MenuBar.config(bg="#332a2a", fg="White")
        StatusBar.config(bg="dodgerblue")

    DarkThemeBtn = Button(ColorThemeWindow, text="Dark Theme", command=DarkTheme)
    DarkThemeBtn.pack()

    # Blue Theme
    def BlueTheme():
        TextBox.config(bg="#187980", fg="White")
        MenuBar.config(bg="White", fg="Black")
        StatusBar.config(bg="dodgerblue")

    BlueThemeBtn = Button(ColorThemeWindow, text="Blue Theme", command=BlueTheme)
    BlueThemeBtn.pack()
    # Main Loop for Color Theme
    ColorThemeWindow.mainloop()



# Close Editor Function
def CloseEditor(*args):
    global OpenFileStatusName
    OpenFileStatusName = False
    TextBox.delete("1.0", END)
root.bind("<Control-Key-w>", CloseEditor)



# Exit Program Function
def ExitProgram(*args):
    root.destroy()
root.bind("<Control-Key-q>", ExitProgram)



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
 


# Run Python Menu Options
def RunPythonFile(*args):
    Open_File_To_Run = filedialog.askopenfile(mode="r", title="Select Python File to Run")
    exec(Open_File_To_Run.read())



def ToggleLineComment(*args):
    TextBox.insert("1.0", "# ")
# Add binding root.bind("<Control-Key-/>", ToggleLineComment)



def ToggleBlockComment(*args):
    TextBox.insert("1.0", "''' \n\n'''")
root.bind("<Control-Shift-A>", ToggleBlockComment)



# Tools Menu Options



# Word Count Function
def DeclareWordCount():
    # Get data in textbox - turns into a string
    TextContent = TextBox.get("1.0", END)
    # String to number 
    CharactersInTextBox = len(TextContent)    
    WordsInTextBox = len(TextContent.split()) 
    # Config in Status Bar
    StatusBar.config(text="Code Knight - Characters: " + str(CharactersInTextBox-1) + " Words: " + str(WordsInTextBox))

def InitWordCount():
    DeclareWordCount()
    StatusBar.after(1, InitWordCount)



# Toggle Word Wrap Function
def ToggleWordWrap(*args):

    # If there is no word wrap then add word wrap
    if TextBox.cget("wrap") == "none":
        TextBox.configure(wrap="word")
        # Turn on Check Mark if the Function is called 
        WordWrap_CheckMark.set(True)

    # If there is word wrap then take out word wrap
    elif TextBox.cget("wrap") == "word":
        TextBox.configure(wrap="none")
        # Turn off Check Mark if the Function is disabled
        WordWrap_CheckMark.set(False)
root.bind("<Alt-Key-z>", ToggleWordWrap)



# Speech to Text Function
def Speech_to_Text():
    mic_list = sr.Microphone.list_microphone_names()
    print('here........')
    print(mic_list)
    mic_name='Intel 82801AA-ICH: MIC ADC (hw:0,1)'
    for i, microphone_name in enumerate(mic_list): 
        if microphone_name == mic_name: 
            device_id = i 
    print(device_id)

    # Values that are recording for processing
    sample_rate = 48000

    # Bytes of Data that we want to read at once 
    chunk_size = 5000
    r = sr.Recognizer() 
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source:
        r.adjust_for_ambient_noise(source) 
        print("Recording...")
        #listens for the user's input 
        audio = r.listen(source)
        try: 
            text = r.recognize_google(audio)
            # Insert content into text box
            TextBox.insert(1.0, text)

        #error occurs when google could not understand what was said 

        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio - TRY AGAIN") 
            Speech_to_Text()



# Template Manager Function
def TemplateManagerFunction(*args):
    TemplateManager = Toplevel(root)
    TemplateManager.geometry("500x500")
    TemplateManager.title("Template Manager")

    # HTML Templates
    def HTML_Basic_MarkupFunction(*args):
        HTML_Basic_Markup = "<!DOCTYPE html> \n<html lang=\"en\"> \n<head> \n\t<meta charset=\"UTF-8\"> \n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"> \n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> \n\t<title>Untitled</title> \n</head> \n<body> \n\n</body> \n</html>"
        global OpenFileStatusName
        OpenFileStatusName = False
        # Create a New Tab when new file function occurs
        TextBox.delete("1.0", END)
        TextBox.insert("1.0", HTML_Basic_Markup)
    
    def HTML_LoginForm_Function(*args):
        HTML_LoginForm = "<!DOCTYPE html> \n<html lang=\"en\"> \n<head> \n\t<meta charset=\"UTF-8\"> \n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"> \n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> \n\t<title>Untitled</title> \n</head> \n<body> \n\t<form> \n\t\t<div> \n\t\t\t<label>Username</label> \n\t\t\t<input> \n\t\t</div> \n\n\t\t<div> \n\n\t\t\t<label>Password</label> \n\t\t\t<input> \n\t\t</div> \n\n\t\t<button>Submit</button> \n\t</form> \n</body> \n</html>"
        global OpenFileStatusName
        OpenFileStatusName = False
        # Create a New Tab when new file function occurs
        TextBox.delete("1.0", END)
        TextBox.insert("1.0", HTML_LoginForm)

    # Buttons for HTML Templates
    HTML_HeaderText = Label(TemplateManager, text="HTML", fg="Black", font=("Helvetica", 16))
    HTML_HeaderText.pack()

    HTML_StartFile = Button(TemplateManager, text="Basic Markup", bg="Royalblue", fg="White", command=HTML_Basic_MarkupFunction)
    HTML_StartFile.pack()

    HTML_LoginFormBtn = Button(TemplateManager, text="Login Form", bg="Royalblue", fg="White", command=HTML_LoginForm_Function)
    HTML_LoginFormBtn.pack(pady=5)

    #Python Templates
    def Tkinter_SetupFunction():
        Tkinter_Setup = "from tkinter import * \n\nroot = Tk() \nroot.geometry(\"300x300\") \nroot.title(\"Untitled\") \n\nroot.mainloop()"
        global OpenFileStatusName
        OpenFileStatusName = False
        # Create a New Tab when new file function occurs
        TextBox.delete("1.0", END)
        TextBox.insert("1.0", Tkinter_Setup)
    
    # Buttons for Python Templates
    Python_HeaderText = Label(TemplateManager, text="Python", fg="Black", font=("Helvetica", 16))
    Python_HeaderText.pack(pady=10)
    
    Tkinter_SetupBtn = Button(TemplateManager, text="Tkinter Starting Code", bg="Royalblue", fg="White", command=Tkinter_SetupFunction)
    Tkinter_SetupBtn.pack()

    TemplateManager.mainloop()



# Help Menu Functions



# About Screen Function
def AboutScreen():
    # About Screen Window
    AboutScreenPopUp = Toplevel(root)
    AboutScreenPopUp.title("About")
    AboutScreenPopUp.geometry("300x300")

    # Header
    AboutHeader = Label(AboutScreenPopUp, text="Code Knight", font=("Helvetica", 16))
    AboutHeader.pack()

    # Attribution
    AboutHeaderAttribtion = Label(AboutScreenPopUp, text="By: Sohan Kyatham", font=("Helvetica", 12))
    AboutHeaderAttribtion.pack(pady=5)

    # Version
    AboutVersion = Label(AboutScreenPopUp, text="Version: 1.0.0", font=("Helvetica", 12))
    AboutVersion.pack(pady=60)

    # Mainloop
    AboutScreenPopUp.mainloop()




# For future versions - add tabs so users can work with multiple files at once
# Tab Control --- place for adding new tab
# TabControl = ttk.Notebook(root)
# TabControl.pack()



# Add stuff like word count, character count, what the location of the mouse is like for eg: Ln 22, Col 2
# Status Bar
StatusBar = Label(root, text="Code Knight", anchor=W)
StatusBar.config(bg="dodgerblue")
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



# Text Box               Change width to fit other stuff in future versions
TextBox = Text(MainFrame, width=500, font=("Courier New", 16), selectbackground="skyblue", undo=True, wrap="none", yscrollcommand=VerticalScrollbar.set, xscrollcommand=HorizontalScrollbar.set)
TextBox.pack(fill=BOTH)



# Configuring the Vertical Scrollbar
VerticalScrollbar.config(command=TextBox.yview)



# Configure the Horizontal Scroll Bar
HorizontalScrollbar.config(command=TextBox.xview)



# Menu Bar
MenuBar = Menu(root)
root.config(menu=MenuBar)
MenuBar.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))



# Check Marks for Options on File Menu
AutoSave_CheckMark = BooleanVar()
AutoSave_CheckMark.set(False)

# File Menu for Menu Bar
FileOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="File", menu=FileOption, underline=0)
FileOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))

# New Drop Down Option for File Menu             
NewOption = Menu(FileOption, tearoff=False)
NewOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
NewOption.add_command(label="Empty File", command=EmptyFile, accelerator="Ctrl+N")
NewOption.add_command(label="From Template", command=TemplateManagerFunction)
# Cascade the New menu to the File Menu
FileOption.add_cascade(label="New", menu=NewOption)

# Add the Other File Menu Options
FileOption.add_command(label="Open File", command=OpenFile, accelerator="Ctrl+O")
FileOption.add_command(label="Save File", command=SaveFile, accelerator="Ctrl+S")
FileOption.add_command(label="Save As", command=SaveFileAs, accelerator="Ctrl+Shift+S")
FileOption.add_separator()
FileOption.add_checkbutton(label="Auto Save", onvalue=1, offvalue=0, variable=AutoSave_CheckMark, command=AutoSaveInit)

# Preferences Drop Down Option for File Menu             
PreferencesMenu = Menu(FileOption, tearoff=False)
PreferencesMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
PreferencesMenu.add_command(label="Color Theme", command=ColorTheme)
# Cascade the Preferences menu to the File Menu
FileOption.add_cascade(label="Preferences", menu=PreferencesMenu)

# The Remaining options for the File Menu
FileOption.add_separator()
FileOption.add_command(label="Close Editor", command=CloseEditor)
FileOption.add_command(label="Exit", command=ExitProgram, accelerator="Ctrl+Q")



# Edit Option for Menu Bar
EditOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Edit", menu=EditOption, underline=0)
EditOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
EditOption.add_command(label="Undo", command=TextBox.edit_undo, accelerator="Ctrl+Z")
EditOption.add_command(label="Redo", command=TextBox.edit_redo, accelerator="Ctrl+Y")
EditOption.add_separator()
EditOption.add_command(label="Cut", command=lambda: CutText(False), accelerator="Ctrl+X")
EditOption.add_command(label="Copy", command=lambda: CopyText(False), accelerator="Ctrl+C")
EditOption.add_command(label="Paste", command=lambda: PasteText(False), accelerator="Ctrl+V")
EditOption.add_separator()
EditOption.add_command(label="Toggle Line Comment", command=ToggleLineComment)
EditOption.add_command(label="Toggle Block Comment", command=ToggleBlockComment, accelerator="Ctrl+Shift-A")
EditOption.add_separator()
EditOption.add_command(label="Select All", command=lambda: SelectAll(True), accelerator="Ctrl+A")



# Check Marks for Options in View Menu
Toolbar_CheckMark = BooleanVar()
Toolbar_CheckMark.set(True)

StatusBar_CheckMark = BooleanVar()
StatusBar_CheckMark.set(True)

# View Option for Menu Bar
ViewOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="View", menu=ViewOption, underline=0)
ViewOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
# Add command for the options below
ViewOption.add_checkbutton(label="Show Toolbar", onvalue=1, offvalue=0, variable=Toolbar_CheckMark)     
ViewOption.add_checkbutton(label="Show Status Bar", onvalue=1, offvalue=0, variable=StatusBar_CheckMark)  
#ViewOption.add_separator()
#ViewOption.add_command(label="Zoom In", accelerator="Ctrl++")
#ViewOption.add_command(label="Zoom Out", accelerator="Ctrl+-")



# Run Option for Menu Bar
RunOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Run", menu=RunOption, underline=0)
RunOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
RunOption.add_command(label="Run Python File", command=RunPythonFile)
# Add a debugger in future versions



# Check Marks for Options in Tools Menu
WordWrap_CheckMark = BooleanVar()
WordWrap_CheckMark.set(False)

# Tools Option for Menu Bar
ToolsOption = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Tools", menu=ToolsOption, underline=0)
ToolsOption.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
ToolsOption.add_command(label="Word Count", command=InitWordCount)
ToolsOption.add_checkbutton(label="Toggle Word Wrap", onvalue=1, offvalue=0, variable=WordWrap_CheckMark, command=ToggleWordWrap, accelerator="Alt-Z")
ToolsOption.add_separator()
ToolsOption.add_command(label="Speech to Text", command=Speech_to_Text)
ToolsOption.add_command(label="Template Manager", command=TemplateManagerFunction)



# Help Option for Menu Bar
HelpMenu = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Help", menu=HelpMenu, underline=0)
HelpMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
HelpMenu.add_command(label="Get Started")
HelpMenu.add_command(label="Documentation")
HelpMenu.add_command(label="Release Notes")
HelpMenu.add_command(label="Keyboard Shortcuts Reference")
HelpMenu.add_separator()
HelpMenu.add_command(label="Report Issue")
HelpMenu.add_command(label="View License")
HelpMenu.add_separator()
HelpMenu.add_command(label="Settings", command=None)    # Create new window that has the settings options; For future versions create a tab in the IDE for the settings option
HelpMenu.add_command(label="About", command=AboutScreen)



# Add options - run file 
# Right Click Menu
RightClickMenu = Menu(TextBox, tearoff=False)
RightClickMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
RightClickMenu.add_command(label="Undo", command=TextBox.edit_undo, accelerator="Ctrl+Z")
RightClickMenu.add_command(label="Redo", command=TextBox.edit_redo, accelerator="Ctrl+Y")
RightClickMenu.add_separator()
RightClickMenu.add_command(label="Cut", command=lambda: CutText(False), accelerator="Ctrl+X")
RightClickMenu.add_command(label="Copy", command=lambda: CopyText(False), accelerator="Ctrl+C")
RightClickMenu.add_command(label="Paste", command=lambda: PasteText(False), accelerator="Ctrl+V")
RightClickMenu.add_command(label="Select All", command=lambda: SelectAll(True), accelerator="Ctrl+A")
RightClickMenu.add_separator()
RightClickMenu.add_command(label="Run Python File", command=RunPythonFile)

# Right Click Menu Popup Function
def RightClickMenuPopUp(e):
    RightClickMenu.tk_popup(e.x_root, e.y_root)
# Binding for Right Click and Menu Popup
root.bind("<Button-3>", RightClickMenuPopUp)



# Mainloop
root.mainloop()
