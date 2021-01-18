import tkinter as tk
import tkinter.messagebox

class garage:
    def __init__(self):
        self.main_window = tk.Tk()
        
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        
        self.cb_var1 = tk.IntVar()
        self.cb_var2 = tk.IntVar()
        self.cb_var3 = tk.IntVar()
        self.cb_var4 = tk.IntVar()
        self.cb_var5 = tk.IntVar()
        self.cb_var6 = tk.IntVar()
        self.cb_var7 = tk.IntVar()
        
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        
        self.cb1 = tk.Checkbutton(self.top_frame,
                                  text = 'Oil change - 500',
                                  variable = self.cb_var1)
        self.cb2 = tk.Checkbutton(self.top_frame,
                                  text = 'Other - 300',
                                  variable = self.cb_var2)
        self.cb3 = tk.Checkbutton(self.top_frame,
                                  text = 'Radiator cleaning - 700',
                                  variable = self.cb_var3)
        self.cb4 = tk.Checkbutton(self.top_frame,
                                  text = 'Transmission fluid change - 1000',
                                  variable = self.cb_var4)
        self.cb5 = tk.Checkbutton(self.top_frame,
                                  text = 'Check - 800',
                                  variable = self.cb_var5)
        self.cb6 = tk.Checkbutton(self.top_frame,
                                  text = 'Exhaust replacement - 1300',
                                  variable = self.cb_var6)
        self.cb7 = tk.Checkbutton(self.top_frame,
                                  text = 'Tires replacement - 1300',
                                  variable = self.cb_var7)      
        
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        
        self.price_button = tk.Button(self.bottom_frame,
                                      text = 'Show price',
                                      command = self.get_price)
        
        self.quit_button = tk.Button(self.bottom_frame,
                                     text = 'Exit',
                                     command = self.main_window.destroy)
        
        self.price_button.pack()
        self.quit_button.pack()
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tk.mainloop()
        
    def get_price(self):
        self.total = 0
        
        if self.cb_var1.get() == 1:
            self.total += 500
        if self.cb_var2.get() == 1:
            self.total += 300
        if self.cb_var3.get() == 1:
            self.total += 700
        if self.cb_var4.get() == 1:
            self.total += 1000
        if self.cb_var5.get() == 1:
            self.total += 800
        if self.cb_var6.get() == 1:
            self.total += 1300      
        if self.cb_var7.get() == 1:
            self.total += 1300     
        
        tk.messagebox.showinfo('Total costs =', self.total)    
            
test = MyGui()