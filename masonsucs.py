import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')


        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text = 'Ty sucks?')
        

        self.label1.pack(side='top')


        self.mybutton = tkinter.Button(self.main_window, text='Yes',command=self.do_something)

        self.quit_button = tkinter.Button(self.main_window, text = 'No', command = self.main_window.destroy)

        self.mybutton.pack(side='bottom')
        self.quit_button.pack(side='bottom')

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')


        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response','Youre right!!!')


my_gui = MyGUI()

print('moving on....')
