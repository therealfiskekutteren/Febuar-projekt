import pyttsx3 as tts
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.engine = tts.init()
        self.engine.setProperty('rate', 150)
        self.view.get_button.config(command=self.button_get_word)
        self.view.play_button.config(command=self.button_play_sound)
        self.view.check_button.config(command=self.button_submit_word)
        self.view.reveal_button.config(command=self.button_reveal_word)

    def button_get_word(self):
        data = self.model.get_word_json()
        print(data)
        self.model.set_data(data)
        word = data[0]["word"]
        self.model.set_word(word)
        self.engine.say(word)
        self.engine.runAndWait()
    
    def button_submit_word(self):
        input = self.view.input_bar.get()
        if input == self.model.word:
            self.view.label_win.config(text="Correct")
            self.engine.say("Correct")
            self.engine.runAndWait()
        else:
            self.view.label_win.config(text="Incorrect")
            self.engine.say("Incorrect")
            self.engine.runAndWait()

    def button_play_sound(self):
        self.engine.say(self.model.word)
        self.engine.runAndWait()

    def button_reveal_word(self):
        self.view.label_win.config(text=f"The word was: {self.model.word}")
        self.engine.say(f"The word was: {self.model.word}")
        self.engine.runAndWait()
        