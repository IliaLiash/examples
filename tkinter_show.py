import tkinter as tk

class MyGui:
    def __init__(self):
        self.main_window = tk.Tk()
        
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        
        self.value = tk.StringVar()
        self.text_label = tk.Label(self.top_frame, textvariable = self.value)
        self.text_label.pack()
        
        self.info_button = tk.Button(self.bottom_frame, text = 'Показать инфо', command = self.show)
        self.quit_button = tk.Button(self.bottom_frame, text = 'Выход', command = self.main_window.destroy)
        
        self.info_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tk.mainloop()
        
    def show(self):
        text = 'Где эта улица, где этот дом?'
        self.value.set(text)
            
test = MyGui()