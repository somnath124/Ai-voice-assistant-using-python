from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from threading import Thread
from kivy.uix.scrollview import ScrollView
import os
import sys
import time

from main import run_assistant

Window.clearcolor = (0, 0, 0, 1)
Window.size = (540, 720)

class SunLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=20, padding=40, **kwargs)

        self.animation = Image(source=os.path.join("media", "wave.gif"), anim_delay=0.05, size_hint=(1, 0.8))
        scroll = ScrollView(size_hint=(1, 0.3))
        self.label = Label(text="👋 Hello, I am Sun",font_size='22sp',color=(1, 1, 1, 1),size_hint_y=None,halign='center',valign='top',text_size=(Window.width - 80, None))
        self.label.bind(texture_size=self.label.setter('size'))
        scroll.add_widget(self.label)

       
        self.add_widget(self.animation)
        self.add_widget(scroll)

        Clock.schedule_once(self.start_sequence, 2)

    def update_status(self, text):
        self.label.text = text

    def start_sequence(self, dt):
       
        anim = Animation(opacity=0.5, duration=0.5) + Animation(opacity=1.0, duration=0.5)
        anim.repeat = True
        anim.start(self.animation)

       
        Thread(target=self.run_backend_process).start()

    def run_backend_process(self):
        def frontend_callback(message):
            Clock.schedule_once(lambda dt: self.update_status(message))
        
        run_assistant(callback=frontend_callback)

       
        def finish_task(dt):
            self.update_status("✅ Task Completed")
            time.sleep(1) 
            os._exit(0)  

        Clock.schedule_once(finish_task)



class SunApp(App):
    def build(self):
        return SunLayout()

if __name__ == "__main__":
    SunApp().run()
