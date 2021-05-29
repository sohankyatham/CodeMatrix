'''
Create UserInfo.py  
This will store all the User Information; i.e If user have autosave turned on, if user has word wrap turned  on,
to see which color theme the user has, see if user has word count turned on, and apply settings.
'''

'''
from UserInfo.py import *

# Create a value if autosave is on - get the value from UserInfo.py, 
# If autosave is turned on then, UserInfo.py.write(auto is turned on)
# then from CodeKnight_main_.py get the value to see if autosave was turned on
# Call this function in a mainloop
if autosave value = on:
    call the autosave function
if autosave value = off:
    disable the autosave function
'''

# Imports
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter.font as tkfont

# Importing File Templates from FileTemplates.py
from FileTemplates import *



# Window
root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Code Knight")   



# Global OpenStatusName - used for finding name and status of opened file and use it for saving file and etc
global OpenFileStatusName
OpenFileStatusName = False



# File Type Variable - used for finding the file type of the file (i.e .py for Python, .html for HTML)
global FileType
FileType = ""



# Global SelectedText - used for storing any selected text and then pasting text into textbox
global SelectedText
SelectedText = False
 


# File Menu Functions



# New File Function
# Make New tab when this function is passed
def NewFile(*args):
    global OpenFileStatusName
    OpenFileStatusName = False
    # Create a New Tab when new file function occurs
    TextBox.delete("1.0", END) 
