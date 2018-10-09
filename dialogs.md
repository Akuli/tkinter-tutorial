# Message Dialogs

Now we know how to make a button that prints a message on the terminal.
But that's boring! We want to display a nice message box instead.

## Built-in dialogs

Tkinter comes with many useful functions for making message dialogs.
Here's a simple example:

[include]: # (hello-world.py)
```python
import tkinter
from tkinter import ttk, messagebox


def do_hello_world():
    messagebox.showinfo("Important Message", "Hello World!")


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="Click me", command=do_hello_world)
button.pack()
root.mainloop()
```

That's pretty cool. We can create a dialog with a label and an OK button
and wait for the user to click the button with just one function call.
[The callback is blocking](buttons.md#blocking-callback-functions), but
it doesn't matter here because Tk handles dialogs specially.

The `tkinter.messagebox` module supports many other things too, and
there are other modules like it as well. Here's an example that
demonstrates most of the things that are possible. You can use this
program when you need to use a dialog so you don't need to remember
which function to use.

Note that many of these functions return None if you close the dialog
using the X button in the corner.

[include]: # (dialog-tester.py)
```python
import functools
import tkinter
from tkinter import ttk, messagebox, filedialog, simpledialog, colorchooser


class Demo:

    def __init__(self, big_frame, modulename):
        self.frame = ttk.LabelFrame(big_frame, text=("tkinter." + modulename))
        self.modulename = modulename

    # this makes buttons that demonstrate messagebox functions
    # it's a bit weird but it makes this code much less repetitive
    def add_button(self, functionname, function, args=(), kwargs=None):
        # see http://stackoverflow.com/q/1132941
        if kwargs is None:
            kwargs = {}

        # the call_string will be like "messagebox.showinfo('Bla Bla', 'Bla')"
        parts = []
        for arg in args:
            parts.append(repr(arg))
        for key, value in kwargs.items():
            parts.append(key + "=" + repr(value))
        call_string = "%s.%s(%s)" % (self.modulename, functionname,
                                     ', '.join(parts))

        callback = functools.partial(self.on_click, call_string,
                                     function, args, kwargs)
        button = ttk.Button(self.frame, text=functionname, command=callback)
        button.pack()

    def on_click(self, call_string, function, args, kwargs):
        print('running', call_string)
        result = function(*args, **kwargs)
        print('  it returned', repr(result))


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

msgboxdemo = Demo(big_frame, "messagebox")
msgboxdemo.add_button(
    "showinfo", messagebox.showinfo,
    ["Important Message", "Hello World!"])
msgboxdemo.add_button(
    "showwarning", messagebox.showwarning,
    ["Warny Warning", "This may cause more problems."])
msgboxdemo.add_button(
    "showerror", messagebox.showerror,
    ["Fatal Error", "Something went wrong :("])
msgboxdemo.add_button(
    "askyesno", messagebox.askyesno,
    ["Important Question", "Do you like this?"])
msgboxdemo.add_button(
    "askyesnocancel", messagebox.askyesnocancel,
    ["Important Question", "Do you like this?"])
msgboxdemo.add_button(
    "askokcancel", messagebox.askokcancel,
    ["Stupid Question", "Do you really want to do this?"])
msgboxdemo.add_button(
    "askyesnocancel", messagebox.askyesnocancel,
    ["Save Changes?", "Do you want to save your changes before quitting?"])

filedialogdemo = Demo(big_frame, "filedialog")
filedialogdemo.add_button(
    "askopenfilename", filedialog.askopenfilename,
    kwargs={'title': "Open File"})
filedialogdemo.add_button(
    "asksaveasfilename", filedialog.asksaveasfilename,
    kwargs={'title': "Save As"})

simpledialogdemo = Demo(big_frame, "simpledialog")
simpledialogdemo.add_button(
    "askfloat", simpledialog.askfloat,
    ["Pi Question", "What's the value of pi?"])
simpledialogdemo.add_button(
    "askinteger", simpledialog.askinteger,
    ["Computer Question", "How many computers do you have?"])
simpledialogdemo.add_button(
    "askstring", simpledialog.askstring,
    ["Editor Question", "What is your favorite editor?"])

colorchooserdemo = Demo(big_frame, "colorchooser")
colorchooserdemo.add_button(
    "askcolor", colorchooser.askcolor,
    kwargs={'title': "Choose a Color"})

msgboxdemo.frame.grid(row=0, column=0, rowspan=3)
filedialogdemo.frame.grid(row=0, column=1)
simpledialogdemo.frame.grid(row=1, column=1)
colorchooserdemo.frame.grid(row=2, column=1)

root.title("Dialog Tester")
root.resizable(False, False)
root.mainloop()
```

As you can see, using [a
class](https://github.com/Akuli/python-tutorial/blob/master/basics/classes.md)
is handy with bigger programs. I explained `functools.partial`
[here](buttons.md#passing-arguments-to-callback-functions), so you can
read that if you haven't seen it before.

Many of these functions can take other keyword arguments too. Most of
them are explained in [the manual pages](getting-started.md#manual-pages).

[comment]: # (tk_getSaveFile is also documented in tk_getOpenFile)

| Python module           | Manual page                                                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `tkinter.messagebox`    | [tk_messageBox(3tk)]                                                                                                        |
| `tkinter.filedialog`    | [tk_getOpenFile(3tk)] and [tk_chooseDirectory(3tk)]                                                                         |
| `tkinter.colorchooser`  | [tk_chooseColor(3tk)]                                                                                                       |
| `tkinter.simpledialog`  | No manual page, but the module seems to be from [this tutorial](http://effbot.org/tkinterbook/tkinter-dialog-windows.htm).  |

## Message dialogs without the root window

Let's try displaying a message without making a root window first and
see if it works:

```python
>>> from tkinter import messagebox
>>> messagebox.askyesno("Test", "Does this work?")
```

This code creates a message box correctly, but it also creates a stupid
window in the background. The problem is that tkinter needs a root
window to display the message, but we didn't create a root window yet so
tkinter created it for us.

Sometimes it makes sense to display a message dialog without creating
any other windows. For example, our program might need to display an
error message and exit before the main window is created.

In these cases, we can create a root window and hide it with the
`withdraw()` method. It's documented in [wm(3tk)]
as `wm withdraw`; you can scroll down to it or just press Ctrl+F
and type "withdraw".

[include]: # (startup-error.py)
```python
import tkinter
from tkinter import messagebox


root = tkinter.Tk()
root.withdraw()

messagebox.showerror("Fatal Error", "Something went badly wrong :(")
```

The root window hides itself so quickly that we don't notice it at all. It's
also possible to unhide it like `root.deiconify()`.

## Custom dialogs

Tkinter's default dialogs are enough most of the time, but sometimes it
makes sense to create a custom dialog. For example, a tkinter program
might have a custom setting dialog, but everything else would be done
with tkinter's dialogs.

It might be tempting to create multiple root windows, but **don't do
this, this example is BAD**:

[include]: # (two-roots-bad.py)
```python
import tkinter
from tkinter import ttk


def display_dialog():
    root2 = tkinter.Tk()      # BAD! NO!!
    big_frame2 = ttk.Frame(root2)
    big_frame2.pack(fill='both', expand=True)

    ttk.Label(big_frame2, text="Hello World").place(relx=0.5, rely=0.3, anchor='center')
    root2.mainloop()


root = tkinter.Tk()
button = ttk.Button(root, text="Click me", command=display_dialog)
button.pack()
root.mainloop()
```

Things like message boxes need a root window, and if we create more than one
root window, we can't be sure about which root window is used and we may
get weird problems. Or worse, your code may work just fine for you and someone
else running it will get weird problems.

The [toplevel(3tk)] widget is a window that uses an existing root window:

[include]: # (toplevel.py)
```python
import tkinter
from tkinter import ttk


def display_dialog():
    dialog = tkinter.Toplevel()
    big_frame = ttk.Frame(dialog)
    big_frame.pack(fill='both', expand=True)

    label = ttk.Label(big_frame, text="Hello World")
    label.place(relx=0.5, rely=0.3, anchor='center')

    dialog.transient(root)
    dialog.geometry('300x150')
    dialog.wait_window()


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="Click me", command=display_dialog)
button.pack()
root.mainloop()
```

You probably understand how most of this code works, but there are a
couple lines that need explanations:

```python
dialog = tk.Toplevel()
```

The toplevel widget uses our root window even though we don't explicitly
give it a root window. You can also do `tk.Toplevel(root)` if you like
that more.

```python
dialog.transient(root)
```

This line makes the dialog look like it belongs to the root window. It's
always in front of the root window, and it may be centered over the root
window too. You can leave this out if you don't like it.

```python
dialog.wait_window()
```

This is like `root.mainloop()`, it waits until the dialog is destroyed.
You don't need to call this method if you want to let the user do other
things while the dialog is showing.

Clicking on the X button destroys the dialog, but it's also possible to
destroy it like `dialog.destroy()`. This is useful for creating buttons
that close the dialog:

```python
okbutton = ttk.Button(dialog, text="OK", command=dialog.destroy)
```

## "Do you want to quit" dialogs

Many programs display a "do you want to save your changes?" dialog when
the user closes the main window. We can also do this with tkinter using
the `root.protocol()` method. It's documented in [wm(3tk)] as `wm protocol`.

[include]: # (wanna-quit.py)
```python
import tkinter
from tkinter import messagebox


def wanna_quit():
    if messagebox.askyesno("Quit", "Do you really want to quit?"):
        # the user clicked yes, let's close the window
        root.destroy()


root = tkinter.Tk()
root.protocol('WM_DELETE_WINDOW', wanna_quit)
root.mainloop()
```

## Running dialogs on startup

Some programs display dialogs before the main window appears. We can also do
that in tkinter.

[include]: # (startup-dialog.py)
```python
import tkinter
from tkinter import ttk


# only use this before creating the main root window! otherwise you get
# two root windows at the same time, and that's bad, see above
def startup_dialog(labeltext):
    result = None
    rooty_dialog = tkinter.Tk()
    big_frame = ttk.Frame(rooty_dialog)
    big_frame.pack(fill='both', expand=True)

    # result is left to None if the dialog is closed without clicking OK
    def on_ok():
        # usually 'result = entry.get()' creates a local variable called
        # result, but this thing makes it also appear outside on_ok()
        nonlocal result

        result = entry.get()
        rooty_dialog.destroy()   # stops rooty_dialog.mainloop()

    label = ttk.Label(big_frame, text=labeltext)
    label.place(relx=0.5, rely=0.3, anchor='center')
    entry = ttk.Entry(big_frame)
    entry.place(relx=0.5, rely=0.5, anchor='center')
    okbutton = ttk.Button(big_frame, text="OK", command=on_ok)
    okbutton.place(relx=0.5, rely=0.8, anchor='center')

    rooty_dialog.geometry('250x150')
    rooty_dialog.mainloop()

    # now the dialog's mainloop has stopped, so the dialog doesn't exist
    # anymore and creating another root window is ok
    return result


name = startup_dialog("Enter your name:")
if name is not None:      # the user clicked OK
    root = tkinter.Tk()
    big_frame = ttk.Frame(root)
    big_frame.pack(fill='both', expand=True)

    label = ttk.Label(big_frame, text=("Hello %s!" % name))
    label.pack()
    root.mainloop()
```

Earlier I said that having multiple root windows **at the same time** is bad,
but this is ok because we only have one root window at a time; we destroy the
old root window before creating a new one.

## Summary

- Tkinter comes with many handy dialogs functions. You can use the test
  program in this tutorial to decide which function to use.
- If you don't want a root window, you can create it and hide it
  immediately with the `withdraw()` method.
- Don't use multiple root windows at the same time. Use `tk.Toplevel` instead;
  it has a handy `transient()` method too.
- You can use `some_window.protocol('WM_DELETE_WINDOW', callback)` to
  change what clicking the X button does. You can close the window with
  the `destroy()` method.

[manpage list]: # (start)
[tk_chooseColor(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/chooseColor.htm
[tk_chooseDirectory(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/chooseDirectory.htm
[tk_getOpenFile(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/getOpenFile.htm
[tk_messageBox(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/messageBox.htm
[toplevel(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/toplevel.htm
[wm(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/wm.htm
[manpage list]: # (end)
