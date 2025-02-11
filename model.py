import requests as req
import json

class Model():
    def __init__(self):
        word = None
        word_data = None


    def get_word_json(self):

        while True:
            try:
                response = req.get("https://random-word-api.herokuapp.com/word")
                response = response.json()
                response = req.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+response[0])
                response = response.json()
                if not response[0]["word"]:
                    continue
            except Exception as e:
                print(f"Error: {e}")
            else:
                break

        return response
    
    def set_word(self, word):
        self.word = word
    def set_data(self, data):
        self.word_data = data