root.bind('<Control-Key-n>', NewFile)
 

 
# Open File Function
def OpenFile(*args):
    # Ask user for which file they want to open
    FilePath = filedialog.askopenfilename(initialdir="C:/gui/", title="Open a File", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"),("JavaScript Files", "*.js"), ("Python Files", "*.py")))
    print(FilePath)
    # Check to see if there is a file opened, then find the name and status of the file and use it in code for other things like saving a file and accessing it later
    if FilePath:
        global OpenFileStatusName
        global FileType
        OpenFileStatusName = FilePath
        FileType = OpenFileStatusName
    
    TextBox.delete("1.0", END)
    
    # Open File and Insert File Content into Editor
    FilePath = open(FilePath, 'r')
    FileContent = FilePath.read()
    TextBox.insert(END, FileContent)
    FilePath.close()
root.bind('<Control-Key-o>', OpenFile)
 
 

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
root.bind('<Control-Key-s>', SaveFile)
 

 
# Save File As Function
def SaveFileAs(*args):
    FilePath = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/", title="Save File As", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("JavaScript Files", "*.js"), ("Python Files", "*.py")))
    if FilePath:
        global FileType
        FileType = FilePath
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
    TextBox.after(1000, AutoSaveInit)



# Preferences Drop Down Menu in File Menu



# Keyboard Shortcuts Function



# Choose Color Theme Function
def ChooseColorTheme():
    # Color Theme Window
    ColorThemeWindow = Toplevel(root)
    ColorThemeWindow.geometry("250x150")
    ColorThemeWindow.title("Color Theme")
    ColorThemeWindow.resizable(0,0)

    # Cancel Color Theme Function
    def CancelColorThemeFunc():
        ColorThemeWindow.destroy()

    # Color Theme Function
    def ColorThemeFunc():
        # Get the Value from the Combobox
        ColorTheme = SelectedColorTheme.get()
        # Set the Default Theme
        if ColorTheme == "Default":
            print("Default Color Theme Activated")
        # Set the Light Theme
        if ColorTheme == "Light (Code Knight)":
            print("Light Color Theme Activated")
        # Set the Dark Theme
        if ColorTheme == "Dark (Code Knight)":
            print("Dark Color Theme Activated")
        # Set the Red Theme
        if ColorTheme == "Red":
            TextBox.config(bg="Red", fg="White", selectbackground="Dodgerblue")
            MenuBar.config(bg="Red", fg="Black")
            StatusBar.config(bg="Red")
            

    # Color Theme Label
    ColorThemeLabel = Label(ColorThemeWindow, text="Color Theme", font=("Arial", 16))
    ColorThemeLabel.pack()

    # Set the SelectedColorTheme to a String Value
    SelectedColorTheme = StringVar()

    # Color Theme Combobox for selecting a Color Theme
    ColorTheme = ttk.Combobox(ColorThemeWindow, width=16, textvariable=SelectedColorTheme, font=("Arial", 11))
    ColorTheme.pack(pady=20)

    # Value for Color Themes
    ColorTheme["values"] = [
        "Default",
        "Light (Code Knight)",
        "Dark (Code Knight)",
        "Red",
    ]

    # Set Default Theme to the 0th Value from ColorTheme["values"]
    ColorTheme.current(0)

    # Frame for Placing Cancel and Ok button on ColorThemeWindow 
    ColorThemeBtns_Frame = Frame(ColorThemeWindow)
    ColorThemeBtns_Frame.pack()

    # Cancel Button
    CancelBtn = Button(ColorThemeBtns_Frame, text="Cancel", width=6, font=("Arial", 11), command=CancelColorThemeFunc)
    CancelBtn.grid(row=0, column=0)

    # Ok Button
    OkBtn = Button(ColorThemeBtns_Frame, text="Ok", width=6, font=("Arial", 11), command=ColorThemeFunc)
    OkBtn.grid(row=0, column=1)
    
    # Main Loop for Color Theme Window
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



# File Templates Functions
                     


# Basic HTML Markup Function
def Basic_HTML_Markup_Function():
    global OpenFileStatusName
    OpenFileStatusName = False
    # Delete Previous Content and Insert HTML Template in TextBox
    TextBox.delete("1.0", END)
    TextBox.insert("1.0", Basic_HTML_Markup.strip())



# Basic PHP File Function
def Basic_PHP_File_Function():
    global OpenFileStatusName
    OpenFileStatusName = False
    # Delete Previous Content and Insert PHP Template in TextBox
    TextBox.delete("1.0", END)
    TextBox.insert("1.0", Basic_PHP_File.strip())



# C++ Start File Function
def C_Plus_Plus_StartFile_Function():
    global OpenFileStatusName
    OpenFileStatusName = False
    # Delete Previous Content and Insert C++ Template in TextBox
    TextBox.delete("1.0", END)
    TextBox.insert("1.0", C_Plus_Plus_StartFile.strip())



# JAVA Start File Function
def JAVA_Start_File_Function():
    global OpenFileStatusName
    OpenFileStatusName = False
    # Delete Previous Content and Insert JAVA Template in TextBox
    TextBox.delete("1.0", END)
    TextBox.insert("1.0", JAVA_Start_File.strip())



# Python Start File Function
def Python_Start_File_Function():
    global OpenFileStatusName
    OpenFileStatusName = False
    # Delete Previous Content and Insert Python Template in TextBox
    TextBox.delete("1.0", END)
    TextBox.insert("1.0", Python_Start_File.strip())



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
    global OpenFileStatusName

    OpenFileToRun = filedialog.askopenfile(mode="r", title="Select Python File to Run")
    exec(OpenFileToRun.read())



def ToggleLineComment(*args):
    TextBox.insert("1.0", "# ")
# Add binding root.bind("<Control-Key-/>", ToggleLineComment)



def ToggleBlockComment(*args):
    TextBox.insert("1.0", "''' \n\n'''")
root.bind("<Control-Shift-A>", ToggleBlockComment)



# Tools Menu Options



# Declare Word Count and Character Count Function
def DeclareWordCount():
    # Get data in textbox - turn into a string
    TextContent_ForWordCount = TextBox.get("1.0", END)
    # String to number 
    CharactersInTextBox = len(TextContent_ForWordCount)    
    WordsInTextBox = len(TextContent_ForWordCount.split()) 
    # Config in Status Bar
    StatusBar.config(text="Ln 5, Col 6     -     " + str(CharactersInTextBox-1) + " Characters, " + str(WordsInTextBox) + " Words, ")



# Initialize Word Count Function - check if the function is already active, if it is, then turn of word count
def InitWordCount():
    if WordCount_CheckMark.get():
        DeclareWordCount()
        StatusBar.after(1, InitWordCount)
    else: 
        StatusBar.config(text="Code Knight")



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



# Help Menu Functions



# About Screen Function - MAYBE - PLACE IN A NEW FILE
def AboutScreen():
    # About Screen Window
    AboutScreenPopUp = Toplevel(root)
    AboutScreenPopUp.title("About")
    AboutScreenPopUp.geometry("300x300")
    AboutScreenPopUp.resizable(0,0)
    #AboutScreenPopUp.transient(1)

    # Header
    AboutHeader = Label(AboutScreenPopUp, text="Code Knight", font=("Arial", 30))
    AboutHeader.pack(pady=25)

    # Attribution
    AboutHeaderAttribtion = Label(AboutScreenPopUp, text="By: Sohan Kyatham", font=("Arial", 12))
    AboutHeaderAttribtion.pack()

    # Version
    AboutVersion = Label(AboutScreenPopUp, text="Version: 1.0.0", font=("Arial", 12))
    AboutVersion.pack()

    # Operating System Version
    AboutOS = Label(AboutScreenPopUp, text="OS: Linux", font=("Arial", 12))
    AboutOS.pack()

    # Mainloop
    AboutScreenPopUp.mainloop()



# WORK ON USER INTERFACE FOR SETTINGS WINDOW
# Function for Settings Window
def SettingsWindowFunc():
    # Window
    SettingsWindow = Toplevel(root)
    SettingsWindow.geometry("600x600")
    SettingsWindow.title("Settings Window")

    '''
    Create Tabs:
        Text Editor:
            Font Family
            Font Size
            Font Weight
            Cursor Options
            Auto Save Checkbox
            Auto Save Delay
            Word Wrap
            Tab Size
            

    
    '''
    # Mainloop
    SettingsWindow.mainloop()


# For future versions - add tabs so users can work with multiple files at once
# Tab Control --- place for adding new tab
# TabControl = ttk.Notebook(root)
# TabControl.pack()



# Add stuff like word count, character count, what the location of the mouse is like for eg: Ln 22, Col 2
# Status Bar
StatusBar = Label(root, text="Code Knight", anchor=W)
StatusBar.config(bg="Dodgerblue")
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
TextBox = Text(MainFrame, width=500, font=("DejaVu Sans Mono", 16), selectbackground="Skyblue", undo=True, wrap="none", yscrollcommand=VerticalScrollbar.set, xscrollcommand=HorizontalScrollbar.set)
TextBox.pack(fill=BOTH)

# Set Tab Size for Text Box - Default is 4 Spaces
font = tkfont.Font(font=TextBox['font'])
TabSize = font.measure("    ")
TextBox.config(tabs=TabSize)
    
    

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
FileMenu = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="File", menu=FileMenu, underline=0)
FileMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))

