class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
        pass

    def on_exit_button_click(self):
        self.view.root.destroy()

    def get_questions(self):
        return self.model.get_questions()

    def get_card_path(self,index):
        return self.model.give_card_image_path()

    def get_tarot_card_image_path(self,question): # current
        return self.model.give_tarot_card_image_path(question)
    def get_tarot_prediction_image_path(self,question,card):
        return self.model.give_tarot_prediction_image_path(question,card)
    def get_tarot_prediction_image_name(self,path):
        return self.model.get_tarot_prediction_image_name(path)
    def get_tarot_random_card_name(self,card):
        return self.model.get_tarot_random_card_name(card)

    def on_card_click(self,question):
        self.view.show_page_3(question)

    def on_question_button_click(self,question,event=None):
        self.model.set_user_question(question)
        print(question)
        #print(self.model.user_question)
        self.view.show_page_2(question)
    def on_back_button_click(self):
        self.view.show_page()
    def on_back_button_click_3(self,question):
        self.view.show_page_2(question)
    def on_shuffle_button_click(self,question):
        self.view.shuffle_cards(question)

