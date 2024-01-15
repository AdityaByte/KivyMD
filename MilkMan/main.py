from datetime import date, datetime
from io import DEFAULT_BUFFER_SIZE
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import SlideTransition
from kivy.core.text import LabelBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton
from kivymd.uix.list import IconLeftWidget, IconRightWidget, OneLineIconListItem, OneLineListItem, OneLineRightIconListItem, ThreeLineAvatarIconListItem, ThreeLineRightIconListItem, TwoLineRightIconListItem
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDFloatingBottomButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton,MDFlatButton
from kivymd.uix.picker import MDDatePicker
from datetime import datetime
from kivymd.uix.list import IconLeftWidget, OneLineListItem, ThreeLineIconListItem, ThreeLineListItem, TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine, MDExpansionPanelThreeLine, MDExpansionPanelTwoLine
from kivy.metrics import dp
import re
import webbrowser
import os
from database import DataBase

db = DataBase()

Window.size = (360,600)

KV = '''

ScreenManager:
    id: scrn_manager
    nav_drawer: nav_drawer


    Screen:
        name: 'welcome_scrn'
        FitImage:
            source: 'bg111.jpg'
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '20sp'
            padding: '40dp'
            Widget: 
            MDLabel:
                text: 'Hey Buddy'
                halign: 'center'
                font_style: 'H3'
                font_name: 'KSR'
                theme_text_color: 'Custom'
                text_color: app.theme_cls.primary_color
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {'center_y':.76}
            MDLabel:
                text: "Are You Agree with all the Terms and Conditions of this app we ensure that your privacy is all time protected our team didn't steal your data this is the fully protected app"
                halign: 'center'
                font_style: 'H6'
                font_name: 'KSR'
                theme_text_color: 'Custom'
                text_color: [255/255, 253/255, 136/255, 0.8/1]
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {'center_y':.55}
            MDFillRoundFlatIconButton:
                icon: 'android'
                text: 'Getting Started'
                font_style: 'H6'
                font_name: 'KSR'
                pos_hint: {'center_x':.5}
                on_release: 
                    scrn_manager.current = "data_scrn"
                    scrn_manager.transition.direction = "left"

            Widget:

    Screen:
        name: 'data_scrn'
        user: user
        account_check: account_check
        dis_but1: dis_but1
        FitImage:
            source: 'bg112.png'
        MDLabel:
            text: 'Sign Up'
            halign: 'center'
            font_style: 'H3'
            font_name: 'KSR'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {'center_y':.78}
        MDTextField:
            id: user
            theme_text_color: 'ContrastParentBackground'
            text_color: 0,0,0,1
            hint_text: 'Username'
            mode: 'rectangle'
            size_hint_x: 0.7
            pos_hint: {'center_x':.5 , 'center_y':.6}
            font_name: 'NSB'
        MDFloatingActionButton:
            id: account_check
            icon: 'account'
            pos_hint: {'center_x':.5 , 'center_y':.44}
            on_release: app.check_username()          

        MDFloatingActionButton:
            icon: 'arrow-left'
            pos_hint: {'center_x':.15 , 'center_y':.1}
            on_release: 
                scrn_manager.current = "welcome_scrn"
                scrn_manager.transition.direction = "right"
        MDFloatingActionButton:
            id: dis_but1
            disabled: True
            icon: 'arrow-right'
            pos_hint: {'center_x':.86 , 'center_y':.1}
            on_release: 
                scrn_manager.current = "data2_scrn"
                scrn_manager.transition.direction = "left" 

    Screen:
        name: 'data2_scrn'
        email: email
        account_check2: account_check2
        dis_but2: dis_but2
        FitImage:
            source: 'bg112.png'
        MDLabel:
            text: 'Sign Up'
            halign: 'center'
            font_style: 'H3'
            font_name: 'KSR'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {'center_y':.78}
        MDTextField:
            id: email
            theme_text_color: 'ContrastParentBackground'
            text_color: 0,0,0,1
            hint_text: 'Email'
            mode: 'rectangle'
            size_hint_x: 0.7
            pos_hint: {'center_x':.5 , 'center_y':.6}
            font_name: 'NSB'
        MDFloatingActionButton:
            id: account_check2
            icon: 'account'
            pos_hint: {'center_x':.5 , 'center_y':.44}
            on_release: app.check_email()          

        MDFloatingActionButton:
            icon: 'arrow-left'
            pos_hint: {'center_x':.15 , 'center_y':.1}
            on_release: 
                scrn_manager.current = "data_scrn"
                scrn_manager.transition.direction = "right"
        MDFloatingActionButton:
            id: dis_but2
            disabled: True
            icon: 'arrow-right'
            pos_hint: {'center_x':.86 , 'center_y':.1}
            on_release: 
                app.save_data_using_json()
                scrn_manager.current = "main_scrn"
                scrn_manager.transition.direction = "left"      

    Screen:
        name: "main_scrn"
        changing_text: changing_text
        changing_text2: changing_text2
        FitImage:
            source: 'butterbg.png'
        MDBoxLayout:
            padding: '8dp'
            orientation: 'vertical'
            spacing: '10dp'
            MDIconButton:   
                icon: 'menu-open'
                pos_hint: {'center_y':1}
                on_release:
                    nav_drawer.set_state("toggle")
            Widget:
        MDLabel:
            text: 'Milkman App ,'
            font_style: 'H4'
            font_name: 'KSR'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            halign: 'center'
            pos_hint: {'center_y':.85 , 'center_x':.38}
            size_hint_y: None
            height: self.texture_size[1]
        MDLabel:
            id: changing_text
            text: ''
            font_style: 'H5'
            font_name: 'KSR'
            halign: 'center'
            pos_hint: {'center_y':.78 , 'center_x':.4}
            size_hint_y: None
            height: self.texture_size[1]
        MDIcon:
            icon: 'robot'
            halign: 'center'
            pos_hint: {'center_x':.2 , 'center_y':.63}
            font_size: '75sp'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
        MDLabel:
            text: 'Hey Buddy ,'
            font_style: 'H6'
            font_name: 'KSR'
            halign: 'center'
            pos_hint: {'center_y':.65 , 'center_x':.5}
            size_hint_y: None
            height: self.texture_size[1] 
        MDLabel:
            text: 'I am your assistant , '
            font_style: 'H6'
            font_name: 'KSR'
            halign: 'center'
            pos_hint: {'center_y':.6 , 'center_x':.6}
            size_hint_y: None
            height: self.texture_size[1] 
        MDLabel:
            text: 'Maintain Your Hisab and Kitab with One Click On this app , Wanna to get started with that app'
            font_style: 'H5'
            font_name: 'KSR'
            halign: 'center'
            pos_hint: {'center_y':.43 , 'center_x':.5}
            size_hint_y: None
            height: self.texture_size[1]     
        MDRoundFlatIconButton:
            text: 'Make my Hisab'
            icon: 'book-account'
            font_style: 'H6'
            font_name: 'COR'
            pos_hint: {'center_x':.5 , 'center_y':.26}
            on_release: 
                app.change_date()
                scrn_manager.current = "hisab_scrn"
                scrn_manager.transition.direction = "left"
        MDLabel:
            text: 'Fully make in india'
            font_style: 'H6'
            font_name: 'KSR'
            halign: 'center'
            pos_hint: {'center_y':.14 , 'center_x':.5}
            size_hint_y: None
            height: self.texture_size[1]   
        MDLabel:
            text: 'Proud to be an indian'
            font_style: 'H6'
            font_name: 'KSR'
            halign: 'center'
            pos_hint: {'center_y':.09 , 'center_x':.5}
            size_hint_y: None
            height: self.texture_size[1]                


        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
                orientation: 'vertical'
                MDIconButton:
                    icon: 'arrow-left'
                    pos_hint: {'center_x':.9}
                    on_release: nav_drawer.set_state('close')
                Image:
                    source: 'cow.png'
                    size_hint_y: 1
                    size_hint_x: 1
                MDExpansionPanelTwoLine:
                    id: changing_text2
                    text: '[font=CarterOne-Regular.ttf]Aditya Pawar[/font]'
                    secondary_text: '[font=CarterOne-Regular.ttf]aditya@gmail.com[/font]'
                    font_name: 'COR'
                    IconLeftWidget:
                        icon: 'account-details'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: '[font=CarterOne-Regular.ttf]Profile[/font]'
                            on_release:
                                scrn_manager.current = "profile"
                                nav_drawer.set_state("close")
                                scrn_manager.transition.direction = "left"
                            IconLeftWidget:
                                icon: 'account'
                        OneLineIconListItem:
                            text: '[font=CarterOne-Regular.ttf]About[/font]'
                            on_release:
                                scrn_manager.current = "about"
                                nav_drawer.set_state("close")
                                scrn_manager.transition.direction = "left"

                            IconLeftWidget:
                                icon: 'information'
                        OneLineIconListItem:
                            text: '[font=CarterOne-Regular.ttf]Settings[/font]'
                            on_release:
                                scrn_manager.current = "settings"
                                nav_drawer.set_state("close")
                                scrn_manager.transition.direction = 'left'
                            IconLeftWidget:
                                icon: 'cog'
                        OneLineIconListItem:
                            text: '[font=CarterOne-Regular.ttf]Your Data[/font]'
                            on_release:
                                scrn_manager.current = "dataviewer_scrn"
                                nav_drawer.set_state("close")
                                scrn_manager.transition.direction = 'left'                                
                            IconLeftWidget:
                                icon: 'book'

                        OneLineIconListItem:
                            text: '[font=CarterOne-Regular.ttf]Exit[/font]'
                            on_release:
                                app.stop()
                            IconLeftWidget:
                                icon: 'location-exit'

    Screen:
        name: 'hisab_scrn'
        container: container
        date: date
        MDIconButton:  
            icon: 'arrow-left'
            pos_hint: {'center_x':.1 , 'center_y':.95}
            on_release: 
                scrn_manager.current = "main_scrn"
                scrn_manager.transition.direction = "right"
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '10sp'
            padding: '20sp'
            MDLabel:
                text: 'Your Hisab'
                font_style: 'H4'
                font_name: 'COR'
                size_hint_y: None
                height: self.texture_size[1]
                halign: 'center'

            MDLabel:
                id: date
                text: ''
                size_hint_y: None
                font_style: 'H6'
                font_name: 'COR'
                height: self.texture_size[1]
                bold: True
                halign: 'center'
            ScrollView:
                MDList:
                    id: container
                    spacing: '15sp'
        MDFloatingActionButton:
            icon: 'plus'
            pos_hint: {'center_x':.86 , 'center_y':.08}
            on_release: app.show_hisab_adder()

    Screen:
        name: 'dataviewer_scrn'
        bxlayout: bxlayout
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_x':.1 , 'center_y':.939}
            on_release: 
                scrn_manager.current = "main_scrn"
                scrn_manager.transition.direction = "right"
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '15dp'
            padding: '20dp'
            MDLabel:
                text: 'Your Data'
                font_style: 'H5'
                font_name: 'COR'
                size_hint_y: None
                height: self.texture_size[1]
                halign: 'center'
            ScrollView:
                MDList:
                    id: bxlayout
                    spacing: '20dp'
                    padding: '10dp'
        MDFloatingActionButton:
            icon: 'information-variant'
            pos_hint: {'center_x':.87 , 'center_y':.069}
            on_release: 
                app.open_info()




    Screen:
        name: 'profile'
        user_changer: user_changer
        email_changer: email_changer
        FitImage:
            source: 'butterbg.png'
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_x':.1 , 'center_y':.95} 
            on_release: 
                scrn_manager.current = "main_scrn" 
                scrn_manager.transition.direction = "right"  
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '25sp'
            MDIcon:
                icon: 'account-circle'
                font_size: '200sp'
                theme_text_color: 'Custom'
                text_color: app.theme_cls.primary_color
                pos_hint: {'center_y':.8}
                halign: 'center' 
                size_hint_y: None
                height: self.texture_size[1]
            MDTextField:
                id: user_changer
                mode: 'fill'
                text: ''
                hint_text: 'Username'
                readonly: True
                size_hint_x: .8
                theme_text_color: 'Custom'
                text_color: [0,0,0,1]
                pos_hint: {'center_x':.5} 
            MDTextField:
                id: email_changer
                mode: 'fill'
                text: ''
                hint_text: 'Email'
                readonly: True
                size_hint_x: .8
                theme_text_color: 'Custom'
                text_color: [0,0,0,1]
                pos_hint: {'center_x':.5} 
            Widget:
    
    Screen:
        name: 'about'
        FitImage:
            source: 'butterbg.png'
        MDBoxLayout:
            orientation: 'vertical'
            padding: '10sp'
            spacing: '5sp'
            MDIconButton:
                icon: 'arrow-left'
                size_hint_y: None
                on_release:
                    scrn_manager.current = "main_scrn"
                    scrn_manager.transition.direction = "right"  

            Image:
                source: 'adit.png'
                pos_hint: {'center_x':.5 , 'center_y':.8}    
                size_hint_x: .5   
                size_hint_y: .5 
            ScrollView:
                MDList:
                    MDLabel:
                        text: 'Developer -> Aditya Pawar ( Cyber_adi ) '
                        font_style: 'H6'
                        font_name: 'COR'
                        halign: 'center'
                        size_hint_y: None
                        height: self.texture_size[1]              
                    MDLabel:
                        text: 'Designer -> Aditya pawar'
                        font_style: 'H6'
                        font_name: 'COR'
                        halign: 'center' 
                        size_hint_y: None
                        height: self.texture_size[1]     
                    MDLabel:
                        text: 'Email id -> cybergeek563@gmail.com'
                        font_style: 'H6'
                        font_name: 'COR'
                        halign: 'center' 
                        size_hint_y: None
                        height: self.texture_size[1]     
                    MDLabel:
                        text: 'Instagram username -> adityapawar4914'
                        font_style: 'H6'
                        font_name: 'COR'
                        halign: 'center' 
                        size_hint_y: None
                        height: self.texture_size[1]     

                    MDLabel:
                        text: 'Github Profile -> github.com/aditya12-cyber'
                        font_style: 'H6'
                        font_name: 'COR'
                        halign: 'center' 
                        size_hint_y: None
                        height: self.texture_size[1]                         
                    MDLabel:
                        text: 'This app is written in python language using the KIVYMD and KIVY module or library'
                        font_style: 'H6'
                        font_name: 'COR'
                        halign: 'center' 
                        size_hint_y: None
                        height: self.texture_size[1]
            MDGridLayout:
                cols: 3
                adaptive_height: True
                adaptive_width: True
                MDIconButton:
                    icon: 'instagram'
                    theme_text_color: 'Custom'
                    text_color: [138/255, 58/255, 185/255, 1]
                    pos_hint: {'center_x':.9 , 'center_y':.05}
                    on_release: app.insta()

                MDIconButton:
                    icon: 'youtube'
                    theme_text_color: 'Custom'
                    text_color: [255/255 , 0 , 0 , 1]
                    pos_hint: {'center_x':.8 , 'center_y':.05}
                    on_release: app.yt()

                MDIconButton:
                    icon: 'github'
                    theme_text_color: 'Custom'
                    text_color: [64/255, 120/255, 192/255, 1]
                    pos_hint: {'center_x':.7 , 'center_y':.05}
                    on_release: app.git()

    Screen:
        name: 'settings'
        MDBoxLayout:
            orientation: 'vertical'
            padding: '10sp'
            spacing: '20sp'
            MDIconButton:
                icon: 'arrow-left'
                size_hint_y: None
                on_release:
                    scrn_manager.current = "main_scrn"
                    scrn_manager.transition.direction = "right"
            Widget:
        MDIcon:
            icon: 'cog'
            font_size: '200sp'
            pos_hint: {'center_y':.8}
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
        MDLabel:
            text: 'Theme Changer'
            font_style: 'H4'
            font_name: 'CarterOne-Regular.ttf'
            pos_hint: {'center_x':.5 , 'center_y':.5}
            halign: 'center'

        MDFloatingActionButton:
            icon: 'apple-icloud'
            pos_hint: {'center_x':.5 , 'center_y':.35}
            elevation_normal: 12
            on_release:
                app.theme()


<DialogContent>:
    name: 'dialog_scrn'
    orientation: 'vertical'
    spacing: '10dp'
    size_hint: 1 , None
    height: '450dp'
    starting_date: starting_date
    ending_date: ending_date
    prsn: prsn
    prce: prce
    litre: litre
    addr: addr
    MDBoxLayout:
        orientation: 'vertical'
        spacing: '10dp'
        MDLabel:
            text: 'Create Hisab'
            font_style: 'H6'
            font_name: 'COR'
            size_hint_y: None
            height: self.texture_size[1]
            halign: 'center'
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '5sp'
            MDTextField:
                id: prsn
                hint_text: "Person name"
                font_name_hint_text: 'COR'
                font_name: 'COR'
                size_hint_x: .95
                helper_text: 'Ex : Aditya Pawar'
                font_name_helper_text: 'COR'
                helper_text_mode: 'on_focus'
                pos_hint: {'center_x':.5}
            MDTextField:
                id: litre
                hint_text: 'How much litre did he want'
                font_name_hint_text: 'COR'
                size_hint_x: .95
                font_name: 'COR'
                helper_text: 'Ex : 2 litre'
                font_name_helper_text: 'COR'
                helper_text_mode: 'on_focus'
                pos_hint: {'center_x':.5}
            MDTextField:
                id: addr
                hint_text: 'Address of the person'
                font_name_hint_text: 'COR'
                size_hint_x: .95
                font_name: 'COR'
                helper_text: 'Ex : Indore'
                font_name_helper_text: 'COR'
                helper_text_mode: 'on_focus'
                pos_hint: {'center_x':.5}
            MDTextField:
                id: prce
                hint_text: 'Price of the milk'
                font_name_hint_text: 'COR'
                size_hint_x: .95
                font_name: 'COR'
                helper_text: 'Ex : 40 Ruppees'
                font_name_helper_text: 'COR'
                helper_text_mode: 'on_focus'
                pos_hint: {'center_x':.5}
            MDGridLayout:
                rows: 1
                MDTextField:
                    id: starting_date
                    hint_text: 'Date when he started'
                    font_name_hint_text: 'COR'
                    size_hint_x: .8
                    font_name: 'COR'
                    helper_text: 'Ex : 01/01/2022'
                    font_name_helper_text: 'COR'
                    helper_text_mode: 'on_focus'
                    pos_hint: {'center_x':.5}
                MDIconButton:
                    icon: 'calendar'
                    padding: '10dp'
                    on_release: root.show_date_picker()
            MDGridLayout:
                rows: 1
                MDTextField:
                    id: ending_date
                    hint_text: 'Date when he ends'
                    font_name_hint_text: 'COR'
                    size_hint_x: .8
                    font_name: 'COR'
                    helper_text: 'Ex : 12/12/2022'
                    font_name_helper_text: 'COR'
                    helper_text_mode: 'on_focus'
                    pos_hint: {'center_x':.5}
                MDIconButton:
                    icon: 'calendar'
                    padding: '10dp'
                    on_release: root.show_date_picker2()
            MDGridLayout:
                rows: 1
                MDRaisedButton:
                    text: 'Save'
                    font_name: 'COR'
                    font_style: 'Button'
                    on_release: (app.add_hisab(prsn,litre,addr,prce,starting_date,ending_date))
                MDFlatButton:
                    text: 'Cancel'
                    font_style: 'Button'
                    font_name: 'COR'
                    on_release: app.close_dialog()

'''

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Expansionpanelwithcheckbox(MDExpansionPanel):

    def __init__(self, pk=None , **kwargs):
        super().__init__(**kwargs)
        self.pk = pk
    
    def mark(self , check , the_list_item):
        if check.active == True:
            the_list_item.text = '[s]'+the_list_item.text+'[/s]'
        else:
            pass
    
    def delete_item(self , the_list_item):
        self.parent.remove_widget(the_list_item)
    
