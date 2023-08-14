import sys
import random
import os

class Model:
    def __init__(self):
        self.tarot_card_image_path = None
        self.user_question = None
        self.executable_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        # Load the image from the executable directory
        self.image_path = os.path.join(self.executable_dir, "Asset/backcard.png")
        self.questions = ["General", "Past Life", "Love Life", "Education", "Career"]
        self.cards = ["The Fool", "The Magician", "The Popess", "The Empress", "The Emperor",
                      "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
                      "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
                      "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgment", "The World"]
        self.question_to_prediction_folder = {
            "General": "G",
            "Past Life": "P",
            "Love Life": "L",
            "Education": "E",
            "Career": "C"
        }
        # card ka nay img , list
        self.card_to_image = [card.lower().replace(" ", "_").replace("the_", "") + ".jpg" for card in self.cards]
        # card ane img match Dictionary
        self.card_and_image = {card.lower().replace(" ", "_").replace("the_", "") + ".jpg": card for card in self.cards}

        self.selected_question = "" # ma thone
        self.selected_card = "" # ma thone

    def get_random_prediction(self): #for test , not ma thone
        random_prediction = random.choice(self.card_to_image)
        return random_prediction

    def get_questions(self):
        return self.questions
    def give_card_image_path(self):
        return self.image_path
    def set_user_question(self,question):
        self.user_question = question

    '''def get_random_card(self):
        self.selected_card = random.choice(self.cards)'''

    def get_folder_name(self, question_name): #ma thone buu
        return self.question_to_prediction_folder.get(question_name)

    # card retrieval
    def give_tarot_card_image_path(self,question): #current
        folder_name = "Cards"
        random_card = random.choice(self.card_to_image)
        executable_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        # Load the image from the executable directory
        random_card_paths = os.path.join(executable_dir, "Cards/"+random_card)
        random_card_path = os.path.join(folder_name,random_card_paths)
        self.tarot_card_image_path = random_card_path
        return self.tarot_card_image_path
    def get_tarot_random_card_name(self,card):
        if card in self.card_and_image:
            card_name = self.card_and_image[card]
            return card_name
        else:
            return None

    def get_tarot_prediction_image_name(self,path):
        return os.path.basename(path)
    def give_tarot_prediction_image_path(self, question,card):
        if question in self.question_to_prediction_folder:
            prediction_folder = self.question_to_prediction_folder[question]
            image_path = f"Predictions/{prediction_folder}/{card}"
            return image_path
        else:
            return None



#pyinstaller --onefile --windowed --name "Tarot Fortune Teller" --icon=Asset/nala.png main.py