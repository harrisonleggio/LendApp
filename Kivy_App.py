from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ObjectProperty


class Request(Screen):
    pass


class Send(Screen):
    pass



class Manager(ScreenManager):

    request_screen = ObjectProperty(None)
    send_screen = ObjectProperty(None)

class LendAFriend(App):

    def build(self):
        m = Manager(transition=SlideTransition())
        return m


if __name__ == '__main__':
    LendAFriend().run()
