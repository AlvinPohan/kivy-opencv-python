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
from kivymd.uix.card import MDCard

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
    
    Image:
        source: 'datasets/Anggrek/anggrek_(1).jpg'  # Ganti dengan nama dan path gambar yang sesuai
        allow_stretch: True
        keep_ratio: False
        color: (1, 1, 1, 0.5)  # Ubah nilai alpha untuk membuat gambar lebih gelap

    MDBoxLayout:
        orientation: 'vertical'

        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: "150dp", "60dp"
            pos_hint: {"center_x": .5, "center_y": .5}
            padding: "3dp"

            MDLabel:
                text: "OPENCV PROJECT"
                font_style: "H5"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]
                halign: "center"
                valign: "middle"

        MDBoxLayout:
            orientation: 'vertical'
            spacing: '10dp'
            padding: '10dp'
            size_hint_y: None
            height: self.minimum_height  # Tinggi dinamis untuk mengakomodasi elemen
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}  # Atur posisi ke tengah bawah layar
            
            MDBoxLayout:
                orientation: 'vertical'
                adaptive_height: True

                MDLabel:
                    text: 'Choose a Media'
                    font_size: '24sp'
                    halign: 'center'
                    theme_text_color: "Secondary"

        MDBoxLayout:
            orientation: 'vertical'
            spacing: '10dp'
            padding: '10dp'
            size_hint_y: None
            height: self.minimum_height  # Tinggi dinamis untuk mengakomodasi elemen
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}  # Atur posisi ke tengah bawah layar

            MDGridLayout:
                cols: 5
                spacing: '45dp'
                padding: '45dp'
                size_hint_y: None
                # size_hint_x: 1
                height: self.minimum_height  # Tinggi dinamis untuk mengakomodasi elemen
                pos_hint: {'center_x': 0.65, 'center_y': 0.5}

                MDFloatingActionButton:
                    on_press: root.manager.current = 'anggrek'
                    md_bg_color: (0.2, 0.6, 0.4, 1)

                    MDLabel:
                        text: "Anggrek"
                        halign: "center"

                MDFloatingActionButton:
                    on_press: root.manager.current = 'bunga'
                    md_bg_color: (0.2, 0.4, 0.8, 1)

                    MDLabel:
                        text: "Bunga"
                        halign: "center"

                MDFloatingActionButton:
                    on_press: root.manager.current = 'daun_jeruk'
                    md_bg_color: (0.8, 0.4, 0.2, 1)

                    MDLabel:
                        text: "Daun Jeruk"
                        halign: "center"

                MDFloatingActionButton:
                    on_press: root.manager.current = 'daun_a'
                    md_bg_color: (0.8, 0.8, 0.2, 1)

                    MDLabel:
                        text: "Daun A"
                        halign: "center"

                MDFloatingActionButton:
                    on_press: root.manager.current = 'daun_b'
                    md_bg_color: (0.4, 0.2, 0.8, 1)

                    MDLabel:
                        text: "Daun B"
                        halign: "center"


<AnggrekScreen>:
    name: 'anggrek'
    MDBoxLayout:
        orientation: 'vertical'
        # size_hint_y: None
        # height: dp(300)  # Set the desired height

        MDRectangleFlatButton:
            text: '<- Back'
            pos_hint: {'center_x':0.1,'center_y':0.1}
            on_press: root.manager.current = 'menu'

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
    
<BungaScreen>:
    name: 'bunga'
    MDBoxLayout:
        orientation: 'vertical'

        MDRectangleFlatButton:
            text: '<- Back'
            pos_hint: {'center_x':0.1,'center_y':0.1}
            on_press: root.manager.current = 'menu'

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

<DaunJerukScreen>:
    name: 'daun_jeruk'
    MDBoxLayout:
        orientation: 'vertical'

        MDRectangleFlatButton:
            text: '<- Back'
            pos_hint: {'center_x':0.1,'center_y':0.1}
            on_press: root.manager.current = 'menu'

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

<DaunAScreen>:
    name: 'daun_a'
    MDBoxLayout:
        orientation: 'vertical'

        MDRectangleFlatButton:
            text: '<- Back'
            pos_hint: {'center_x':0.1,'center_y':0.1}
            on_press: root.manager.current = 'menu'
        
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

