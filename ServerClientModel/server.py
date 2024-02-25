from ctypes import addressof
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.text import LabelBase
from kivymd.uix.label import MDLabel
import socket,threading

Window.size = (360,600)

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

KV = '''


<TooltipMDRaisedButton@MDRaisedButton+MDTooltip>

WindowManager:
    Scrn1:
    Scrn2:


<Scrn1>:
    name: 'screen1'
    ip: ip
    port: port

    MDScreen:
        MDFloatLayout:

            Image: 
                source: 'serverlogo.gif'
                pos_hint: {'center_x':.5 , 'center_y':.649}


            MDLabel:
                text: 'Enter the server Ip address'
                halign: 'center'
                pos_hint: {'center_y':.430}
                font_name: 'irish'
                font_size: 20
            MDTextField:
                name: ip
                id: ip
                size_hint: None,None
                width: 120
                pos_hint: {'center_x':.5 , 'center_y':.360}
                hint_text: 'IP Address'
                text: '127.0.0.1'
                font_name: 'irish'
                font_size: 15
            MDLabel:
                text: 'Enter the Server PORT'
                halign: 'center'
                pos_hint: {'center_y':.280}
                font_name: 'irish'
                font_size: 20
            MDTextField:
                id: port
                size_hint: None,None
                input_filter: "int"
                width: 80
                pos_hint: {'center_x':.5 , 'center_y':.210}
                hint_text: 'PORT'
                text: '4444'
                input_type: 'number'
                font_name: 'irish'
                font_size: 15
            MDRaisedButton:
                text: 'Make Server'
                id: connect
                font_name: 'irish'
                font_size: 17
                pos_hint: {'center_x':.5 , 'center_y':.115}
                on_release:
                    root.make_server()
                    app.root.current = "screen2" if ip.text != "" and port.text != "" else "screen1"

<Scrn2>:
    name: 'screen2'
    chat_list: chat_list
    chats: chats
    send_msg: send_msg
    msg: msg


    MDScreen:
        MDFloatLayout:
            MDBoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'Server'
                    left_action_items: [['arrow-left-bold-circle' , lambda x: app.stop()]]

                ScrollView:
                    size_hint_y: .88
                    pos_hint: {"x": 0 , "y": .2}
                    on_scroll_x: False
                    on_scroll_y: True
                    MDBoxLayout:
                        id : chat_list
                        orientation: 'vertical'
                        size: (root.width , root.height)
                        height: self.minimum_height
                        size_hint: None , None
                        pos_hint: {'top': 10}
                        cols: 1
                        spacing: 5
                        MDTextFieldRect:
                            id: chats
                            size: (root.width , root.height)
                            height: self.minimum_height
                            size_hint: None , None
                            pos_hint: {'top': 10}
                            height: 530
                            spacing: 30
                            multiline: True
                            readonly: True
                            disabled: True
        
            TooltipMDRaisedButton:
                text: 'recieve message'
                id: recv_msg_btn
                tooltip_text: 'press the button when you wanna to receive a message'
                pos_hint: {'center_x':.5 , 'center_y':.123}
                on_press: 
                    root.recv()

            MDTextFieldRect:
                id: msg
                hint_text: 'Message'
                size_hint: None,None
                multiline: False
                height: 40
                width: 275
                font_size: 20
                font_name: 'irish'

            MDRaisedButton:
                id: send_msg
                text: 'SEND'
                pos_hint: {'center_x':.9}
                spacing: 30
                font_size: 18
                font_name: 'irish'
                on_press:
                    root.send()
      
'''
class Scrn1(Screen):


    
    def __init__(self, **kw):
        super().__init__(**kw)


    def make_server(self):
        
        if (self.ip.text != "" and self.port.text != ""):
            s.bind((self.ip.text , int(self.port.text)))
            print("listenting")

            s.listen(2)

            global client
            client , addr = s.accept()
            print("connected")




class Scrn2(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)

    
    def send(self):
        
        self.Typedmsg = str(self.msg.text)
        print(self.Typedmsg)

        try:
            if (self.Typedmsg != ""):

                self.sending_msg = self.Typedmsg

                client.send(self.sending_msg.encode())

                self.chats.text += "you -> " + self.sending_msg + "\n"
            
            else:

                print("please enter a message")

        except:
            print("error")



    def recv(self):

        try:
            self.recive_msg = client.recv(1024)
            self.recive_msg = self.recive_msg.decode()

            self.chats.text += "papu -> " + self.recive_msg + "\n"

        except:
            print("error")

    def close(self , obj):
        print("working")

class WindowManager(ScreenManager):
    pass



class Server(MDApp):


    def build(self):

        
        self.kv = Builder.load_string(KV)
        return self.kv

if __name__ == "__main__":
    LabelBase.register(name = "irish" , fn_regular = "irish.ttf")
    Server().run()
