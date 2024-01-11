Help on module tkinter.filedialog in tkinter:

NAME
    tkinter.filedialog - File selection dialog classes.

MODULE REFERENCE
    https://docs.python.org/3.11/library/tkinter.filedialog.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Classes:
    
    - FileDialog
    - LoadFileDialog
    - SaveFileDialog
    
    This module also presents tk common file dialogues, it provides interfaces
    to the native file dialogues available in Tk 4.2 and newer, and the
    directory dialogue available in Tk 8.3 and newer.
    These interfaces were written by Fredrik Lundh, May 1997.

CLASSES
    builtins.object
        FileDialog
            LoadFileDialog
            SaveFileDialog
    tkinter.commondialog.Dialog(builtins.object)
        Directory
    _Dialog(tkinter.commondialog.Dialog)
        Open
        SaveAs
    
    class Directory(tkinter.commondialog.Dialog)
     |  Directory(master=None, **options)
     |  
     |  Ask for a directory
     |  
     |  Method resolution order:
     |      Directory
     |      tkinter.commondialog.Dialog
     |      builtins.object
     |  
     |  Data and other attributes defined here:
     |  
     |  command = 'tk_chooseDirectory'
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from tkinter.commondialog.Dialog:
     |  
     |  __init__(self, master=None, **options)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  show(self, **options)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from tkinter.commondialog.Dialog:
     |  
     |  __dict__
     |      dictionary for instance variables
     |  
     |  __weakref__
     |      list of weak references to the object
    
    class FileDialog(builtins.object)
     |  FileDialog(master, title=None)
     |  
     |  Standard file selection dialog -- no checks on selected file.
     |  
     |  Usage:
     |  
     |      d = FileDialog(master)
     |      fname = d.go(dir_or_file, pattern, default, key)
     |      if fname is None: ...canceled...
     |      else: ...open file...
     |  
     |  All arguments to go() are optional.
     |  
     |  The 'key' argument specifies a key in the global dictionary
     |  'dialogstates', which keeps track of the values for the directory
     |  and pattern arguments, overriding the values passed in (it does
     |  not keep track of the default argument!).  If no key is specified,
     |  the dialog keeps no memory of previous state.  Note that memory is
     |  kept even when the dialog is canceled.  (All this emulates the
     |  behavior of the Macintosh file selection dialogs.)
     |  
     |  Methods defined here:
     |  
     |  __init__(self, master, title=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  cancel_command(self, event=None)
     |  
     |  dirs_double_event(self, event)
     |  
     |  dirs_select_event(self, event)
     |  
     |  files_double_event(self, event)
     |  
     |  files_select_event(self, event)
     |  
     |  filter_command(self, event=None)
     |  
     |  get_filter(self)
     |  
     |  get_selection(self)
     |  
     |  go(self, dir_or_file='.', pattern='*', default='', key=None)
     |  
     |  ok_command(self)
     |  
     |  ok_event(self, event)
     |  
     |  quit(self, how=None)
     |  
     |  set_filter(self, dir, pat)
     |  
     |  set_selection(self, file)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables
     |  
     |  __weakref__
     |      list of weak references to the object
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  title = 'File Selection Dialog'
    
    class LoadFileDialog(FileDialog)
     |  LoadFileDialog(master, title=None)
     |  
     |  File selection dialog which checks that the file exists.
     |  
     |  Method resolution order:
     |      LoadFileDialog
     |      FileDialog
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  ok_command(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  title = 'Load File Selection Dialog'
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from FileDialog:
     |  
     |  __init__(self, master, title=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  cancel_command(self, event=None)
     |  
     |  dirs_double_event(self, event)
     |  
     |  dirs_select_event(self, event)
     |  
     |  files_double_event(self, event)
     |  
     |  files_select_event(self, event)
     |  
     |  filter_command(self, event=None)
     |  
     |  get_filter(self)
     |  
     |  get_selection(self)
     |  
     |  go(self, dir_or_file='.', pattern='*', default='', key=None)
     |  
     |  ok_event(self, event)
     |  
     |  quit(self, how=None)
     |  
     |  set_filter(self, dir, pat)
     |  
     |  set_selection(self, file)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from FileDialog:
     |  
     |  __dict__
     |      dictionary for instance variables
     |  
     |  __weakref__
     |      list of weak references to the object
    
    class Open(_Dialog)
     |  Open(master=None, **options)
     |  
     |  Ask for a filename to open
     |  
     |  Method resolution order:
     |      Open
     |      _Dialog
     |      tkinter.commondialog.Dialog
     |      builtins.object
     |  
     |  Data and other attributes defined here:
     |  
     |  command = 'tk_getOpenFile'
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from tkinter.commondialog.Dialog:
     |  
     |  __init__(self, master=None, **options)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  show(self, **options)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from tkinter.commondialog.Dialog:
     |  
     |  __dict__
     |      dictionary for instance variables
     |  
     |  __weakref__
     |      list of weak references to the object
    
    class SaveAs(_Dialog)
     |  SaveAs(master=None, **options)
     |  
     |  Ask for a filename to save as
     |  
     |  Method resolution order:
     |      SaveAs
     |      _Dialog
     |      tkinter.commondialog.Dialog
     |      builtins.object
     |  
     |  Data and other attributes defined here:
     |  
     |  command = 'tk_getSaveFile'
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from tkinter.commondialog.Dialog:
     |  
     |  __init__(self, master=None, **options)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  show(self, **options)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from tkinter.commondialog.Dialog:
     |  
     |  __dict__
     |      dictionary for instance variables
     |  
     |  __weakref__
     |      list of weak references to the object
    
    class SaveFileDialog(FileDialog)
     |  SaveFileDialog(master, title=None)
     |  
     |  File selection dialog which checks that the file may be created.
     |  
     |  Method resolution order:
     |      SaveFileDialog
     |      FileDialog
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  ok_command(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  title = 'Save File Selection Dialog'
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from FileDialog:
     |  
     |  __init__(self, master, title=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  cancel_command(self, event=None)
     |  
     |  dirs_double_event(self, event)
     |  
     |  dirs_select_event(self, event)
     |  
     |  files_double_event(self, event)
     |  
     |  files_select_event(self, event)
     |  
     |  filter_command(self, event=None)
     |  
     |  get_filter(self)
     |  
     |  get_selection(self)
     |  
     |  go(self, dir_or_file='.', pattern='*', default='', key=None)
     |  
     |  ok_event(self, event)
     |  
     |  quit(self, how=None)
     |  
     |  set_filter(self, dir, pat)
     |  
     |  set_selection(self, file)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from FileDialog:
     |  
     |  __dict__
     |      dictionary for instance variables
     |  
     |  __weakref__
     |      list of weak references to the object

FUNCTIONS
    askdirectory(**options)
        Ask for a directory, and return the file name
    
    askopenfile(mode='r', **options)
        Ask for a filename to open, and returned the opened file
    
    askopenfilename(**options)
        Ask for a filename to open
    
    askopenfilenames(**options)
        Ask for multiple filenames to open
        
        Returns a list of filenames or empty list if
        cancel button selected
    
    askopenfiles(mode='r', **options)
        Ask for multiple filenames and return the open file
        objects
        
        returns a list of open file objects or an empty list if
        cancel selected
    
    asksaveasfile(mode='w', **options)
        Ask for a filename to save as, and returned the opened file
    
    asksaveasfilename(**options)
        Ask for a filename to save as

DATA
    __all__ = ['FileDialog', 'LoadFileDialog', 'SaveFileDialog', 'Open', '...

FILE
    c:\program files\windowsapps\pythonsoftwarefoundation.python.3.11_3.11.2032.0_x64__qbz5n2kfra8p0\lib\tkinter\filedialog.py

