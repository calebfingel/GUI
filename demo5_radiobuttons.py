import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')


        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        
       

        self.rb1 = tkinter.Radiobutton(self.top_frame, text = 'option1', variable = self.radio_var, value = 10)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = 'option2', variable = self.radio_var, value = 20)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = 'option3', variable = self.radio_var, value = 30)

        self.rb2.select()

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()


        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

        self.okbutton = tkinter.Button(self.bottom_frame, text='OK',command=self.show_choice)
        self.resetbutton = tkinter.Button(self.bottom_frame, text='Reset', command = self.rb1.select)
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.okbutton.pack(side='left')
        self.resetbutton.pack(side='left')
        self.quit_button.pack(side='left')

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", 'You have selected option' + str(self.radio_var.get()))


my_gui = MyGUI()

print('moving on....')

