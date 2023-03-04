import plyer
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock

class Notifier(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'

        self.label = Label(text='Hello, world!')
        self.add_widget(self.label)

        self.dismiss_button = Button(text='Dismiss', size_hint=(None, None), size=(200, 50))
        self.dismiss_button.bind(on_press=self.dismiss_notification)
        self.add_widget(self.dismiss_button)

    def show_notification(self, message):
        plyer.notification.notify(title='Notification', message=message)

    def dismiss_notification(self, instance):
        self.label.text = 'Notification dismissed.'
        self.dismiss_button.disabled = True

class NotifierApp(App):
    def build(self):
        notifier = Notifier()
        Clock.schedule_interval(lambda dt: notifier.show_notification('Hello, world!'), 10)
        return notifier

if __name__ == '__main__':
    NotifierApp().run()
