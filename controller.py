import pyttsx3 as tts
import re
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
        self.view.definition_button.config(command=self.button_get_definition)
        self.view.sentence_button.config(command=self.button_get_sentence)

    def button_get_word(self):
        self.view.get_button.config(text="Waiting...")
        data = self.model.get_word_json()
        print(data)
        self.model.set_data(data)
        self.view.get_button.config(text="Get word")
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
        
    def button_get_definition(self):
        word = self.model.word
        definition = self.model.word_data[0]["meanings"][0]["definitions"][0]["definition"]
        subs = "[DATAEXPUNGED]"
        censored_definition = re.compile(re.escape(subs), re.IGNORECASE).sub(word, definition)
        self.view.label_win.config(text=f"Definition: {censored_definition}")
        self.engine.say(definition)
        self.engine.runAndWait()
        
    def button_get_sentence(self):
        print(self.model.word_data)
        sentence = self.model.word_data[0]["meanings"][0]["definitions"][0]["example"]
        word = self.model.word
        subs = "[DATAEXPUNGED]"
        censored_sentence = re.compile(re.escape(subs), re.IGNORECASE).sub(word, sentence)
        self.view.label_win.config(text=f"Sentence: {censored_sentence}")
        self.engine.say(sentence)
        self.engine.runAndWait()
        