<DaunBScreen>:
    name: 'daun_b'
    MDBoxLayout:
        orientation: 'vertical'

        MDRectangleFlatButton:
            text: '<- Back'
            pos_hint: {'center_x':0.1,'center_y':0.1}
            on_press: root.manager.current = 'menu'

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
                    text="Close",
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

        box_layout.add_widget(MDSmartTile(source=self.smart_tile, pos_hint={'center_x': 0.5, 'center_y': 0.6}, size_hint=(5, None), height="300dp"))
        # box_layout.add_widget(MDSmartTile(source=self.smart_tile, pos_hint={'center_x': 0.5, 'center_y': 0.8}, size_hint=(1, None), height="300dp"))

        if self.blurred_image_widget:
            self.blurred_image_widget.size_hint = 5, None
            self.blurred_image_widget.height = "300dp"  # Ganti dengan tinggi yang diinginkan
            self.blurred_image_widget.pos_hint = {'center_x': 0.5, 'center_y': 0.6}
            box_layout.add_widget(self.blurred_image_widget)

        self.add_widget(box_layout)


        # Tambahkan tombol-tombol
        buttons_box = MDBoxLayout(orientation="horizontal", spacing=10, size_hint_y=None)

        blurring_button = MDRaisedButton(text="Blurring", on_release=self.on_blurring_button)
        edge_detection_button = MDRaisedButton(text="Edge Detection", on_release=self.on_edge_detection_button)
        rotation_button = MDRaisedButton(text="Rotation", on_release=self.on_rotation_button)

        buttons_box.add_widget(blurring_button)
        buttons_box.add_widget(edge_detection_button)
        buttons_box.add_widget(rotation_button)

        self.add_widget(buttons_box)

    def on_blurring_button(self, *args):
        if self.smart_tile:
             # Mendapatkan sumber gambar dari objek MDSmartTile
            image_source = self.smart_tile

            # Memuat gambar menggunakan OpenCV
            image_np = cv2.imread(image_source)

            image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

            blurred_image = cv2.blur(image_np, (20, 20))

            rotated_image = cv2.rotate(blurred_image, cv2.ROTATE_180)
            flipped_image = cv2.flip(rotated_image, flipCode=1)

            # Konversi gambar kembali ke format Kivy
            h, w = flipped_image.shape[:2]
            buf = flipped_image.tobytes()
            texture = Texture.create(size=(w, h))
            texture.blit_buffer(buf, bufferfmt='ubyte')

            # Perbarui gambar pada widget Image
            self.blurred_image_widget.texture = texture
            # self.blurred_image_widget.size = (w, h)  # Atur ukuran widget Image

            print("Blurring Clicked!")

    def on_edge_detection_button(self, *args):
        if self.smart_tile:
             # Mendapatkan sumber gambar dari objek MDSmartTile
            image_source = self.smart_tile

             # Memuat gambar menggunakan OpenCV
            image_np = cv2.imread(image_source)

            image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

            # menghilangkan noise
            img = cv2.GaussianBlur(image_gray, (3,3), 0)

            # konvolusi dengan matriks kernel
            lapacian = cv2.Laplacian(img, cv2.CV_64F)
            sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
            sobely = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)

            plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
            plt.title('Original'),plt.xticks([]), plt.yticks([])
            plt.subplot(2,2,2),plt.imshow(lapacian,cmap='gray')
            plt.title('Laplacian'),plt.xticks([]), plt.yticks([])
            plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
            plt.title('Sobel X'),plt.xticks([]), plt.yticks([])
            plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
            plt.title('Sobel Y'),plt.xticks([]), plt.yticks([])

            plt.show()

            print("Edge Detection Clicked!")

    def on_rotation_button(self, *args):
        if self.smart_tile:

            # Mendapatkan sumber gambar dari objek MDSmartTile
            image_source = self.smart_tile

            # Memuat gambar menggunakan OpenCV
            image_np = cv2.imread(image_source)

            h, w = image_np.shape[:2]

            rotation_matrix = cv2.getRotationMatrix2D((w/2, h/2), -180, 0.5)
            rotation_image = cv2.warpAffine(image_np, rotation_matrix, (w,h))

            plt.imshow(cv2.cvtColor(rotation_image, cv2.COLOR_BGR2RGB))
            plt.title("Rotation")
            plt.show()



            print("Histogram clicked!")

class MainApp(MDApp):

    def build(self):
        self.screen = Builder.load_string(screen_helper)
        return self.screen

MainApp().run()
