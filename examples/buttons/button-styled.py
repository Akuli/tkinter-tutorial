from tkinter import Tk, Button #importing Tk and button from tkinter
from tkinter import ttk #importing ttk from tkinter that is used to style the tkinter widgets

'''initilaizing tkinter window'''
root=Tk()

'''Adding Normal Button '''
btn1 = Button(root, text = 'Normal Button')
btn1.pack(pady=20) #pady means padding along y axis

'''#Adding Styled Button'''
style=ttk.Style() #importing Style class from Ttk 
style.configure('TButton', font =('@Adobe Kaiti Std R', 10, 'italic', ),foreground="black",background="Green", )#configuring styles in Button

#adding the made style in Button
btn2=ttk.Button(root, text="Styled Button",style ='TButton')
btn2.pack(pady=20)

'''Notice
style option inside styled button comes only with ttk not with the normal Tk button

'''
root.mainloop()