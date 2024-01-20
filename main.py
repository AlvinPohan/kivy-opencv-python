import os
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp

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
    MDRectangleFlatButton:
        text: 'Anggrek'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'anggrek'
    MDRectangleFlatButton:
        text: 'Bunga'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'bunga'
    MDRectangleFlatButton:
        text: 'Daun Jeruk'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'daun_jeruk'
    MDRectangleFlatButton:
        text: 'Daun 1'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'daun_a'
    MDRectangleFlatButton:
        text: 'Daun 2'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'daun_b'

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
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)
                    
                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)
                
                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(18).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(19).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(20).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(21).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(22).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(23).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(24).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(25).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(26).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(27).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(28).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(29).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('anggrek_(30).jpg')  # Adjust the path accordingly
                    tile_text: 'Anggrek'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

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
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('bunga_(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Bunga'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

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
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(18).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(19).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(20).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(21).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(22).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(23).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(24).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(25).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(26).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(27).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(28).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(29).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(30).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(31).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(32).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(33).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun_jeruk_(34).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun Jeruk'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

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
                    on_release: lambda instance: self.show_popup(instance.source)

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
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(2).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(3).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(4).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(5).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(6).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(7).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(8).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(9).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(10).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(11).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(12).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(13).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(14).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(15).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(16).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(17).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(18).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(19).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(20).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(21).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(22).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(23).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(24).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(25).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(26).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(27).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(28).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(29).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

                MDSmartTile:
                    size_hint_y: None
                    height: dp(150)  # Set the desired height for the SmartTile
                    source: root.build_image_path('daun__(30).jpg')  # Adjust the path accordingly
                    tile_text: 'Daun B'
                    tile_font_style: 'Subtitle1'
                    on_release: lambda instance: self.show_popup(instance.source)

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
            title="Image Popup",
            type="custom",
            content_cls=ImagePopupContent(image_source),
            buttons=[
                MDRaisedButton(
                    text="Close",
                    on_release=lambda *args: dialog.dismiss()
                )
            ],
        )
        dialog.open()

class ImagePopupContent(MDBoxLayout):
    def __init__(self, image_source, **kwargs):
        super(ImagePopupContent, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(MDSmartTile(source=image_source, size_hint_y=None, height=dp(200)))

class BungaScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/Bunga"
        return os.path.join(base_path, filename)

class DaunJerukScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/DaunJeruk"
        return os.path.join(base_path, filename)

class DaunAScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/Daun"
        return os.path.join(base_path, filename)

class DaunBScreen(Screen):
    def build_image_path(self, filename):
        base_path = "datasets/Daun_"
        return os.path.join(base_path, filename)

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AnggrekScreen(name='anggrek'))
sm.add_widget(BungaScreen(name='bunga'))
sm.add_widget(DaunJerukScreen(name='daun_jeruk'))
sm.add_widget(DaunAScreen(name='daun_a'))
sm.add_widget(DaunBScreen(name='daun_b'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
