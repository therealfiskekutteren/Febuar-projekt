import tkinter as tk
class View:
    def __init__(self):
        self.root = tk.Tk()
        self.controller = None
        self.root.geometry("400x400")
        self.root.title("Spelling Bee App")

        # Container for the frames.
        container = tk.Frame(self.root)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        # Create both LoginPage and SpellingBeePage.
        for F in (LoginPage, SpellingBeePage):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("LoginPage")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def set_controller(self,controller):
        self.controller = controller

    def run(self):
        self.root.mainloop()

# LoginPage only contains the GUI elements for login.
class LoginPage(tk.Frame):
    def __init__(self, parent, view):
        tk.Frame.__init__(self, parent)
        self.view = view
        
        self.label = tk.Label(self, text="Login Page", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(pady=(20,5))
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=(20,5))

        #For secret password
        #self.password_entry = tk.Entry(self, show="*")
        self.password_entry = tk.Entry(self)
        self.password_entry.pack()
        
        self.login_button = tk.Button(self, text="Login")
        self.login_button.pack(pady=20)
        
        self.create_account_button = tk.Button(self, text="Create Account")
        self.create_account_button.pack()

# SpellingBeePage only contains the GUI elements for the spelling bee.
class SpellingBeePage(tk.Frame):
    def __init__(self, parent, view):
        tk.Frame.__init__(self, parent)
        self.view = view
        
        self.label = tk.Label(self, text="Spelling Bee", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.get_button = tk.Button(self, text="Get word")
        self.get_button.pack(pady=5)
        
        self.play_button = tk.Button(self, text="Play sound")
        self.play_button.pack(pady=5)
        
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=5)
        
        self.definition_button = tk.Button(self.button_frame, text="Get definition")
        self.definition_button.pack(side=tk.LEFT, padx=5)
        
        self.sentence_button = tk.Button(self.button_frame, text="Get sentence")
        self.sentence_button.pack(side=tk.RIGHT, padx=5)
        
        self.input_bar = tk.Entry(self)
        self.input_bar.pack(pady=10)
        
        self.label_win = tk.Label(self, text="")
        self.label_win.pack(pady=10)
        
        self.score_label = tk.Label(self, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.check_button = tk.Button(self, text="Submit word")
        self.check_button.pack(pady=5)
        
        self.reveal_button = tk.Button(self, text="Reveal word")
        self.reveal_button.pack(pady=5)