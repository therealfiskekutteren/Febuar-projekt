import requests as req
import json

class Model():
    def __init__(self):
        word = None
        word_data = None


    def get_word_json(self):

        for _ in range(10):
            try:
                response = req.get("https://random-word-api.herokuapp.com/word",timeout=0.1)
                response = response.json()
                response = req.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+response[0],timeout=0.4)
                response = response.json()
                if response[0]["word"]:
                    return response
            except Exception as e:
                print(f"Error: {e}")
            else:
                break

        raise Exception("Data not found")
    
    def set_word(self, word):
        self.word = word
    def set_data(self, data):
        self.word_data = data