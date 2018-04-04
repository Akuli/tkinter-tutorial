# Tkinter Tutorial for Beginners

When I was getting started with Python I loved writing Tkinter GUIs. At
first they felt really complicated because the tutorial I was following
wasn't very good. Even the hello world example had a class with
inheritance, and I didn't know what was a class at the time.

This tutorial consists of minimal examples and explains common mistakes.
You don't need to have any experience in GUI programming to read this
tutorial, and you don't even need to know what is a GUI. All you need is
[basic Python
skills](https://github.com/Akuli/python-tutorial/tree/master/basics#basics).

**If you need help**, you're not alone! [Click
here](https://kiwiirc.com/client/chat.freenode.net/##learnpython) to go
to a free Python help chat. If you see Akuli in the user list, that's me.

## Which GUI toolkit?

GUI is short for Graphical User Interface. It means a program that we
can use without a command prompt or a terminal, like a web browser, a
file manager or an editor.

Tkinter is an easy way to write GUIs in Python. Unlike bigger GUI
toolkits like Qt and GTK+, tkinter comes with Python so many Python
users have it already. Tkinter works on Windows, Mac OSX and Linux, so
it's a good choice for writing cross-platform programs. For example, I
have written [Porcupine](https://github.com/Akuli/porcupine) using
tkinter.

Tkinter is not a good choice if you want to write programs mainly for
Linux users. Most Linux distributions don't come with tkinter and
tkinter applications look different than Qt and GTK+ applications on
Linux. On the other hand, many Linux distributions come with
[GTK+](https://python-gtk-3-tutorial.readthedocs.io/en/latest/), so I
recommend using that if you want to write programs for Linux users.

You can also use [PyQt](http://zetcode.com/gui/pyqt5/) if you want to
write cross-platform GUI programs. It doesn't come with Python and
installing it can be difficult, but PyQt programs look good on Windows,
Mac and Linux.

Tkinter is light, but it's also limited in some ways. For example, you
can't write a web browser in tkinter, but it's possible to write web
browsers in GTK+ and PyQt. Simpler things like text editors and music
players can be written in tkinter.

## List of contents

1. [Getting Started](getting-started.md)
2. [Buttons](buttons.md)
3. [Geometry Managers](geometry-managers.md)
4. [Dialogs](dialogs.md)
5. There will be more stuff here later...
6. [Event Loop and Threads](event-loop-stuff.md)
