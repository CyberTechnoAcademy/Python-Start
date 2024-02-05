from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        Window.size = (400, 400)
        return Builder.load_file("calc.kv")

calcApp = CalculatorApp()
calcApp.run()