from kivymd.uix.tab import MDTabsBase

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons

from kivy.lang import Builder
from kivymd.app import MDApp

from kivy_garden.mapview import MapView

from kivy.core.window import Window

Window.size = (400, 600)


class Test(MDApp):

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

KV = '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "#737270"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Map'
            icon: 'map'

            MDLabel:
                text: 'Map'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Search'
            icon: 'map-search-outline'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Other'
            icon: 'dots-horizontal'

            MDSwiper:

                MDSwiperItem:

                    MDCard:
                        orientation: "vertical"
                        padding: 0, 0, 0 , "36dp"
                        size_hint: .5, .5
                        pos_hint: {"center_x": .5, "center_y": .5}
                        elevation: 4
                        shadow_radius: 6
                        shadow_offset: 0, 2
                
                        MDLabel:
                            text: "Theme style - {}".format(app.theme_cls.theme_style)
                            halign: "center"
                            valign: "center"
                            bold: True
                            font_style: "H5"

                        MDRaisedButton:
                            text: "Set theme"
                            on_release: app.switch_theme_style()
                            pos_hint: {"center_x": .5}

                MDSwiperItem:
                    MDCard:
                        orientation: "vertical"
                        padding: 0, 0, 0 , "36dp"
                        size_hint: .5, .5
                        pos_hint: {"center_x": .5, "center_y": .5}
                        elevation: 4
                        shadow_radius: 6
                        shadow_offset: 0, 2
                
                        MDLabel:
                            text: "Theme style - {}".format(app.theme_cls.theme_style)
                            halign: "center"
                            valign: "center"
                            bold: True
                            font_style: "H5"
                
                        MDRaisedButton:
                            text: "Set theme"
                            on_release: app.switch_theme_style()
                            pos_hint: {"center_x": .5}
'''

Test().run()