FileMenu.add_command(label="New File", command=NewFile)

# New (from template) Menu - Drop Down with Options for File Menu             
NewFromTemplate = Menu(FileMenu, tearoff=False)
NewFromTemplate.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
NewFromTemplate.add_command(label="file.html", command=Basic_HTML_Markup_Function)
NewFromTemplate.add_command(label="file.php", command=Basic_PHP_File_Function)
NewFromTemplate.add_command(label="main.cxx", command=C_Plus_Plus_StartFile_Function)
NewFromTemplate.add_command(label="main.java", command=JAVA_Start_File_Function)
NewFromTemplate.add_command(label="main.py", command=Python_Start_File_Function)
# Cascade the New Menu to the File Menu
FileMenu.add_cascade(label="New (from template)", menu=NewFromTemplate)

# Add the Other File Menu Options
FileMenu.add_command(label="Open File", command=OpenFile, accelerator="Ctrl+O") # Add Open Folder & Open Recent
FileMenu.add_separator()
FileMenu.add_command(label="Save", command=SaveFile, accelerator='Ctrl+S')
FileMenu.add_command(label="Save As", command=SaveFileAs, accelerator="Ctrl+Shift+S")
FileMenu.add_separator()
FileMenu.add_checkbutton(label="Auto Save", onvalue=1, offvalue=0, variable=AutoSave_CheckMark, command=AutoSaveInit)

# Preferences Menu - Drop Down with Options for File Menu             
PreferencesMenu = Menu(FileMenu, tearoff=False)
PreferencesMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
PreferencesMenu.add_command(label="Settings", command=SettingsWindowFunc)
PreferencesMenu.add_command(label="Color Theme", command=ChooseColorTheme)
PreferencesMenu.add_command(label="Keyboard Shortcuts", command=None)
# Cascade the Preferences Menu to the File Menu
FileMenu.add_cascade(label="Preferences", menu=PreferencesMenu)
FileMenu.add_separator()

