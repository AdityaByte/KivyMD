from kivymd.app import MDApp
from kivymd.uix import *
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.text import LabelBase
import socket
from kivy.core.window import Window

Window.size = (360,600)

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)


KV = '''
<TooltipMDRaisedButton@MDRaisedButton+MDTooltip>

WindowManager:
    Scrn1:
    Scrn2:

<Scrn1>:
    name: 'screen1'
    txtfield1: txtfield1
    txtfield2: txtfield2

    MDScreen:
        MDFloatLayout:
            Image: 
                source: 'clientlogo.gif'
                pos_hint: {'center_x':.5 , 'center_y':.649}
            

            MDLabel:
                text: 'Enter the Client Ip address'
                halign: 'center'
                pos_hint: {'center_y':.430}
                font_name: 'irish'
                font_size: 20
            MDTextField:
                name: txtfield1
                id: txtfield1
                size_hint: None,None
                width: 120
                pos_hint: {'center_x':.5 , 'center_y':.360}
                hint_text: 'IP Address'
                font_name: 'irish'
                text: '127.0.0.1'
                font_size: 15
            MDLabel:
                text: 'Enter the  PORT'
                halign: 'center'
                pos_hint: {'center_y':.280}
                font_name: 'irish'
                font_size: 20
            MDTextField:
                id: txtfield2
                size_hint: None,None
                input_filter: "int"
                text: '4444'
                width: 80
                pos_hint: {'center_x':.5 , 'center_y':.210}
                hint_text: 'PORT'
                input_type: 'number'
                font_name: 'irish'
                font_size: 15
            MDRaisedButton:
                text: 'Connect'
                id: connect
                font_name: 'irish'
                font_size: 17
                pos_hint: {'center_x':.5 , 'center_y':.115}
                    root.connect_to_server()
                    app.root.current = "screen2" if txtfield1.text != "" and txtfield2.text != "" else "screen1"

<Scrn2>:
    name: 'screen2'
    chats: chats
    msg: msg
    send_btn: send_btn
    MDScreen:
        MDFloatLayout:
            MDBoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    id: "toolbar"
                    name: "toolbar"
                    title: 'Client'
                    left_action_items: [['arrow-left-bold-circle' , lambda                on_release:
 x: app.stop()]]
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
                width: 600
                font_size: 20

            MDRaisedButton:
                id: send_btn
                text: 'SEND'
                font_size: 18
                pos_hint: {'center_x':.9}
                spacing: 30
                on_release:
                    root.send_func()

'''
class Scrn1(Screen):

    
    def __init__(self, **kw):
        super().__init__(**kw)

    def connect_to_server(self):
        
        if (self.txtfield1.text != "" and self.txtfield2.text != ""):

            s.connect((self.txtfield1.text , int(self.txtfield2.text)))
            print("connected")



class Scrn2(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)

        
    
    def send_func(self):

        self.Typedmsg = str(self.msg.text)
        print(self.Typedmsg)


        try:
            if (self.Typedmsg != ""):
                self.sending_msg = self.Typedmsg

                s.send(self.sending_msg.encode())

                self.chats.text += "you -> " + self.sending_msg + "\n"
            else:
                print("please enter the message")

        except:
            print("error")


    def recv(self):

        try:
            self.recive_msg = s.recv(1024)
            self.recive_msg = self.recive_msg.decode()

            self.chats.text += "aditya -> " + self.recive_msg + "\n"

        except:
            print("error")
        

class WindowManager(ScreenManager):
    pass


class Client(MDApp):

    def build(self):

        kv = Builder.load_string(KV)

        return kv
        
        

if __name__ == "__main__":
    LabelBase.register(name = "irish" , fn_regular = "irish.ttf")
    Client().run()
