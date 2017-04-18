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
