import pyttsx3 as tts
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.engine = tts.init()
        self.engine.setProperty('rate', 150)
        self.view.play_button.config(command=self.on_button_click)

    def on_button_click(self):
        data = self.model.get_word_json()
        print(data)
        word = data[0]["word"]
        self.view.label.config(text=word)
        self.engine.say(word)
        self.engine.runAndWait()
        