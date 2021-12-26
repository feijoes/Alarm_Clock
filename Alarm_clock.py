
from pygame import mixer
import datetime
import time
from tkinter import *
from tkcalendar import *
from PIL import ImageTk,Image





class Alarm(Tk):
    def __init__(self):
        super().__init__()
        self.title('Alarm clock')
        self.iconbitmap('images\\clock_ico.ico')
        self.geometry('400x400')
        self.maxsize(width=400,height=400)
        self.name_varH = StringVar()
        self.name_varM = StringVar()
        self.configure(background='white')
        self.create_widgets()
        
        
    def create_widgets(self):
        
        
        def widgests():
            self.cal = Calendar(self,selectmode='day',year=2021,month=12,day=24)
            self.day = Button(self,text='calendar',command=calendar)
            self.hour = Entry(self,textvariable=self.name_varH)
            self.minutes = Entry(self,textvariable=self.name_varM)
            self.submit_button = Button(self, text='Submit', command=self.submit)
            self.output_label = Label(self)
            start = Button(self,text='start',command=alarm)

            # Place of the widgets
            self.output_label.place(y=65,x=1)
            Label(text='Minutes').place(y=350,x=50)
            Label(text='Hour').place(y=330,x=50)
            self.submit_button.place(y=350,x=220)
            self.minutes.place(y=350,x=100)
            self.hour.place(y=330,x=100)
            self.day.place(y=325,x=300)
            start.place(y=200,x=50)
        
        def calendar():
            label1.destroy()
            self.cal.pack(ipady=60,ipadx=100)
            self.day.configure(text='select a date',command=back)
            
        def back():
            global cal
            self.cal.pack_forget()
            image()
            alarm = Label(text=f'Will star at {self.cal.get_date()}',font=('Helvatical bold',8))
            alarm.place(y=50,x=1)
            self.day.configure(text='calendar',command=calendar)
        
        def image():
            global label1
            image1 = Image.open("images\\clock_image.png")
            test = ImageTk.PhotoImage(image1)
            label1 = Label(image=test)
            label1.image = test
            label1.place(x=150, y=40)
        def alarm():
            while True:
                time.sleep(2)
                if self.cal.get_date() == datetime.datetime.today().strftime('%d/%m/%Y'):
                    if time.localtime().tm_hour == int(self.name_varH.get()) and time.localtime().tm_min == int(self.name_varM.get()):
                        mixer.init()
                        mixer.music.load('song.mp3')
                        mixer.music.play()
                else:
                    print('Working')
                    

                    
                    
                   
                    
                    
        image()
        widgests()
        
        
    def submit(self):
        self.output_label.config(text=f'at {self.name_varH.get()}:{self.name_varM.get()}')
        

    








app = Alarm()
app.mainloop()   
    
    















