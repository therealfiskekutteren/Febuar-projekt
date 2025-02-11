import requests as req
import json

class Model():
    def __init__(self):
        test=None


    def get_word_json(self):
        # gotresponse = False
        # while gotresponse == False:
        #     word = req.get("https://random-word-api.herokuapp.com/word").json()[0]
        #     print("Randomword: "+word)
        #     response = req.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
        #     response = response.json()
        #     try:
        #         response[0]["word"]
        #         if response[0]["phonetics"][0]["audio"] != '':
        #             gotresponse = True
        #     except:
        #         continue
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