class LeftCheckBox(ILeftBodyTouch , MDCheckbox):

    pass

class DialogContent(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def show_date_picker(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        """This functions gets the date from the date picker and converts its it a
        more friendly form then changes the date label on the dialog to that"""

        date = value.strftime('%A %d %B %Y')
        self.ids.starting_date.text = str(date)

    def show_date_picker2(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save2)
        date_dialog.open()

    def on_save2(self, instance, value, date_range):
        """This functions gets the date from the date picker and converts its it a
        more friendly form then changes the date label on the dialog to that"""

        date = value.strftime('%A %d %B %Y')
        self.ids.ending_date.text = str(date)

class Content(ThreeLineAvatarIconListItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ThreeLineIconWidget(ThreeLineRightIconListItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        icon = IconRightWidget(icon = "arrow-right")

class Main(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):

        return Builder.load_string(KV)


    def open_info(self):
        print("working")

        tasks  = db.get_tasks()
        self.dialog =  None
        for task in tasks:
            if not self.dialog:
                self.dialog = MDDialog(
                    title = f"[font=CarterOne-Regular.ttf]{task[1]} \n {task[2]} \n {task[3]} \n {task[4]} \n {task[5]} \n {task[6]}[/font]",
                ).open()
        

    def on_stop(self):

        print("stopped")

    def on_start(self):
        
        try:
            tasks = db.get_tasks()
            if tasks != []:
                for task in tasks:
                    add_task = (Expansionpanelwithcheckbox(icon = 'android' ,content = Content(text = f"[font=CarterOne-Regular.ttf]{task[4]}[/font]" , secondary_text = f"[font=CarterOne-Regular.ttf]{task[5]}[/font]" , tertiary_text = f"[font=CarterOne-Regular.ttf]{task[6]}[/font]" ) , panel_cls = MDExpansionPanelThreeLine(text = f"[font=CarterOne-Regular.ttf]{task[1]}[/font]" , secondary_text = f"[font=CarterOne-Regular.ttf]{task[2]}[/font]") , tertiary_text = f"[font=CarterOne-Regular.ttf]{task[3]}[/font]"))
                    self.root.ids.container.add_widget(add_task)
        except Exception as e:
            print(e)
            pass


    def change_date(self):
        
        self.root.ids.date.text = str(datetime.now().strftime('%A %d %B %Y'))

    def theme(self):

        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def show_hisab_adder(self):
        self.hisab_list_dialog = None

        if not self.hisab_list_dialog:
            self.hisab_list_dialog = MDDialog(
                # title = "Create Hisab",
                type = "custom",
                content_cls = DialogContent()
            )

        self.hisab_list_dialog.open()
    
    def close_dialog(self , *args):
        self.hisab_list_dialog.dismiss()

    def add_hisab(self , prsn , litre , addr , prce , starting_date , ending_date):
        print('working')
        print(prsn.text)
        print(litre.text)
        print(addr.text)
        print(prce.text)
        print(starting_date.text)
        print(ending_date.text)

        if prsn.text.split() != [] and litre.text.split() != [] and addr.text.split() != [] and prce.text.split() != [] and starting_date.text.split() != [] and ending_date.text.split() != [] :
            

            created_task = db.create_task(prsn.text , litre.text , addr.text , prce.text , starting_date.text , ending_date.text)
            
            con = Content(text = f"[font=CarterOne-Regular.ttf]{created_task[4]}[/font]" , secondary_text = f"[font=CarterOne-Regular.ttf]{created_task[5]}[/font]" , tertiary_text = f"[font=CarterOne-Regular.ttf]{created_task[6]}[/font]" )
            liw = IconLeftWidget(icon = "android")
            con.add_widget(liw)

            self.root.ids.container.add_widget(Expansionpanelwithcheckbox(icon = 'cow.png' ,content = con , panel_cls = MDExpansionPanelTwoLine(text = str(f"[font=CarterOne-Regular.ttf]{created_task[1]}[/font]") , secondary_text = str(f"[font=CarterOne-Regular.ttf]{created_task[2]}[/font]") , tertiary_text = str(f"[font=CarterOne-Regular.ttf]{created_task[3]}[/font]"))))
            expansionpanel = (Expansionpanelwithcheckbox(icon = 'cow.png' ,content = con , panel_cls = MDExpansionPanelTwoLine(text = str(f"[font=CarterOne-Regular.ttf]{created_task[1]}[/font]") , secondary_text = str(f"[font=CarterOne-Regular.ttf]{created_task[2]}[/font]") , tertiary_text = str(f"[font=CarterOne-Regular.ttf]{created_task[3]}[/font]"))))
            self.root.ids.bxlayout.add_widget(expansionpanel)
            self.close_dialog()

            prsn.text = ''
            litre.text = ''
            addr.text = ''
            prce.text = ''
            starting_date.text = ''
            ending_date.text = ''

        else:
            Snackbar(text = f"[font=CarterOne-Regular.ttf]empty data occurs[/font]").open()


        
    def show_data_in_dialog(self, data):
        self.data = None
        self.data = MDDialog(
            title = "Data",
            text = f"Person Name => {self.prsn} \n Milk he want => {self.litre} \n Address of Person => {self.addrr} \n Price of Milk => {self.prce} \n Data when he started => {self.dte}"
        )

    def change_scrn(self):
        self.root.current = "main_scrn"
        self.root.transition.direction = "right"

    def check_username(self):

        self.USER = self.root.ids.user.text

        username_check_false = False
        self.dialog = None

        try:
            int(self.USER)
        except:
            username_check_false = False

        if username_check_false or self.USER.split() == []:
            
            self.dialog_user = None
            if not self.dialog_user:
                self.dialog_user = MDDialog(
                    title = "Invalid Username",
                    text = "Please Enter a Valid Username",
                    buttons=[
                        MDFlatButton(
                            text="RETRY",
                            on_release = self.close_dialog_of_user ,
                        ),
                    ]
                )
            self.dialog_user.open()
            
        elif len(self.USER) <= 4 or len(self.USER) >= 15:

            self.dialog_user_len = None
            if not self.dialog_user_len:
                self.dialog_user_len = MDDialog(
                    title = "Invalid Username",
                    text = "Please Enter a Valid Username which is greater than 4 characters and less than 15 characters",
                    buttons=[
                        MDFlatButton(
                            text="RETRY",
                            on_release = self.close_dialog_of_user_len ,
                        ),
                    ]
                )
            self.dialog_user_len.open()
            
            
            
        else:
            self.root.ids.user.readonly = True
            self.root.ids.dis_but1.disabled = False
            self.root.ids.account_check.icon = "account-check"

    def close_dialog_of_user(self , *kwargs):
        self.dialog_user.dismiss()

    def close_dialog_of_user_len(self , *kwargs):
        self.dialog_user_len.dismiss()

    def check_email(self):

        self.EMAIL = self.root.ids.email.text

        email_check_false = False
        self.dialog = None

        try:
            int(self.USER)
        except:
            email_check_false = False

        if re.fullmatch(regex , self.EMAIL):

            self.root.ids.email.readonly = True
            self.root.ids.dis_but2.disabled = False
            self.root.ids.account_check2.icon = "account-check"
        
        else:
        
            if not self.dialog:
                self.dialog = MDDialog(
                    title = "Invalid Data",
                    text = "Please Enter a Valid Data",
                    buttons=[
                        MDFlatButton(
                            text="RETRY",
                            on_release = self.close_dialog2 ,
                        ),
                    ]
                )
            self.dialog.open()
            
    

    def close_dialog2(self , *kwargs):
        
        self.dialog.dismiss()

    def on_start(self):

        self.store = JsonStore("UserProfileMMApp.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.user_data_changer()
                self.root.current = 'main_scrn'
                
        except KeyError:
            self.root.current = 'welcome_scrn'
                
        try:
            tasks = db.get_tasks()
            if tasks != []:
                for task in tasks:
                    con = Content(text = f"[font=CarterOne-Regular.ttf]{task[4]}[/font]" , secondary_text = f"[font=CarterOne-Regular.ttf]{task[5]}[/font]" , tertiary_text = f"[font=CarterOne-Regular.ttf]{task[6]}[/font]" ) 
                    
                    liw = IconLeftWidget(icon = "android")
                    con.add_widget(liw)
                    add_task = (Expansionpanelwithcheckbox(icon = 'cow.png' ,content = con , panel_cls = MDExpansionPanelThreeLine(text = str(f"[font=CarterOne-Regular.ttf]{task[1]}[/font]") , secondary_text = str(f"[font=CarterOne-Regular.ttf]{task[2]}[/font]") , tertiary_text = str(f"[font=CarterOne-Regular.ttf]{task[3]}[/font]"))))
                    self.root.ids.container.add_widget(add_task)
        except Exception as e:
            print(e)
            pass

        tasks = db.get_tasks()
        if tasks != []:
            for task in tasks:
                con = Content(text = f"[font=CarterOne-Regular.ttf]{task[4]}[/font]" , secondary_text = f"[font=CarterOne-Regular.ttf]{task[5]}[/font]" , tertiary_text = f"[font=CarterOne-Regular.ttf]{task[6]}[/font]" ) 
                
                liw = IconLeftWidget(icon = "android")
                con.add_widget(liw)
                add_task = (Expansionpanelwithcheckbox(icon = 'cow.png' ,content = con , panel_cls = MDExpansionPanelThreeLine(text = str(f"[font=CarterOne-Regular.ttf]{task[1]}[/font]") , secondary_text = str(f"[font=CarterOne-Regular.ttf]{task[2]}[/font]") , tertiary_text = str(f"[font=CarterOne-Regular.ttf]{task[3]}[/font]"))))
                self.root.ids.bxlayout.add_widget(add_task)        

    def save_data_using_json(self):
        self.store.put('UserInfo',name = self.USER , email = self.EMAIL)
        self.user_data_changer()
    
    def user_data_changer(self):
        self.root.ids.changing_text.text = f"Welcome {self.store.get('UserInfo')['name']}"
        self.root.ids.changing_text2.text = f"[font=CarterOne-Regular.ttf]{self.store.get('UserInfo')['name']}[/font]"
        self.root.ids.changing_text2.secondary_text = f"[font=CarterOne-Regular.ttf]{self.store.get('UserInfo')['email']}[/font]"
        self.root.ids.user_changer.text = self.store.get('UserInfo')['name']
        self.root.ids.email_changer.text = self.store.get('UserInfo')['email']

    ############ Profile opening sites

    def insta(self):
        
        webbrowser.open('https://www.instagram.com/adityapawar4914/')
    
    def yt(self):

        webbrowser.open('https://www.youtube.com/channel/UC9kwKHJ2joLyakqi5p08-kw')
    
    def git(self):

        webbrowser.open('https://github.com/aditya12-cyber') 
    



if __name__ == "__main__":
    LabelBase.register(name = "KSR" , fn_regular = "KaushanScript-Regular.ttf")
    LabelBase.register( name = "NSB" , fn_regular = "CarterOne-Regular.ttf")
    LabelBase.register( name = "COR" , fn_regular = "CarterOne-Regular.ttf")

    Main().run()
