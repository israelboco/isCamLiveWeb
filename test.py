from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.network.urlrequest import UrlRequest
import socketio

class MainApp(MDApp):
    def build(self):
        self.client_id = None
        self.sio = socketio.Client()
        self.sio.connect('http://localhost:5000')

        self.sio.on('connect', self.on_connect)
        self.sio.on('disconnect', self.on_disconnect)
        self.sio.on('notification', self.on_notification)

        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='CamLive - Client')
        layout.add_widget(self.label)
        self.button = MDRaisedButton(text='Envoyer Image', on_release=self.send_image)
        layout.add_widget(self.button)
        return layout

    def on_connect(self):
        self.client_id = self.sio.sid
        print('Connected to server with client ID:', self.client_id)

    def on_disconnect(self):
        print('Disconnected from server')

    def on_notification(self, data):
        self.dialog = MDDialog(title='Notification', text=data['message'])
        self.dialog.open()

    def send_image(self, instance):
        # Envoyer une image (à adapter selon votre source d'image)
        with open('path/to/your/image.jpg', 'rb') as f:
            image_data = f.read()
        self.sio.emit('image', image_data)

if __name__ == '__main__':
    MainApp().run()
