import tkinter
import tkinter.messagebox

def colours():
    red.pack()

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        #self.main_window.configure(bg='blue')


        self.a_frame = tkinter.Frame(self.main_window)
        self.b_frame = tkinter.Frame(self.main_window)
        self.c_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.a_frame, text = 'Toppings:')

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)


        self.cb1 = tkinter.Checkbutton(self.a_frame, text="Pepperoni", variable = self.cb_var1)
        self.cb1.configure(bg='yellow')

        self.cb2 = tkinter.Checkbutton(self.a_frame, text="Sausage", variable = self.cb_var2)
        self.cb2.configure(bg='yellow')

        self.cb3 = tkinter.Checkbutton(self.a_frame, text="Bacon", variable = self.cb_var3)
        self.cb3.configure(bg='yellow')

        self.cb4 = tkinter.Checkbutton(self.a_frame, text="Canadian Bacon", variable = self.cb_var4)
        self.cb4.configure(bg='yellow')

        self.cb5 = tkinter.Checkbutton(self.a_frame, text="Mushrooms", variable = self.cb_var5)
        self.cb5.configure(bg='yellow')


        self.prompt_label.pack(side='left')
        self.cb1.pack(side = 'left')
        self.cb2.pack(side = 'left')
        self.cb3.pack(side = 'left')
        self.cb4.pack(side = 'left')
        self.cb5.pack(side = 'left')

        
        self.a_frame.pack(side='top')
        self.b_frame.pack(side='top')
        self.c_frame.pack(side='top')

        self.prompt_label = tkinter.Label(self.b_frame, text = 'Crust:')

        self.radio_var = tkinter.IntVar()
        
    
        self.rb1 = tkinter.Radiobutton(self.b_frame, text = 'Hand-Tossed Crust', variable = self.radio_var, value = 5.00)
        self.rb1.configure(bg='yellow')

        self.rb2 = tkinter.Radiobutton(self.b_frame, text = 'Thin Crust', variable = self.radio_var, value = 7.00)
        self.rb2.configure(bg='yellow')

        self.rb3 = tkinter.Radiobutton(self.b_frame, text = 'Cheese Stuffed Crust', variable = self.radio_var, value = 10.00)
        self.rb3.configure(bg='yellow')


        self.rb2.select()

        self.prompt_label.pack(side='left')
        self.rb1.pack(side= 'right')
        self.rb2.pack(side= 'right')
        self.rb3.pack(side= 'right')

        
        self.mybutton = tkinter.Button(self.main_window, text='Calculate',command=self.do_something)
        self.mybutton.configure(bg = 'blue')

        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)
        self.quit_button.configure(bg = 'red')

        self.mybutton.pack(side='left')
        self.quit_button.pack(side='right')

        self.input = tkinter.Entry(self.c_frame,width=10)
    
        self.prompt_label = tkinter.Label(self.c_frame, text = 'Enter Name:')
        self.prompt_label.configure(bg='yellow')

        self.prompt_label.pack(side='left')
        self.input.pack(side='left')


        tkinter.mainloop()

    def do_something(self):
        #total_cost = message1 + message2
        #self.message = ('Order Name: ', self.input, 'Total Cost: ', total_cost)
        message1 = 0
        message2 = self.radio_var.get()
        message3 = self.input.get()

        if self.cb_var1.get() == 1:
            message1+= 1.00
        if self.cb_var2.get() == 1:
            message1+= 1.50
        if self.cb_var3.get() == 1:
            message1+= 1.25
        if self.cb_var4.get() == 1:
            message1+= 1.75
        if self.cb_var5.get() == 1:
            message1+= 2.00
        


        total_cost = message1 + message2
        self.message = ('Order Name: '+ message3 +'\nTotal Cost: $'+ str(total_cost))

        tkinter.messagebox.showinfo("Order Details",self.message)
            
        


my_gui = MyGUI()

print('moving on....')

