# Getting Started

Tkinter is a wrapper around a GUI toolkit called Tk. It's usually used
through a language called Tcl, but tkinter allows us to use Tcl and Tk
through Python. This means that we can use Tcl's libraries like Tk with
Python without writing any Tcl code.

## Installing tkinter

**If you installed Python yourself you already have tkinter.** If you
are using Linux you probably don't, but you can install tkinter with
your distribution's package manager. For example, you can use this
command on Debian-based distributions, like Ubuntu and Mint:

```
sudo apt install python3-tk
```

## Hello World!

That's enough talking. Let's do the classic Hello World program :)

[include]: # (hello-world.py)
```python
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello World!")
label.pack()
root.mainloop()
```

Run this program like any other program. It should display a tiny window
with the text `Hello World!` in it. I'm way too lazy to take
screenshots, so here's some ASCII art:

```
,------------------.
| tk   | _ | o | X |
|------------------|
|   Hello World!   |
`------------------'
```

There are many things going on in this short code. Let's go through it
line by line.

```python
import tkinter as tk
```

This line is important. Many other tkinter tutorials use
`from tkinter import *` instead, and then they use things like `Label`
instead of `tk.Label`. **Don't use star imports.** It will confuse you
and other people because you aren't sure about where `Label` comes from
if the file is many lines long, but it also confuses many tools that
process code automatically.

You can also just `import tkinter`, and then use `tkinter.Label` instead
of `tk.Label`. Usually tkinter programs use tkinter's classes so much
that it's easier to `import tkinter as tk`.

```python
root = tk.Tk()
```

The root window is the main window of our program. In this case, it's
the only window that our program creates. Tkinter starts Tcl when you
create the root window.

```python
label = tk.Label(root, text="Hello World!")
```

Like most other GUI toolkits, Tk uses **widgets**. A widget is something
that we see on the screen. Our program has two widgets. The root window
is a widget, and this label is a widget. A label is a widget that just
displays text.

Note that most widgets take a **parent widget** as the first argument.
When we do `tk.Label(root)`, the root window becomes the parent so the
label will be displayed in the root window.

```python
label.pack()
```

This adds the label into the root window so we can see it.

```python
root.mainloop()
```

The code before this takes usually just a fraction of a second to run,
but this line of code runs until we close the window. It's usually
something between a few seconds and a few hours.

## Tkinter and the `>>>` prompt

The `>>>` prompt is a great way to experiment with things. You can also
experiment with tkinter on the `>>>` prompt, but unfortunately it
doesn't work that well on all platforms. Everything works great on
Linux, but on Windows the root window is unresponsive when
`root.mainloop()` is not running.

Try the hello world example to the `>>>` prompt, just type it there line
by line. It's really cool to see the widgets appearing on the screen one
by one as you type. If this works on your system, that's great! If not,
you can run `root.update()` regularly to make it display your changes.

## Print issues

If you try to print a tkinter widget, the results can be surprising.

[comment]: # (github screws up with syntax highlighting here)

```
>>> print(label)
.!label
```

Doing the same thing looks roughly like this on Python 3.5 and older:

```python
>>> print(label)
.3071874380
```

Here `.!label` and `.3071874380` were Tcl's variable names. Converting a
widget to a string like `str(widget)` gives us the widget's Tcl variable
name, and print converts everything to strings using `str()`.

```python
>>> label
<tkinter.Label object at 0xb72aa96c>
>>> str(label)
'.3073026412'
>>> print(label)    # same as print(str(label))
.3073026412
```

So if you're trying to print a variable and you get something like
`.!label` or `.3071874380`, it's probably a tkinter widget. You can also
check that with `print(repr(something))`, it does the same thing as
looking at the widget on the `>>>` prompt:

```python
>>> print(repr(label))
<tkinter.Label object at 0xb72aa96c>
```

## Widget options

When we created a label like `label = tk.Label(root, text="Hello World!")`,
we got a label that displayed the text "Hello World!". Here `text` was
an option, and its value was `"Hello World!"`.

We can also change the text after creating the label in a few different
ways:

```python
>>> label['text'] = "New text"        # it behaves like a dict
>>> label.config(text="New text")     # this does the same thing
>>> label.configure(text="New text")  # this does the same thing too
```

The `config` and `configure` methods do the same thing, only their names
are different.

It's also possible to get the text after setting it:

```python
>>> label['text']       # again, it behaves like a dict
'New text'
>>> label.cget('text')  # or you can use a method instead
'New text'
```

There are multiple different ways to do the same things, and you can mix them
however you want. Personally I like to use initialization arguments and
treat the widget as a dict, but you can do whatever you want.

You can also convert the label to a dict to see all of the options and
their values:

```python
>>> dict(label)
{'padx': <pixel object: '1'>, 'pady': <pixel object: '1'>, 'borderwidth': <pixe
l object: '1'>, 'cursor': '', 'state': 'normal', 'image': '', 'bd': <pixel obje
ct: '1'>, 'font': 'TkDefaultFont', 'justify': 'center', 'height': 0, 'highlight
color': '#ffffff', 'wraplength': <pixel object: '0'>, 'activebackground': '#ece
cec', 'foreground': '#ffffff', 'anchor': 'center', 'bitmap': '', 'fg': '#ffffff
', 'compound': 'none', 'textvariable': '', 'underline': -1, 'background': '#3b3
b3e', 'width': 0, 'highlightbackground': '#3b3b3e', 'relief': 'flat', 'bg': '#3
b3b3e', 'text': '', 'highlightthickness': <pixel object: '0'>, 'takefocus': '0'
, 'disabledforeground': '#a3a3a3', 'activeforeground': '#000000'}
```

That's a mess! Let's use
[pprint.pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint):

```python
>>> import pprint
>>> pprint.pprint(dict(label))
{'activebackground': '#ececec',
 'activeforeground': '#000000',
 'anchor': 'center',
 'background': '#3b3b3e',
 ...
```

If you are wondering what an option does you can just try it and see, or
you can read the manual page (see below).

## Manual pages

Tkinter is not documented very well, but there are many good manual
pages about Tk written for Tcl users. Tcl and Python are two different
languages, but Tk's manual pages are easy to apply to tkinter code.
You'll find the manual pages useful later in this tutorial.

This tutorial contains links to the manual pages, like this
[label(3tk)][label(3tk)] link. There's also [a list of the manual
pages](https://www.tcl.tk/man/tcl/TkCmd/contents.htm).

If you are using Linux and you want to read the manual pages on a
terminal, you can also install Tk's manual pages using your package
manager. For example, you can use this command on Debian-based
distributions:

```
sudo apt install tk-doc
```

Then you can read the manual pages like this:

```
man 3tk label
```

## Summary

- Tkinter is an easy way to write cross-platform GUIs.
- Now you should have tkinter installed and you should know how to use
  it on the `>>>` prompt.
- Don't use star imports.
- You can set the values of Tk's options when creating widgets like
  `label = tk.Label(root, text="hello")`, and you can change them later
  using any of these ways:
    ```python
    label['text'] = "new text"
    label.config(text="new text")
    label.configure(text="new text")
    ```
- You can get the current values of options like this:
    ```python
    print(label['text'])
    print(label.cget('text'))
    ```
- If `print(something)` prints something weird, try
  `print(repr(something))`.
- You can view all options and their values like
  `pprint.pprint(dict(some_widget))`. The options are explained in the
  manual pages.

[manpage list]: # (start)
[label(3tk)]: https://www.tcl.tk/man/tcl/TkCmd/label.htm
[manpage list]: # (end)
