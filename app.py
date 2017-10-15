from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import dp

from kivy_garden.NavigationDrawer import NavigationDrawer

class ExampleApp(App):

    def build(self):
        navigationdrawer = NavigationDrawer()
        side_panel = BoxLayout(orientation='vertical')
        side_panel.add_widget(Button(text='Button One'))
        side_panel.add_widget(Button(text='Button Two'))

        navigationdrawer.add_widget(side_panel)

        button = Button(text='Open nav bar')
        button.bind(on_press=lambda j: navigationdrawer.toggle_state())
        main_panel = BoxLayout(orientation='vertical')
        main_panel.add_widget(button)
        navigationdrawer.add_widget(main_panel)
        return navigationdrawer


if __name__ == '__main__':
    ExampleApp().run()