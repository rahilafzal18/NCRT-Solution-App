from kivy.app import App
from kivy.uix.label import Label

class NCRTSolutionApp(App):
    def build(self):
        # Yeh message aapke app ki screen par dikhega
        return Label(text='Developer: Rahil Afzal\nWelcome to NCRT Solution')

if __name__ == '__main__':
    NCRTSolutionApp().run()
