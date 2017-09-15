from Tkinter import *
from tkFont import *
import serial
class buzzer:
    def __init__(self,master):
        self.master=master
        master.title("QUIZ")
        master.configure(background='#EEC9C1')
        self.score=[0,0,0,0];
        self.r=IntVar()
        self.r.set(2)
        self.rounds=[5,10,20,50];
        file=open('buzzer.txt','r')
        txt=file.readlines()
        o=txt[len(txt)-1]
        file.close()
        self.order=['0','0','0','0'];
        self.order[0]=str(o[1])
        self.order[1]=str(o[2])
        self.order[2]=str(o[3])
        self.order[3]=str(o[4])
        self.t=0

        self.frame=Frame(master,background='#EEC9C1')
        self.frame.pack()
        
        self.frame1=Frame(self.frame,background='#EEC9C1')
        self.frame1.pack()
        self.name=Label(self.frame1,text="QUIZ",width=40,height=5,bg='#4BEBD8')
        self.name.grid(row=0,column=0,padx=(10,10),pady=(10,10))

        self.frame2=Frame(self.frame,background='#EEC9C1')
        self.frame2.pack()

        self.team1=Label(self.frame2,text="TEAM A",width=40,height=5,bg='#4BEBD8')
        self.team1.grid(row=0,column=0,padx=(10,10),pady=(10,10))
        self.score1=Label(self.frame2,text=self.score[0],width=15,height=5,bg='#4BEBD8')
        self.score1.grid(row=0,column=1,padx=(10,10),pady=(10,10))

        self.team2=Label(self.frame2,text="TEAM B",width=40,height=5,bg='#4BEBD8')
        self.team2.grid(row=1,column=0,padx=(10,10),pady=(10,10))
        self.score2=Label(self.frame2,text=self.score[1],width=15,height=5,bg='#4BEBD8')
        self.score2.grid(row=1,column=1,padx=(10,10),pady=(10,10))

        self.team3=Label(self.frame2,text="TEAM C",width=40,height=5,bg='#4BEBD8')
        self.team3.grid(row=2,column=0,padx=(10,10),pady=(10,10))
        self.score3=Label(self.frame2,text=self.score[2],width=15,height=5,bg='#4BEBD8')
        self.score3.grid(row=2,column=1,padx=(10,10),pady=(10,10))

        self.team4=Label(self.frame2,text="TEAM D",width=40,height=5,bg='#4BEBD8')
        self.team4.grid(row=3,column=0,padx=(10,10),pady=(10,10))
        self.score4=Label(self.frame2,text=self.score[3],width=15,height=5,bg='#4BEBD8')
        self.score4.grid(row=3,column=1,padx=(10,10),pady=(10,10))
        
        self.frame3=Frame(self.frame,background='#EEC9C1')
        self.frame3.pack()
        self.ans=Label(self.frame3,text="",width=40,height=5,bg='#4BEBD8')
        self.ans.grid(row=0,column=0,padx=(10,10),pady=(10,10))
        

        self.frame4=Frame(self.frame,background='#EEC9C1')
        self.frame4.pack()

        self.round1=Label(self.frame4,text=self.rounds[0],width=15,height=5,bg='green')
        self.round1.grid(row=0,column=0,padx=(10,10),pady=(10,10))

        self.round2=Label(self.frame4,text=self.rounds[1],width=15,height=5,bg='#4BEBD8')
        self.round2.grid(row=0,column=1,padx=(10,10),pady=(10,10))

        self.round3=Label(self.frame4,text=self.rounds[2],width=15,height=5,bg='#4BEBD8')
        self.round3.grid(row=0,column=2,padx=(10,10),pady=(10,10))

        self.round4=Label(self.frame4,text=self.rounds[3],width=15,height=5,bg='#4BEBD8')
        self.round4.grid(row=0,column=3,padx=(10,10),pady=(10,10))

        self.check = Button(self.frame4, text="CHECK")
        self.check.bind('<c>',lambda e: self.change(self.order[self.t]))
        self.check.bind('<Right>',lambda e: self.change_round(self.r.get()))
        self.check.bind('<r>',lambda e: self.answer_c(1))
        self.check.bind('<w>',lambda e: self.answer_c(0))
        self.check.bind('<w>',lambda e: self.answer_c(0))
        self.check.bind('<s>',lambda e: self.send())
        self.check.bind('<z>',lambda e: self.done())
        self.check.focus_set()
        self.check.grid(row=1,column=2,padx=(10,10),pady=(10,10))

        

        

    def change(self,method):
        file=open('buzzer.txt','r')
        txt=file.readlines()
        o=txt[len(txt)-1]
        file.close()
        self.order[0]=str(o[1])
        self.order[1]=str(o[2])
        self.order[2]=str(o[3])
        self.order[3]=str(o[4])
        if method=="1":
            self.team1.config(bg='green')
            self.team2.config(bg='#4BEBD8')
            self.team3.config(bg='#4BEBD8')
            self.team4.config(bg='#4BEBD8')
        if method=="2":
            self.team2.config(bg='green')
            self.team1.config(bg='#4BEBD8')
            self.team3.config(bg='#4BEBD8')
            self.team4.config(bg='#4BEBD8')
        if method=="3":
            self.team3.config(bg='green')
            self.team1.config(bg='#4BEBD8')
            self.team2.config(bg='#4BEBD8')
            self.team4.config(bg='#4BEBD8')
        if method=="4":
            self.team4.config(bg='green')
            self.team1.config(bg='#4BEBD8')
            self.team2.config(bg='#4BEBD8')
            self.team3.config(bg='#4BEBD8')

        
        
    def done(self):
        file=open('buzzer.txt','r')
        txt=file.readlines()
        o=txt[len(txt)-1]
        file.close()
        self.order[0]=str(o[1])
        self.order[1]=str(o[2])
        self.order[2]=str(o[3])
        self.order[3]=str(o[4])
        
    def change_round(self,method):
        if method==1:
            self.round1.config(bg='green')
            self.round4.config(bg='#4BEBD8')
            self.r.set(2)
        elif method==2:
            self.round2.config(bg='green')
            self.round1.config(bg='#4BEBD8')
            self.r.set(3)
        elif method==3:
            self.round3.config(bg='green')
            self.round2.config(bg='#4BEBD8')
            self.r.set(4)
        elif method==4:
            self.round4.config(bg='green')
            self.round3.config(bg='#4BEBD8')
            self.r.set(1)

    def answer_c(self,method):
        if method==1:
            self.ans.config(text="CORRECT",bg='green')
            self.score[int(self.order[self.t])-1]=self.score[int(self.order[self.t])-1]+(self.rounds[self.r.get()-2])
            self.score1.config(text=self.score[0])
            self.score2.config(text=self.score[1])
            self.score3.config(text=self.score[2])
            self.score4.config(text=self.score[3])
            self.reset()
            if self.t==4:
                self.t=0
                self.reset()
        elif method==0:
            self.ans.config(text="INCORRECT",bg='red')
            self.t=self.t+1
            if self.t==4:
                self.t=0
                self.reset()


    def reset(self):
        self.t=0
        self.team4.config(bg='#4BEBD8')
        self.team1.config(bg='#4BEBD8')
        self.team2.config(bg='#4BEBD8')
        self.team3.config(bg='#4BEBD8')
        fil=open('test.txt','a')
        fil.write('\n0')
        fil.close()

    def send(self):
        self.ans.config(text="START",bg='green')
        fil=open('test.txt','a')
        fil.write('\n1')
        fil.close()

        


root=Tk()
mygui=buzzer(root)
root.mainloop()
        
        
