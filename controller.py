import pyttsx3 as tts
import re

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.engine = tts.init()
        self.engine.setProperty('rate', 150)
        
        # Connect Spelling Bee Page buttons to Controller methods.
        spelling_page = self.view.frames["SpellingBeePage"]
        spelling_page.get_button.config(command=self.button_get_word)
        spelling_page.play_button.config(command=self.button_play_sound)
        spelling_page.check_button.config(command=self.button_submit_word)
        spelling_page.reveal_button.config(command=self.button_reveal_word)
        spelling_page.definition_button.config(command=self.button_get_definition)
        spelling_page.sentence_button.config(command=self.button_get_sentence)
        
        # Connect Login Page buttons to Controller methods.
        login_page = self.view.frames["LoginPage"]
        login_page.login_button.config(command=self.button_login_user)
        login_page.create_account_button.config(command=self.button_create_user)

    def button_get_word(self):
        spelling_page = self.view.frames["SpellingBeePage"]
        spelling_page.get_button.config(text="Waiting...")
        data = self.model.get_word_json()
        print(data)
        self.model.set_data(data)
        spelling_page.get_button.config(text="Get word")
        word = data[0]["word"]
        self.model.set_word(word)
        self.engine.say(word)
        self.engine.runAndWait()
    
    def button_submit_word(self):
        spelling_page = self.view.frames["SpellingBeePage"]
        submitted = spelling_page.input_bar.get()
        if submitted == self.model.word:
            self.model.add_score(self.user,1)
            self.update_score()
            spelling_page.label_win.config(text="Correct")
            self.engine.say("Correct")
            self.engine.runAndWait()
            self.button_get_word()
        else:
            spelling_page.label_win.config(text="Incorrect")
            self.engine.say("Incorrect")
            self.engine.runAndWait()
            self.button_get_word()

    def button_play_sound(self):
        self.engine.say(self.model.word)
        self.engine.runAndWait()

    def button_reveal_word(self):
        spelling_page = self.view.frames["SpellingBeePage"]
        spelling_page.label_win.config(text=f"The word was: {self.model.word}")
        self.engine.say(f"The word was: {self.model.word}")
        self.engine.runAndWait()
        self.button_get_word()
        
    def button_get_definition(self):
        spelling_page = self.view.frames["SpellingBeePage"]
        word = self.model.word
        try:
            definition = self.model.word_data[0]["meanings"][0]["definitions"][0]["definition"]
            subs = "[DATAEXPUNGED]"
            censored_definition = re.compile(re.escape(subs), re.IGNORECASE).sub(word, definition)
            spelling_page.label_win.config(text=f"Definition: {censored_definition}")
            self.engine.say(definition)
            self.engine.runAndWait()
        except:
            spelling_page.label_win.config(text=f"Definition not found")
        
    def button_get_sentence(self):
        spelling_page = self.view.frames["SpellingBeePage"]
        try:
            sentence = self.model.word_data[0]["meanings"][0]["definitions"][0]["example"]
            word = self.model.word
            subs = "[DATAEXPUNGED]"
            censored_sentence = re.compile(re.escape(subs), re.IGNORECASE).sub(word, sentence)
            spelling_page.label_win.config(text=f"Sentence: {censored_sentence}")
            self.engine.say(sentence)
            self.engine.runAndWait()
        except:
            spelling_page.label_win_config(text=f"Sentence not found")

    def button_create_user(self):
        login_page = self.view.frames["LoginPage"]
        username = login_page.username_entry.get()
        password = login_page.password_entry.get()
        success, message = self.model.create_user(username, password)
        print(message)
        if success:
            self.view.show_frame("SpellingBeePage")
            self.user = username
            self.update_score()
            self.button_get_word()
    
    def button_login_user(self):
        login_page = self.view.frames["LoginPage"]
        username = login_page.username_entry.get()
        password = login_page.password_entry.get()
        success, message = self.model.login_user(username, password)
        print(message)
        if success:
            self.view.show_frame("SpellingBeePage")
            self.user = username
            self.update_score()
            self.button_get_word()
    
    def update_score(self):
        spelling_page = self.view.frames["SpellingBeePage"]
        new_score = self.model.get_score(self.user)
        spelling_page.score_label.config(text="Score: "+str(new_score))