import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty

import qrcode, random
from barcode import EAN13
from barcode.writer import ImageWriter

class MainWindow(Screen):
    pass        

class CardsWindow(Screen):
    mainContainer = ObjectProperty(None)
    shops = []
    existingShops = []
        
    def addCard(self,shop):
        self.shops.append(shop)
        
    def on_enter(self):
        for shop in self.shops:
            if(not(shop in self.existingShops)):
                self.mainContainer.add_widget(shop)
                self.existingShops.append(shop)

        
class AddCardWindow(Screen):
    shopName = ObjectProperty(None)
    expireDate = ObjectProperty(None)
    barcode = ObjectProperty(None)
    quickreadcode = ObjectProperty(None)
    bonus = ObjectProperty(None)
    
    
    def addCard(self):
        
        layout = GridLayout(cols=5)
        layout.add_widget(Label(text = self.shopName.text))
        layout.add_widget(Label(text = self.expireDate.text))
        self.generate_qrcode()
        layout.add_widget(Image(source="./Images/qrcode.png"))
        self.generate_barcode()
        layout.add_widget(Image(source="./Images/barcode.png"))
        CardsWindow.addCard(CardsWindow, layout)
        self.clearData()

    def clearData(self):
        self.shopName.text = ""
        self.expireDate.text = ""
        self.barcode.text = ""
        self.quickreadcode.text = ""
        self.bonus.text = ""
        return
    
    def generate_qrcode(self):
        # Need to add id to image name
        image_id = ''
        self.qrcode_image = qrcode.make(self.quickreadcode.text)
        self.qrcode_image.save("./Images/qrcode" + image_id + ".png")
        
    def generate_barcode(self):
        # Need to add id to image name
        image_id = ''
        self.barcode_image = EAN13(self.barcode.text, writer = ImageWriter())
        self.barcode_image.save("./Images/barcode" + image_id + ".png")
         

class BonusWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("AppScreens.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()

    
