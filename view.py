import tkinter as tk
class View:
    def __init__(self):
        self.root = tk.Tk()

        self.controller = None
      
        
        self.root.geometry("400x400")
        self.root.title("Spelling Bee App")

        self.label = tk.Label(self.root, text="Spelling bee")
        self.label.pack()

        self.play_button = tk.Button(self.root, text="Get word")
        self.play_button.pack()
        
        self.input_bar = tk.Entry(self.root)
        self.input_bar.pack()

        self.reveal_button = tk.Button(self.root, text="Submit word")
        self.reveal_button.pack()


    def set_controller(self, controller):
        self.controller = controller

    def run(self):
        self.root.mainloop()