# Add the Other File Menu Options
FileMenu.add_command(label="Close Editor", command=CloseEditor, accelerator="Ctrl+W")
FileMenu.add_command(label="Exit", command=ExitProgram, accelerator="Ctrl+Q")



# Edit Menu for Menu Bar
EditMenu = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Edit", menu=EditMenu, underline=0)
EditMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
EditMenu.add_command(label="Undo", command=TextBox.edit_undo, accelerator="Ctrl+Z")
EditMenu.add_command(label="Redo", command=TextBox.edit_redo, accelerator="Ctrl+Y")
EditMenu.add_separator()
EditMenu.add_command(label="Cut", command=lambda: CutText(False), accelerator="Ctrl+X")
EditMenu.add_command(label="Copy", command=lambda: CopyText(False), accelerator="Ctrl+C")
EditMenu.add_command(label="Paste", command=lambda: PasteText(False), accelerator="Ctrl+V")
EditMenu.add_separator()
# Work on Find and Replace Function; Add some other feature to go with the menu       
EditMenu.add_command(label="Find & Replace", command=None, accelerator="Ctrl+F")
EditMenu.add_separator()
EditMenu.add_command(label="Toggle Line Comment", command=ToggleLineComment, accelerator="Ctrl+/")
EditMenu.add_command(label="Toggle Block Comment", command=ToggleBlockComment, accelerator="Ctrl+Shift-A")
EditMenu.add_separator()
EditMenu.add_command(label="Select All", command=lambda: SelectAll(True), accelerator="Ctrl+A")



# Check Marks for Options in View Menu
Toolbar_CheckMark = BooleanVar()
Toolbar_CheckMark.set(True)

StatusBar_CheckMark = BooleanVar()
StatusBar_CheckMark.set(True)



# View Menu for Menu Bar
ViewMenu = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="View", menu=ViewMenu, underline=0)
ViewMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
# Add command for the options below
ViewMenu.add_checkbutton(label="Show Toolbar", onvalue=1, offvalue=0, variable=Toolbar_CheckMark)     
ViewMenu.add_checkbutton(label="Show Status Bar", onvalue=1, offvalue=0, variable=StatusBar_CheckMark)  
#ViewMenu.add_separator()
#ViewMenu.add_command(label="Zoom In", accelerator="Ctrl++")
#ViewMenu.add_command(label="Zoom Out", accelerator="Ctrl+-")



# Run Menu for Menu Bar
RunMenu = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Run", menu=RunMenu, underline=0)
RunMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
RunMenu.add_command(label="Run Python File", command=RunPythonFile)
# Add a debugger in future versions



# Check Marks for Options in Tools Menu
WordCount_CheckMark = BooleanVar()
WordCount_CheckMark.set(False)

WordWrap_CheckMark = BooleanVar()
WordWrap_CheckMark.set(False)



# Tools Menu for Menu Bar
ToolsMenu = Menu(MenuBar, tearoff=False)
MenuBar.add_cascade(label="Tools", menu=ToolsMenu, underline=0)
ToolsMenu.config(bg="White", fg="Black", activebackground="Whitesmoke", activeforeground="Black", activeborderwidth=1, font=('Monaco', 11))
ToolsMenu.add_checkbutton(label="Word Count", onvalue=1, offvalue=0, variable=WordCount_CheckMark, command=InitWordCount)
ToolsMenu.add_checkbutton(label="Toggle Word Wrap", onvalue=1, offvalue=0, variable=WordWrap_CheckMark, command=ToggleWordWrap, accelerator="Alt-Z")



# Help Menu for Menu Bar
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
RightClickMenu.add_command(label="Run Python File", command=RunPythonFile) # Change this to Run File
 
# Right Click Menu Popup Function
def RightClickMenuPopUp(e):
    RightClickMenu.tk_popup(e.x_root, e.y_root)
# Binding for Right Click and Menu Popup
root.bind("<Button-3>", RightClickMenuPopUp)



# Mainloop
root.mainloop()
