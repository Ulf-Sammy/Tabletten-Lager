import datetime


class Tablette(object):
    def __init__(self): 
        self.Name = ""
        self.inMengeTabletten = 0
        self.istMengeTabletten = 0
        self.MengeproTag = 0
        self.Tab_max_Tag = 0
        self.nochTage = 0
        self.Tab_noch_Tage = 0
        self.InLagerTag = datetime
        self.EndLagerTag = datetime
        self.verbrauchteTage = datetime
         
    def Get_Name(self):
        return self.Name

    def Get_EndDatum(self):
        InfoText = "{:02d}.{:02d}.{:4d}".format(self.EndLagerTag.day,self.EndLagerTag.month,self.EndLagerTag.year)
        return InfoText

    def Get_InDatum(self):
        InfoText = "{:02d}.{:02d}.{:4d}".format(self.InLagerTag.day,self.InLagerTag.month,self.InLagerTag.year)
        return InfoText

    def Get_Heute(self):
        return datetime.date.today()

    def Get_MengeproTag(self):
        return self.MengeproTag

    def Get_InMenge(self):
        return self.inMengeTabletten


    def NeueTablette(self, Name, TagMenge, Menge): 
       self.Name = Name
       self.MengeproTag = TagMenge
       self.inMengeTabletten =  Menge
       self.InLagerTag = datetime.date.today()
       Tablette.berechneVerbrauch(self)


    def fill_Lager ( self, Menge):
       self.inMengeTabletten = self.istMengeTabletten + Menge
       self.InLagerTag = datetime.date.today()
       Tablette.berechneVerbrauch(self)

    def berechneVerbrauch(self):
       self.verbrauchteTage = datetime.date.today() - self.InLagerTag
       self.istMengeTabletten = self.inMengeTabletten - (self.verbrauchteTage.days * self.MengeproTag)
       self.Tab_noch_Tage = int(self.istMengeTabletten / self.MengeproTag)
       self.Tab_max_Tag  = int (self.inMengeTabletten  / self.MengeproTag)
       self.EndLagerTag = self.InLagerTag + datetime.timedelta (days = self.Tab_max_Tag) 

    def LoadLager(self, Data):
        Wert = Data.split('|')
        self.Name = Wert[0]
        self.inMengeTabletten = int(Wert[1])
        self.MengeproTag = int(Wert[2])
        self.InLagerTag = datetime.date(int(Wert[5]),int(Wert[4]),int(Wert[3]))
        Tablette.berechneVerbrauch(self)

    def SaveLager(self):
        SaveText = "{:20}|{:4d}|{:2d}|{:2d}|{:2d}|{:4}|\n".format(self.Name,self.inMengeTabletten,self.MengeproTag,self.InLagerTag.day,self.InLagerTag.month,self.InLagerTag.year)
        return SaveText
   
