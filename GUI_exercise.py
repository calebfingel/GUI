import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        

        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.fourth_frame = tkinter.Frame(self.main_window)
        self.fifth_frame = tkinter.Frame(self.main_window)


        self.prompt_label1 = tkinter.Label(self.first_frame, text = 'Enter the score for test 1:\n')
        self.test_entry1 = tkinter.Entry(self.first_frame,width=10)
        self.prompt_label2 = tkinter.Label(self.second_frame, text = 'Enter the score for test 2:\n')
        self.test_entry2 = tkinter.Entry(self.second_frame,width=10)
        self.prompt_label3 = tkinter.Label(self.third_frame, text = 'Enter the score for test 3:\n')
        self.test_entry3 = tkinter.Entry(self.third_frame,width=10)

        self.descr_label = tkinter.Label(self.fourth_frame, text = "Average:")
        self.avg_var = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.fourth_frame, textvariable=self.avg_var)

        self.descr_label.pack(side='left')
        self.avg_label.pack(side='left')


        self.prompt_label1.pack(side='left')
        self.test_entry1.pack(side='left')
        self.prompt_label2.pack(side='left')
        self.test_entry2.pack(side='left')
        self.prompt_label3.pack(side='left')
        self.test_entry3.pack(side='left')

    

        self.averagebutton = tkinter.Button(self.fifth_frame, text='Average',command=self.convert)

        self.quit_button = tkinter.Button(self.fifth_frame, text = 'Quit', command = self.main_window.destroy)

        self.averagebutton.pack(side='left')
        self.quit_button.pack(side='right')

        self.first_frame.pack(side='top')
        self.second_frame.pack(side='top')
        self.third_frame.pack(side='top')
        self.fourth_frame.pack(side='top')
        self.fifth_frame.pack(side='bottom')


        tkinter.mainloop()



    def convert(self):
        
        test1 = float(self.test_entry1.get())
        test2 = float(self.test_entry1.get())
        test3 = float(self.test_entry1.get())

        average = round((test1 + test2 + test3)/3)

        self.avg_var.set(average)
        


my_gui = MyGUI()

print('moving on....')

