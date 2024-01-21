import os
import cv2
import numpy as np
import uuid
from kivy.graphics.texture import Texture
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.imagelist import MDSmartTile
# from kivymd.uix.gridlayout import MDGridLayout
# from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from matplotlib import pyplot as plt

screen_helper = """

ScreenManager:
    MenuScreen:
    AnggrekScreen:
    BungaScreen:
    DaunJerukScreen:
    DaunAScreen:
    DaunBScreen:

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1

        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 1
            height: dp(200)  # Atur ketinggian background sesuai kebutuhan

            canvas.before:
                Color:
                    rgba: 0.2, 0.2, 0.2, 1  # Warna background
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text: 'Gallery'
                font_size: '36sp'
                font_name: 'Roboto'
                bold: True
                color: 1, 1, 1, 1  # Warna teks title
                size_hint: None, None
                # size: self.texture_size
                pos_hint: {'center_x':0.5,'center_y':0.6}

    MDRectangleFlatButton:
        text: 'Anggrek'
        on_press: root.manager.current = 'anggrek'
        pos_hint: {'center_x':0.5,'center_y':0.6}
    MDRectangleFlatButton:
        text: 'Bunga'
        on_press: root.manager.current = 'bunga'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    MDRectangleFlatButton:
        text: 'Daun Jeruk'
        on_press: root.manager.current = 'daun_jeruk'
        pos_hint: {'center_x':0.5,'center_y':0.4}
    MDRectangleFlatButton:
        text: 'Daun 1'
        on_press: root.manager.current = 'daun_a'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDRectangleFlatButton:
        text: 'Daun 2'
        on_press: root.manager.current = 'daun_b'
        pos_hint: {'center_x':0.5,'center_y':0.2}

<AnggrekScreen>:
    name: 'anggrek'
    MDBoxLayout:
        orientation: 'vertical'
        # size_hint_y: None
        # height: dp(300)  # Set the desired height
        MDScrollView

            MDGridLayout:
                cols: 3
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(1).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)
                    
                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)
                
                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(18).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(19).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(20).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(21).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(22).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(23).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(24).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(25).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(26).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(27).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(28).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(29).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(30).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: root.manager.current = 'menu'
    
<BungaScreen>:
    name: 'bunga'
    MDBoxLayout:
        orientation: 'vertical'
        MDScrollView

            MDGridLayout:
                cols: 3
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(1).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(18).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(19).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(20).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(21).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(22).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(23).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(24).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(25).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(26).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(27).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(28).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(29).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(30).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(31).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(32).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(33).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(34).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(35).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(36).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(37).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(38).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: root.manager.current = 'menu'

<DaunJerukScreen>:
    name: 'daun_jeruk'
    MDBoxLayout:
        orientation: 'vertical'
        MDScrollView

            MDGridLayout:
                cols: 3
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(1).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(18).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(19).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(20).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(21).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(22).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(23).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(24).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(25).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(26).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(27).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(28).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(29).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(30).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(31).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(32).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(33).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(34).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: root.manager.current = 'menu'

<DaunAScreen>:
    name: 'daun_a'
    MDBoxLayout:
        orientation: 'vertical'
        MDScrollView

            MDGridLayout:
                cols: 3
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(1).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(18).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(19).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(20).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(21).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(22).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(23).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(24).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(25).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(26).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(27).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(28).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(29).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(30).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(31).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(32).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(33).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(34).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(35).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(36).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(37).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_(38).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun A'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: root.manager.current = 'menu'

<DaunBScreen>:
    name: 'daun_b'
    MDBoxLayout:
        orientation: 'vertical'
        MDScrollView

            MDGridLayout:
                cols: 3
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(1).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(18).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(19).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(20).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(21).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(22).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(23).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(24).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(25).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(26).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(27).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(28).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(29).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(30).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: root.show_popup(self.source)

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: root.manager.current = 'menu'

"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass

class AnggrekScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/Anggrek"
        return os.path.join(base_path, filename)
    
    def show_popup(self, image_source):
        dialog = MDDialog(
            title="Anggrek",
            type="custom",
            content_cls=ImagePopupContent(image_source, size_hint=(None, None), size=("500dp", "450dp")),
            buttons=[
                MDRaisedButton(
                    text="Close1",
                    on_release=lambda *args: dialog.dismiss(),
                    pos_hint={'center_x': 0.9, 'center_y': 0.5}
                )
            ],
        )
        dialog.open()

class BungaScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/Bunga"
        return os.path.join(base_path, filename)
    
    def show_popup(self, image_source):
        dialog = MDDialog(
            title="Bunga",
            type="custom",
            content_cls=ImagePopupContent(image_source, size_hint=(None, None), size=("500dp", "450dp")),
            buttons=[
                MDRaisedButton(
                    text="Close1",
                    on_release=lambda *args: dialog.dismiss(),
                    pos_hint={'center_x': 0.9, 'center_y': 0.5}
                )
            ],
        )
        dialog.open()

class DaunJerukScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/DaunJeruk"
        return os.path.join(base_path, filename)

    def show_popup(self, image_source):
        dialog = MDDialog(
            title="Daun Jeruk",
            type="custom",
            content_cls=ImagePopupContent(image_source, size_hint=(None, None), size=("500dp", "450dp")),
            buttons=[
                MDRaisedButton(
                    text="Close1",
                    on_release=lambda *args: dialog.dismiss(),
                    pos_hint={'center_x': 0.9, 'center_y': 0.5}
                )
            ],
        )
        dialog.open()

class DaunAScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/Daun"
        return os.path.join(base_path, filename)
    
    def show_popup(self, image_source):
        dialog = MDDialog(
            title="Daun A",
            type="custom",
            content_cls=ImagePopupContent(image_source, size_hint=(None, None), size=("500dp", "450dp")),
            buttons=[
                MDRaisedButton(
                    text="Close1",
                    on_release=lambda *args: dialog.dismiss(),
                    pos_hint={'center_x': 0.9, 'center_y': 0.5}
                )
            ],
        )
        dialog.open()

class DaunBScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/Daun_"
        return os.path.join(base_path, filename)
    
    def show_popup(self, image_source):
        dialog = MDDialog(
            title="Daun B",
            type="custom",
            content_cls=ImagePopupContent(image_source, size_hint=(None, None), size=("500dp", "450dp")),
            buttons=[
                MDRaisedButton(
                    text="Close1",
                    on_release=lambda *args: dialog.dismiss(),
                    pos_hint={'center_x': 0.9, 'center_y': 0.5}
                )
            ],
        )
        dialog.open()

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AnggrekScreen(name='anggrek'))
sm.add_widget(BungaScreen(name='bunga'))
sm.add_widget(DaunJerukScreen(name='daun_jeruk'))
sm.add_widget(DaunAScreen(name='daun_a'))
sm.add_widget(DaunBScreen(name='daun_b'))


class ImagePopupContent(MDBoxLayout):
    def __init__(self, smart_tile, **kwargs):
        super(ImagePopupContent, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.smart_tile = smart_tile
        self.blurred_image_widget = Image()

        box_layout = MDBoxLayout();
        
        box_layout.spacing = "10dp"

        box_layout.add_widget(MDSmartTile(source=self.smart_tile, pos_hint={'center_x': 0.5, 'center_y': 0.8}, size_hint=(1, None), height="200dp"))
        # box_layout.add_widget(MDSmartTile(source=self.smart_tile, pos_hint={'center_x': 0.5, 'center_y': 0.8}, size_hint=(1, None), height="200dp"))
        self.blurred_image_widget.size_hint_y = None
        self.blurred_image_widget.height = "200dp"  # Ganti dengan tinggi yang diinginkan
        box_layout.add_widget(MDSmartTile(self.blurred_image_widget))

        self.add_widget(box_layout)


        # Tambahkan tombol-tombol
        buttons_box = MDBoxLayout(orientation="horizontal", spacing=10, size_hint_y=None)

        blurring_button = MDRaisedButton(text="Blurring", on_release=self.on_blurring_button)
        button2 = MDRaisedButton(text="Edge Detection", on_release=self.on_button2_click)
        button3 = MDRaisedButton(text="Button 3", on_release=self.on_button3_click)

        buttons_box.add_widget(blurring_button)
        buttons_box.add_widget(button2)
        buttons_box.add_widget(button3)

        self.add_widget(buttons_box)

    def on_blurring_button(self, *args):
        if self.smart_tile:
             # Mendapatkan sumber gambar dari objek MDSmartTile
            image_source = self.smart_tile

            # Memuat gambar menggunakan OpenCV
            image_np = cv2.imread(image_source)

            image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

            blurred_image = cv2.GaussianBlur(image_gray, (15, 15), 0)

            # Konversi gambar kembali ke format Kivy
            h, w = blurred_image.shape[:2]
            buf = blurred_image.tobytes()
            texture = Texture.create(size=(w, h), colorfmt='luminance')
            texture.blit_buffer(buf , colorfmt='luminance', bufferfmt='ubyte')

            # Perbarui gambar pada widget Image
            self.blurred_image_widget.texture = texture
            # self.blurred_image_widget.size = (w, h)  # Atur ukuran widget Image

            print("Blurring Clicked!")

    def on_button2_click(self, *args):
        print("Button 2 clicked!")

    def on_button3_click(self, *args):
        print("Button 3 clicked!")

class MainApp(MDApp):

    def build(self):
        self.screen = Builder.load_string(screen_helper)
        return self.screen

MainApp().run()
