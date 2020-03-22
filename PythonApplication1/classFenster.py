from tkinter import *
from TablettenLager import Tablette
from tkinter.messagebox import showerror

DateiName = "TablettenLager.txt"


class MyApp(Frame):
    def __init__(self):
        super().__init__()
        
        self.Lager = [] # Lager Daten
        self.NeueMenge = int # neue Menge Daten
        self.Liste_Namen =  []
        self.T_Index = 0
        self.Ende = True
        self.Load_Data()
        self.heute  = Tablette().Get_Heute()

        self.initUI()
        self.Genug_Tabletten()

    def initUI(self):
        self.master.geometry("500x300+400+400")
        self.master.title("Mein Tabletten Lager")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(0, pad = 2)
        self.columnconfigure(1, pad = 0)
        self.columnconfigure(2, pad = 0)
        self.columnconfigure(3, pad = 2)
        self.rowconfigure(0, pad = 10)
        self.rowconfigure(1, pad=20)
        self.rowconfigure(2, pad=0)
        self.rowconfigure(3, pad=0)
        self.rowconfigure(4, pad=0)
        self.rowconfigure(5, pad=0)
        self.rowconfigure(6, pad=0)
        self.rowconfigure(7, pad=0)
        self.rowconfigure(8, pad=0)
        self.rowconfigure(9, pad=0)
        self.rowconfigure(10, pad=20)
        self.rowconfigure(11, pad=20)
        self.rowconfigure(12, pad=20)

        Label(self,text=" Mein Tabletten-Lager : ",relief=SUNKEN,bg = "purple1").grid(row=0,column=0,columnspan=4,sticky=W+E)
        Label(self,text=" Tabletten Name ", relief=RIDGE,bg= "SteelBlue1", width = 30).grid(row=3,column=0)
        Label(self,text=" Menge "         , relief=RIDGE,bg= "SteelBlue1", width = 10).grid(row=3,column=1)
        Label(self,text=" EndDatum "      , relief=RIDGE,bg= "SteelBlue1", width = 15).grid(row=3,column=2)
        Label(self,text=" noch Tage"      , relief=RIDGE,bg= "SteelBlue1", width = 10).grid(row=3,column=3)
        self.button1 = Button(self, text='   Tabletten auffüllen  ', command= self.Tabletteauffuellen,width=20,bg="LightYellow3").grid(row = 10, column = 0)
        self.button2 = Button(self, text='  Tablette neu anlegen  ', command= self.NeueTablette      ,width=20,bg="LightYellow3").grid(row = 11, column = 0)
        self.button3 = Button(self, text='Tabletten Lager anzeigen', command= self.ZeigeLager        ,width=20,bg="LightYellow3").grid(row = 12, column = 0)
        self.button4 = Button(self, text='Ende'                    , command= self.CloseWindow       ,width=10,bg="firebrick1").grid(row = 12, column = 3)

        r = 4
        for t in self.Lager:
             self.Liste_Namen.append(t.Get_Name())
             Tag = t.Tab_noch_Tage
             if (Tag > 14):
                Color= "lawn green"
             elif (Tag >= 7 ) and (Tag <= 14):
                 Color = "goldenrod1"
             else: 
                 Color = "orange red"
             Label(self,text=t.Get_Name(),         relief=RIDGE,width=30,bg = Color).grid(row=r,column=0)
             Label(self,text=t.istMengeTabletten,  relief=RIDGE,width=10,bg = Color).grid(row=r,column=1)
             Label(self,text=t.Get_EndDatum() ,   relief=RIDGE,width=15,bg = Color).grid(row=r,column=2)
             Label(self,text=t.Tab_noch_Tage  ,   relief=RIDGE,width=10,bg = Color).grid(row=r,column=3)
             r += 1       
        
        Label(self,text=" ",relief=RIDGE,bg= "maroon1").grid(row=9,column=0,columnspan=4,sticky=W+E)        

    def initDialog1(self):
        self.Dialog1 = Tk()
        self.Dialog1.geometry("180x100+500+550")
        self.Dialog1.title("Neue Menge")
        self.Dialog1.rowconfigure(0, pad = 10)
        self.var = StringVar(self.Dialog1)
        self.var.set(self.Lager[self.T_Index].Get_Name())

        OptionMenu(self.Dialog1, self.var, *self.Liste_Namen, command=self.readTablettenPlatz).grid(row=0,column=0,columnspan=4,sticky=W+E)
        Label(self.Dialog1,text =" neue Menge",width = 10).grid(row= 1, column =  0)
        self.entryVar = StringVar(self.Dialog1)
        self.entryVar.set("0")

        self.entry = Entry(self.Dialog1,width=10, textvariable = self.entryVar).grid(row = 1, column = 1)
        self.buttonE = Button(self.Dialog1, text='Ende'                    , command= self.readMenge         ,width=10,bg="firebrick1").grid(row = 2, column = 1)

    def initDialog2(self):
        self.Dialog2 = Tk()
        self.Dialog2.geometry("200x140+500+550")
        self.Dialog2.title("Neue Tablette")
        self.Dialog2.rowconfigure(0, pad = 10)
        self.Dialog2.rowconfigure(4, pad = 20)

        self.entryVar1 = StringVar(self.Dialog2)
        self.entryVar2 = StringVar(self.Dialog2)
        self.entryVar3 = StringVar(self.Dialog2)
        Label(self.Dialog2,text ="Name Tablette Daten eingebn",width = 26,relief=RIDGE,bg= "SteelBlue1").grid(row= 0, column =  0,columnspan=2,sticky=W+E)
        Label(self.Dialog2,text ="Name Tablette       :",width = 16).grid(row= 1, column =  0)
        Label(self.Dialog2,text ="Tabletten pro Tag   :",width = 16).grid(row= 2, column =  0)
        Label(self.Dialog2,text ="Menge der Tabletten :",width = 16).grid(row= 3, column =  0)

        self.entry1 = Entry(self.Dialog2,width=10,textvariable=self.entryVar1).grid(row = 1, column = 1)
        self.entry2 = Entry(self.Dialog2,width=10,textvariable=self.entryVar2).grid(row = 2, column = 1)
        self.entry3 = Entry(self.Dialog2,width=10,textvariable=self.entryVar3).grid(row = 3, column = 1)

        self.buttonE = Button(self.Dialog2, text='Ende'                    , command= self.readneuTablette         ,width=10,bg="firebrick1").grid(row = 4, column = 1)

    def initDialog3(self):
        dark_Color = True
        self.Dialog3 = Tk()
        self.Dialog3.geometry("745x300+500+500")
        self.Dialog3.title("Tabletten Lager")
        self.Dialog3.rowconfigure(0, pad = 10)
        Label(self.Dialog3,text="Mein Tabletten-Lager : ",relief=SUNKEN,bg = "purple1").grid(row=0,column=0,columnspan=7,sticky=W+E)
        Label(self.Dialog3,text="Tabletten Name ", relief=RIDGE,bg= "maroon1", width = 30).grid(row=3,column=0)
        Label(self.Dialog3,text="Tabl./Tag"      , relief=RIDGE,bg= "maroon1", width = 10).grid(row=3,column=1)
        Label(self.Dialog3,text="in Menge"       , relief=RIDGE,bg= "maroon1", width = 10).grid(row=3,column=2)
        Label(self.Dialog3,text="in Datum"       , relief=RIDGE,bg= "maroon1", width = 15).grid(row=3,column=3)
        Label(self.Dialog3,text="ist Menge"      , relief=RIDGE,bg= "maroon1", width = 10).grid(row=3,column=4)
        Label(self.Dialog3,text="EndDatum"       , relief=RIDGE,bg= "maroon1", width = 15).grid(row=3,column=5)
        Label(self.Dialog3,text="noch Tage"      , relief=RIDGE,bg= "maroon1", width = 10).grid(row=3,column=6)
        r = 4
        for t in self.Lager:
             if dark_Color:
                Color= "light grey"
                dark_Color = False
             else: 
                Color = "antique white"
                dark_Color = True
             Label(self.Dialog3,text=t.Get_Name(),        relief=RIDGE,width=30,bg = Color).grid(row=r,column=0)
             Label(self.Dialog3,text=t.Get_MengeproTag(), relief=RIDGE,width=10,bg = Color).grid(row=r,column=1)
             Label(self.Dialog3,text=t.inMengeTabletten,  relief=RIDGE,width=10,bg = Color).grid(row=r,column=2)
             Label(self.Dialog3,text=t.Get_InDatum(),     relief=RIDGE,width=15,bg = Color).grid(row=r,column=3)
             Label(self.Dialog3,text=t.istMengeTabletten, relief=RIDGE,width=10,bg = Color).grid(row=r,column=4)      
             Label(self.Dialog3,text=t.Get_EndDatum(),    relief=RIDGE,width=15,bg = Color).grid(row=r,column=5)
             Label(self.Dialog3,text=t.Tab_noch_Tage,     relief=RIDGE,width=10,bg = Color).grid(row=r,column=6)
             r += 1       
        
        Label(self.Dialog3,text=" ",relief=RIDGE,bg= "maroon1").grid(row=9,column=0,columnspan=7,sticky=W+E)        

    def Genug_Tabletten(self):
        MinTage =  []
        for m in self.Lager:
            MinTage.append(m.Tab_noch_Tage)
        tage = min(MinTage)
        Text = "Du hast in nicht genug Tabletten !! \n Sie reichen noch für {:2d} Tage !".format(tage)
        if ( tage < 5):
            showerror(title = "Arzt !", message = Text )
  

    def ZeigeLager(self):
        self.initDialog3()
        self.Dialog3.mainloop()

    def NeueTablette(self):
        self.initDialog2()
        self.Dialog2.mainloop()

    def Tabletteauffuellen(self):
        self.initDialog1()
        self.Dialog1.mainloop()

    def readTablettenPlatz(self, text):
        self.T_Index = self.Liste_Namen.index(text)

    def readMenge(self):
        self.Dialog1.destroy()
        self.NeueMenge = int(self.entryVar.get())
        self.Lager[self.T_Index].fill_Lager(self.NeueMenge)
        self.Ende = True
        self.Save_Data()
        self.master.destroy()

    def readneuTablette(self):
        self.Dialog2.destroy()
        T_Name = self.entryVar1.get()
        T_TagMenge = int(self.entryVar2.get())
        T_Menge    = int(self.entryVar3.get())
        nT = Tablette() 
        nT.NeueTablette(T_Name,T_TagMenge,T_Menge )
        self.Lager.append(nT)
        self.Ende = True
        self.Save_Data()
        self.master.destroy()

    def Get_Intex(self):
        return self.T_Index
  
    def Load_Data(self):
        self.Lager.clear()
        Datei = open(DateiName, "r")
        Tag = Datei.readline()
        for Line in Datei:
            nT = Tablette() 
            nT.LoadLager(Line)
            self.Lager.append(nT)
        Datei.close()
        
    def Save_Data(self):
        Datei = open(DateiName, "w")
        Datei.write(str(self.heute)+"\n")
        for Line in self.Lager:
            Datei.write(Line.SaveLager())
        Datei.close()

    def Ende_Dialog(self):
        return self.End

    def CloseWindow(self):
        self.Ende = False
        self.master.destroy()
