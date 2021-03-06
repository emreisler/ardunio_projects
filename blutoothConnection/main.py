from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.bubble import Button
from kivy.uix.togglebutton import ToggleButton
import threading
import urllib.request
import time


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.disDcit = {"dis1" : False, "dis2" : False, "dis3" : False, "dis4" : False, "dis5" : False, "dis6" : False, "dis7" : False, "dis8" : False, "dis9" : False, "dis10" : False}
        self.dis1 = ToggleButton(text="Allergy" )
        self.dis2 = ToggleButton(text="Asthma")
        self.dis3 = ToggleButton(text="Bronchitis")
        self.dis4 = ToggleButton(text="Goiter")
        self.dis5 = ToggleButton(text="Rheumatics")
        self.dis6 = ToggleButton(text="Sinusitis")
        self.dis7 = ToggleButton(text="Pneumonia")
        self.dis8 = ToggleButton(text="Tension")
        self.dis9 = ToggleButton(text="Tubercular")
        self.dis10 = ToggleButton(text="Flu")


        self.add_widget(self.dis1)
        self.add_widget(self.dis2)
        self.add_widget(self.dis3)
        self.add_widget(self.dis4)
        self.add_widget(self.dis5)
        self.add_widget(self.dis6)
        self.add_widget(self.dis7)
        self.add_widget(self.dis8)
        self.add_widget(self.dis9)
        self.add_widget(self.dis10)

        self.dis1.bind(on_press=self.dis1Action)
        self.dis2.bind(on_press=self.dis2Action)
        self.dis3.bind(on_press=self.dis3Action)
        self.dis4.bind(on_press=self.dis4Action)
        self.dis5.bind(on_press=self.dis5Action)
        self.dis6.bind(on_press=self.dis6Action)
        self.dis7.bind(on_press=self.dis7Action)
        self.dis8.bind(on_press=self.dis8Action)
        self.dis9.bind(on_press=self.dis9Action)
        self.dis10.bind(on_press=self.dis10Action)

        #self.startThreading()

    def dis1Action(self,event):
        if self.disDcit["dis1"] == False:
            self.disDcit["dis1"] = True
        else :
            self.disDcit["dis1"] = False

        print("Diss 1  : " , self.disDcit["dis1"])

    def dis2Action(self,event):
        if self.disDcit["dis2"] == False:
            self.disDcit["dis2"] = True
        else :
            self.disDcit["dis2"] = False

        print("Diss 2  : ", self.disDcit["dis2"])

    def dis3Action(self,event):
        if self.disDcit["dis3"] == False:
            self.disDcit["dis3"] = True
        else :
            self.disDcit["dis3"] = False

        print("Diss 3  : ", self.disDcit["dis3"])

    def dis4Action(self,event):
        if self.disDcit["dis4"] == False:
            self.disDcit["dis4"] = True
        else :
            self.disDcit["dis4"] = False

        print("Diss 4  : ", self.disDcit["dis4"])

    def dis5Action(self,event):
        if self.disDcit["dis5"] == False:
            self.disDcit["dis5"] = True
        else :
            self.disDcit["dis5"] = False

        print("Diss 5  : ", self.disDcit["dis5"])

    def dis6Action(self,event):
        if self.disDcit["dis6"] == False:
            self.disDcit["dis6"] = True
        else :
            self.disDcit["dis6"] = False

        print("Diss 6  : ", self.disDcit["dis6"])

    def dis7Action(self,event):
        if self.disDcit["dis7"] == False:
            self.disDcit["dis7"] = True
        else :
            self.disDcit["dis7"] = False

        print("Diss 7  : ", self.disDcit["dis7"])

    def dis8Action(self,event):
        if self.disDcit["dis8"] == False:
            self.disDcit["dis8"] = True
        else :
            self.disDcit["dis8"] = False

        print("Diss 8  : ", self.disDcit["dis8"])

    def dis9Action(self,event):
        if self.disDcit["dis9"] == False:
            self.disDcit["dis9"] = True
        else :
            self.disDcit["dis9"] = False

        print("Diss 9  : ", self.disDcit["dis9"])

    def dis10Action(self,event):
        if self.disDcit["dis10"] == False:
            self.disDcit["dis10"] = True
        else :
            self.disDcit["dis10"] = False

        print("Diss 8  : ", self.disDcit["dis8"])

    def startThreading(self):

        getDataThrad = threading.Thread(target = self.getData)
        getDataThrad.start()

    def getData(self):
        while True:
            x = urllib.request.urlopen('http://mywebapp-299211.appspot.com/')

            print(x.read())
            time.sleep(1)

class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()