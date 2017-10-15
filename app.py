from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy_garden.NavigationDrawer import NavigationDrawer

class ExampleApp(App):

    def build(self):
        navigationdrawer = NavigationDrawer()

        side_panel = BoxLayout(orientation='vertical')
        button_one = Button(text='Button One')
        button_one.bind(on_press=lambda x: navigationdrawer.toggle_state())
        side_panel.add_widget(button_one)
        navigationdrawer.add_widget(side_panel)

        button = Button(text='=', pos=(0,1000), size_hint=(.1, .1))
        button.bind(on_press=lambda x: navigationdrawer.toggle_state())

        main_panel = AnchorLayout(anchor_x='left', anchor_y='top')
        main_panel.add_widget(button)
        main_panel.add_widget(Label(text='Lend App'))
        navigationdrawer.add_widget(main_panel)

        return navigationdrawer


if __name__ == '__main__':
    ExampleApp().run()