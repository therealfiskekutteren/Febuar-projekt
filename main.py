import requests as req
import json
from view import View
from model import Model
from connection import Connection
from controller import Controller
import pyttsx3 as tts
#idea for project: Create a spelling bee app that uses the dictionary api to get the word and the phonetics of the word

def main():
    connection = Connection()
    um = Model(connection)
    uv = View()
    uc = Controller(um, uv)
    #uv.set_controller(uc) Ubrugelig
    uv.run()
def test():
    engine = tts.init()
    engine.say("hello world")
    engine.runAndWait()

if __name__ == "__main__":
    main()
    #test()