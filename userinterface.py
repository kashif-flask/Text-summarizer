import kivy
import kivymd
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.properties import StringProperty,ListProperty,ObjectProperty,NumericProperty
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton,MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.progressbar import MDProgressBar
import project

import os


def totxt(path):
    ss=project.convert_pdf_to_txt(path)
    return ss
def summmarize(text):
    ob1,ob2,ob3,ob4=project.summarize_pdf(text)
    return ob1,ob2,ob3,ob4
def model(ob1,ob2,ob3,ob4):
    summ=project.model(ob1,ob2,ob3,ob4)
    return summ

class MainScreen(MDScreen):
    paths=StringProperty("path")
    smm=StringProperty("summary")
    s=StringProperty("summary")
    lengths=NumericProperty(0)
    l1=ListProperty([])
    def assign(self):
        try:
            self.paths=os.path.join(self.ids.filechooser.path,self.ids.filechooser.selection[0])
            
        except:
            pass
    def filter(self,directory,filename):
        if (filename.split('.')[-1]=='pdf'):
            return True
        else:
            return False
    def txt(self,*kwargs):
        self.s=totxt(self.paths)
        
        print(self.lengths)
    def select(self,**kwargs):
        self.l1,self.l2,self.l3,self.l4=summmarize(self.s)
    
    def mo(self,**kwargs):
        
        if not self.l1:
            self.popup("Please Select File First")
        elif not self.lengths:
            self.popup("Please Select length of sentences")

        else:
            
            try:
                
                self.l=model(self.l1,self.l2,self.l3,self.l4)
                
                self.smm="".join(self.l[:int(self.lengths)])
                with open("summary.txt",'w') as f:
                    f.write(self.smm)
                self.manager.get_screen('other').ids['text_input'].text=self.smm
            except:
                self.popup("OOPS! SOMETHING WENT WRONG")
            
    def popup(self,text):
        self.dialog=MDDialog(title="ERROR",text=text,
                             buttons=[MDRectangleFlatButton(text="CANCEL")])
        self.dialog.open()
    
class AnotherScreen(MDScreen):
    tx=ObjectProperty(None)
    
        
    

    
    
    
class ScreenManager(ScreenManager):
    pass

class MainApp(MDApp):
    state=StringProperty("stop")
    def build(self):
        present =Builder.load_file("mains.kv")
        return present
    def on_state(self,instance,value):
        {
            "start":MainScreen().ids.progress.start,
            "stop":MainScreen().ids.progress.stop,
            }.get(value)()
if __name__=="__main__":
    obj=MainApp()
    obj.run()
