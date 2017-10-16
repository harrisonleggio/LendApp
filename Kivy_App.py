from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class Request(Screen):
    pass

class Send(Screen):
    amount_input = ObjectProperty()
    receiver_input = ObjectProperty()
    interest_input = ObjectProperty()

    def process_amount(self):
        amount = self.amount_input.text
        receiver = self.receiver_input.text
        interest = self.interest_input.text

        print amount
        print receiver
        print interest

class Manager(ScreenManager):

    request_screen = ObjectProperty(None)
    send_screen = ObjectProperty(None)

class LendAFriend(App):

    def build(self):
        m = Manager(transition=SlideTransition())
        return m


if __name__ == '__main__':
    LendAFriend().run()
