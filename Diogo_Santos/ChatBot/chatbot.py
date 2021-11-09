from user import User
import requests,time,random,json

class Chatbot:
    ''' The core of the app chatbot

    Attributes:
        user                The user in app
        manualProcessing    The flag which dictates how the input/output is processed
        stopChat            The flag which dictates the end of chat
        brainshopURL        The URL GET request target for brainshop API
        jokesURL            The URL GET request target for jokes API
    
    This app allows the user to chat with a chatbot named ZenBot.
    The user input can be processed manually or through an API from https://brainshop.ai/

    Note:
    This bot uses an API from https://brainshop.ai/ which requires some sensitive data
    that should be kept in env variables or store somewhere save, not a big deal here 
    since this is a burden account
    '''

    def __init__(self, user: User):
        ''' Creates an instance of the class Chatbot '''
        self.user = user
        self.manualProcessing = False
        self.stopChat = False
        self.brainshopURL = "http://api.brainshop.ai/get?bid=160986&key=4NaYGGa0iuqAcOeR&uid=1&msg="
        self.jokesURL = "https://v2.jokeapi.dev/joke/Any"


    def ZenBot(self) -> None:
        ''' Starts a conversation with Zenbot '''

        userName = self.user.getName()
        self.stopChat = False
        self.__introduction(userName)
        while True:
            userInput = input(f"{userName}: ")
            self.__processInput(userInput, self.manualProcessing)
            if(self.stopChat):
                return


    def __processInput(self, userInput: str, manual: bool) -> None:
        """ Process user input manually or through an external API"""
        if(userInput == "exit"):
            self.stopChat = True
            return
        if(manual):
            self.__manualResponse(userInput)
        else:
            self.__apiResponse(userInput)


    def __manualResponse(self, userInput: str) -> None:
        """ Process response manually """
        with open("ChatBot/botBrain.json","r") as json_file:
            words = userInput.lower().split(" ")
            db = json.load(json_file)
            for intent in db["intents"]:
                for word in words:
                    if(word in ["joke","jokes"]):
                        self.__apiJoke()
                        return
                    if(word in intent["input"]):
                        self.__botSpeak(intent["output"][random.randint(0,len(intent["output"])-1)])
                        return
            self.__botSpeak("I'm not sure how to respond to that :(")


    def __apiResponse(self, userInput: str) -> None:
        """ Process response with external API """

        response = requests.get(self.brainshopURL+userInput).json()
        response = response["cnt"]

        self.__botSpeak(response) 


    def __apiJoke(self) -> None:
        """ Requests joke from external API """
        response = requests.get(self.jokesURL).json()
    
        if(response["error"]):
            self.__botSpeak("Ups, something went wrong")
            return 

        if(response["type"] == "twopart"):
            self.__botSpeak(response["setup"])
            self.__botSpeak(response["delivery"])
        else:
            self.__botSpeak(response["joke"])
        

    def __introduction(self, userName: str) -> None:
        """ Introduces Zenbot to user """
        introductionPhrases = [
            f"Hello {userName}, this is a simple chatbot",
            "He has two modes:"
            "(1) Replies with the assist of an API powered by AI."
            "(2) Replies manually with a small dataset or jokes from an API."
            "Please forgive me if he is too dumb.",
            "Waking him up",
            "...",
            "...",
            "He is ready!"
        ]
        for phrase in introductionPhrases:
            print(phrase)
            time.sleep(0.5)

        self.__botSpeak("Hello! Let's chat")


    def __botSpeak(self, phrase: str) -> None:
        """ Prints Zenbot response """
        print(f"Zen: {phrase}")
        # To simulate typing and thinking
        time.sleep(0.5)