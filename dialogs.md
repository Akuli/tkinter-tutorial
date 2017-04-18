# Message Dialogs

Now we know how to make a button that prints a message on the terminal.
But that's boring! We want to display a nice message box instead.

## Tkinter's dialogs

Tkinter comes with many useful functions for making message dialogs.
Here's a simple example:

[include]: # (examples/hello-world-msgbox.py)
```python
import tkinter as tk
from tkinter import messagebox


def do_hello_world():
    messagebox.showinfo("Important Message", "Hello World!")


root = tk.Tk()
button = tk.Button(root, text="Click me", command=do_hello_world)
button.pack()
root.mainloop()
```

That's pretty cool. We can create a dialog with a label and an OK button
and wait for the user to click the button with just one function call.

If you have used [buttons](buttons.md) before most of the code is pretty
easy to understand. There's only one thing that needs explaning:

```python
import tkinter as tk
from tkinter import messagebox
```

This probably feels a bit odd. First we import the whole tkinter as
`tk`, but then we need to separately dig a `messagebox` module from
tkinter. Why can't we just `import tkinter as tk` and use
`tk.messagebox`? Actually we can, but only if something else has already
imported the `messagebox`, so it's not a good idea.

The reason is that `import tkinter` actually loads
`tkinter/__init__.py`, but `tkinter.messagebox` comes from
`tkinter/messagebox.py`:

```python
>>> import tkinter      # only __init__.py loads
>>> tkinter
<module 'tkinter' from '/bla/bla/bla/tkinter/__init__.py'>
>>> tkinter.messagebox
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'tkinter' has no attribute 'messagebox'
>>> import tkinter.messagebox   # now messagebox.py loads too
>>> tkinter.messagebox
<module 'tkinter.messagebox' from '/bla/bla/bla/tkinter/messagebox.py'>
>>>
```

Here Python didn't load `tkinter.messagebox` right away because many
tkinter programs don't need it and `import tkinter` runs faster if
Python doesn't need to load `messagebox.py` at all.

The `tkinter.messagebox` module supports many other things too, and
there are other modules like it as well. Here's an example that
demonstrates most of the things that are possible. You can use this
program when you need to use a dialog, but you don't remember which
function you should use.

Note that many of these functions return None if you close the dialog
using the X button in the corner.

[include]: # (examples/many-msgboxes.py)
```python
import functools
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, colorchooser


class DemoLabelFrame(tk.LabelFrame):

    def __init__(self, root, modulename):
        super().__init__(root, text=("tkinter." + modulename))
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
        button = tk.Button(self, text=functionname, command=callback)
        button.pack()

    def on_click(self, call_string, function, args, kwargs):
        print('running', call_string)
        result = function(*args, **kwargs)
        print('  it returned', repr(result))


root = tk.Tk()

messageboxframe = DemoLabelFrame(root, "messagebox")
messageboxframe.add_button(
    "showinfo", messagebox.showinfo,
    ["Important Message", "Hello World!"])
messageboxframe.add_button(
    "showwarning", messagebox.showwarning,
    ["Warny Warning", "This may cause more problems."])
messageboxframe.add_button(
    "showerror", messagebox.showerror,
    ["Fatal Error", "Something went wrong :("])
messageboxframe.add_button(
    "askyesno", messagebox.askyesno,
    ["Important Question", "Do you like this?"])
messageboxframe.add_button(
    "askyesnocancel", messagebox.askyesnocancel,
    ["Important Question", "Do you like this?"])
messageboxframe.add_button(
    "askokcancel", messagebox.askokcancel,
    ["Stupid Question", "Do you really want to do this?"])
messageboxframe.add_button(
    "askyesnocancel", messagebox.askyesnocancel,
    ["Save Changes?", "Do you want to save your changes before quitting?"])

filedialogframe = DemoLabelFrame(root, "filedialog")
filedialogframe.add_button(
    "askopenfilename", filedialog.askopenfilename,
    kwargs={'title': "Open File"})
filedialogframe.add_button(
    "asksaveasfilename", filedialog.asksaveasfilename,
    kwargs={'title': "Save As"})

simpledialogframe = DemoLabelFrame(root, "simpledialog")
simpledialogframe.add_button(
    "askfloat", simpledialog.askfloat,
    ["Pi Question", "What's the value of pi?"])
simpledialogframe.add_button(
    "askinteger", simpledialog.askinteger,
    ["Computer Question", "How many computers do you have?"])
simpledialogframe.add_button(
    "askstring", simpledialog.askstring,
    ["Editor Question", "What is your favorite editor?"])

colorchooserframe = DemoLabelFrame(root, "colorchooser")
colorchooserframe.add_button(
    "askcolor", colorchooser.askcolor,
    kwargs={'title': "Choose a Color"})

messageboxframe.grid(row=0, column=0, rowspan=3)
filedialogframe.grid(row=0, column=1)
simpledialogframe.grid(row=1, column=1)
colorchooserframe.grid(row=2, column=1)

root.title("Dialog Tester")
root.resizable(False, False)
root.mainloop()
```

As you can see, using [a
class](https://github.com/Akuli/python-tutorial/blob/master/basics/classes.md)
is handy with bigger programs. I explained `functools.partial`
[here](buttons.md#passing-arguments-to-callback-functions), so you can
read that if you haven't seen it before.

## Message dialogs without the root window

Let's try displaying a message without making a root window first and
see if it works:

```python
>>> from tkinter import messagebox
>>> messagebox.askyesno("Test", "Does this work?")
```

This code creates a message box correctly, but it also creates a stupid
window in the back ground. The problem is that tkinter needs a root
window to display the message, but we didn't create a root window yet so
tkinter created it for us.

Sometimes it makes sense to display a message dialog without creating
any other windows. For example, our program might need to display an
error message and exit before the main window is created.

In these cases, we can create a root window and hide it with the
withdraw method. It's documented in the
[wm(3tk)](https://www.tcl.tk/man/tcl/TkCmd/wm.htm) manual page; you can
scroll down to it or just press Ctrl+F and type "withdraw".

[include]: # (examples/startup-error.py)
```python
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.withdraw()

messagebox.showerror("Fatal Error", "Something went badly wrong :(") 
```

The root window hides itself so quickly that it's impossible to notice
it at all.

## Custom message dialogs

**TODO**
