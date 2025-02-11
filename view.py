import tkinter as tk
class View:
    def __init__(self):
        self.root = tk.Tk()

        self.controller = None
      
        
        self.root.geometry("400x400")
        self.root.title("Spelling Bee App")

        self.label = tk.Label(self.root, text="Spelling bee")
        self.label.pack()

        self.get_button = tk.Button(self.root, text="Get word")
        self.get_button.pack()

        self.play_button = tk.Button(self.root, text="Play sound")
        self.play_button.pack()
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.definition_button = tk.Button(self.button_frame, text="Get definition")
        self.definition_button.pack(side=tk.LEFT)

        self.sentence_button = tk.Button(self.button_frame, text="Get sentence")
        self.sentence_button.pack(side=tk.RIGHT)

        self.input_bar = tk.Entry(self.root)
        self.input_bar.pack()

        self.label_win = tk.Label(self.root, text="")
        self.label_win.pack()

        self.check_button = tk.Button(self.root, text="Submit word")
        self.check_button.pack()

        self.reveal_button = tk.Button(self.root, text="Reveal word")
        self.reveal_button.pack()


    def set_controller(self, controller):
        self.controller = controller

    def run(self):
        self.root.mainloop()