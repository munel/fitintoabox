import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic

#load both ui file
uifile_1 = 'giris.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

uifile_2 = 'elleHesapla.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

uifile_3 = 'Ana_Ekran.ui'
form_3, base_3 = uic.loadUiType(uifile_3)

uifile_4 = 'koliAdetOtomatik.ui'
form_4, base_4 = uic.loadUiType(uifile_4)

uifile_5 = 'koliAdetManuel.ui'
form_5, base_5 = uic.loadUiType(uifile_5)


kutular = ["35,35,24","40,50,60", "50,70,80", "20,30,40", "65,55,95", "75,80,40"]
urunler = ["4,8,10","4,5,6", "10,12,4", "8,9,10","4,15,10","2,5,7","8,12,6"]


        
        
class elleHesapla(base_2,form_2):
    def __init__(self):
        super(base_2,self).__init__()
        self.setupUi(self)
        self.hesaplaButton.clicked.connect(self.hesapla)
    def hesapla(self):
        #Kutu ve ürün boyutları liste içine alındı
        self.kutu = [float(self.textEdit.toPlainText()),float(self.textEdit_2.toPlainText()),float(self.textEdit_3.toPlainText())]
        self.urun = [float(self.textEdit_4.toPlainText()),float(self.textEdit_5.toPlainText()),float(self.textEdit_6.toPlainText())]
        #Hesapla.hesapla(self.kutu,self.urun)
        gelenSonuc = Hesapla.hesapla(self.kutu,self.urun)
        self.sonucLabel.setText(str(gelenSonuc[0]))
        self.sonucLabel_3.setText(str(gelenSonuc[1]) + " Adet --> " + str(gelenSonuc[2][0]))
        self.sonucLabel_4.setText(str(gelenSonuc[3][0]) + " Adet --> " + str(gelenSonuc[3][1]))
        self.sonucLabel_5.setText(str(gelenSonuc[4][0]) + " Adet --> " + str(gelenSonuc[4][1]))
        self.sonucLabel_6.setText(str(gelenSonuc[5][0]) + " Adet --> " + str(gelenSonuc[5][1]))
        
        
class koliAdetManuel(base_5,form_5):
    def __init__(self):
        super(base_2,self).__init__()
        self.setupUi(self)

        self.hesaplaButton.clicked.connect(self.hesapla)
        
        self.kutu = []
        self.urun = []

        
    def hesapla(self):
        self.kutu = [float(self.textEdit_3.toPlainText()),float(self.textEdit_4.toPlainText()),float(self.textEdit_6.toPlainText())]
        self.urun = [float(self.textEdit_8.toPlainText()),float(self.textEdit_7.toPlainText()),float(self.textEdit_5.toPlainText())]  
        gelenSonuc = Hesapla.hesapla(self.kutu,self.urun)
        self.urunSayisi = int(self.textEdit.toPlainText())
        self.destedekiAdet = int(self.textEdit_2.toPlainText())
        
        gelenSonuc = Hesapla.hesapla(self.kutu,self.urun)
        self.enFazla = gelenSonuc[0]
        self.desteSayisi = int(self.urunSayisi/self.destedekiAdet)
        self.gerekliKoli = self.desteSayisi/self.enFazla
        self.label_7.setText(str(self.desteSayisi))
        self.label_13.setText("Toplam Deste Sayısı ----------------->" + str(self.desteSayisi) + "\n "
                              "Seçilen Kutuya Sığan Deste Sayısı --->" + str(gelenSonuc[0]) + "\n"
                              "Gerekli Olan Koli Sayısı------------->" + str(int(self.gerekliKoli)) +"\n"
                              "Artan Deste Sayısı------------------->" + str(self.desteSayisi - self.enFazla*int(self.gerekliKoli)))
        
class Hesapla:
    def hesapla(x,y):
        kutu = x
        deste = y
        desteVaryasyon = [[deste[0],deste[1],deste[2]], [deste[0],deste[2],deste[1]],[deste[1],deste[0],deste[2]],[deste[1],deste[2],deste[0]],[deste[2],deste[0],deste[1]],[deste[2],deste[1],deste[0]]]
        hesapDegerleri = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for i in range(0,len(desteVaryasyon)):
            kacAdet = list(map(lambda x,y: int(x/y),kutu,desteVaryasyon[i]))
            hesapDegerleri[i][1] = kacAdet[0] * kacAdet[1] * kacAdet[2]
            hesapDegerleri[i][2] = [desteVaryasyon[i],[kacAdet[0],kacAdet[1],kacAdet[2]]]
            kalanX = kutu[0] - (kacAdet[0]*desteVaryasyon[i][0])
            kalanY = kutu[1] - (kacAdet[1]*desteVaryasyon[i][1])
            kalanZ = kutu[2] - (kacAdet[2]*desteVaryasyon[i][2])
           
            kalanHesapX = YeniHesap.yeniHesap([kalanX,kutu[1],kutu[2]],desteVaryasyon[i])
            hesapDegerleri[i][3] = kalanHesapX
           
            kalanHesapY = YeniHesap.yeniHesap([kutu[0],kalanY,kutu[2]],desteVaryasyon[i])
            hesapDegerleri[i][4] = kalanHesapY
           
            kalanHesapZ = YeniHesap.yeniHesap([kutu[0],kutu[1],kalanZ],desteVaryasyon[i])
            hesapDegerleri[i][5] = kalanHesapZ
            hesapDegerleri[i][0] = hesapDegerleri[i][1] +  hesapDegerleri[i][3][0] + hesapDegerleri[i][4][0] + hesapDegerleri[i][5][0]
            
           
            
        #hesapDegerleri[i][0] = desteVaryasyon[i]
        #hesapDegerleri[i][1] = kacAdet[0] * kacAdet[1] * kacAdet[2]
        #hesapDegerleri.sort(reverse= True)
        #print(max(hesapDegerleri))
        hesapDegerleri.sort(reverse= True)
        for l in hesapDegerleri:           
            print(l)
        return hesapDegerleri[0]
            
        
        
        

        
class YeniHesap():           
            
    def yeniHesap(x,y):
        kutu = x
        deste = y
        desteVaryasyon = [[deste[0],deste[1],deste[2]], [deste[0],deste[2],deste[1]],[deste[1],deste[0],deste[2]],[deste[1],deste[2],deste[0]],[deste[2],deste[0],deste[1]],[deste[2],deste[1],deste[0]]]
        hesapDegerleri = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        for i in range(0,len(desteVaryasyon)):
            kacAdet = list(map(lambda x,y: int(x/y),kutu,desteVaryasyon[i]))
            hesapDegerleri[i][0] = kacAdet[0] * kacAdet[1] * kacAdet[2]
            hesapDegerleri[i][1] = desteVaryasyon[i]
            hesapDegerleri[i][2] = [kacAdet[0],kacAdet[1],kacAdet[2]]
            #print(hesapDegerleri[i])
        hesapDegerleri.sort(reverse= True)
        return hesapDegerleri[0]
        
class EkranBir(base_1, form_1):

    def __init__(self):
        super(base_1,self).__init__()

        self.setupUi(self)
        self.comboBox.addItems(kutular)
        self.comboBox_2.addItems(urunler)        
        self.comboBox.activated.connect(self.kutuSecim)
        self.comboBox_2.activated.connect(self.urunSecim)
        


        
        self.pushButton.clicked.connect(self.hesapla)
      

    def kutuSecim(self):
        self.kutu = self.comboBox.currentText().split(",")
        self.kutu[0] = float(self.kutu[0])
        self.kutu[1] = float(self.kutu[1])
        self.kutu[2] = float(self.kutu[2])
        
        #print(self.kutu)
    def urunSecim(self):
        self.urun = self.comboBox_2.currentText().split(",")
        self.urun[0] = float(self.urun[0])
        self.urun[1] = float(self.urun[1])
        self.urun[2] = float(self.urun[2])
    def hesapla(self):
        Hesapla.hesapla(self.kutu,self.urun)
        gelenSonuc = Hesapla.hesapla(self.kutu,self.urun)
        self.sonucLabel.setText(str(gelenSonuc[0]))
        self.sonucLabel_3.setText(str(gelenSonuc[1]) + " Adet --> " + str(gelenSonuc[2][0]))
        self.sonucLabel_4.setText(str(gelenSonuc[3][0]) + " Adet --> " + str(gelenSonuc[3][1]))
        self.sonucLabel_5.setText(str(gelenSonuc[4][0]) + " Adet --> " + str(gelenSonuc[4][1]))
        self.sonucLabel_6.setText(str(gelenSonuc[5][0]) + " Adet --> " + str(gelenSonuc[5][1]))
        


class koliAdetOtomatik(base_4, form_4):

    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.comboBox.addItems(kutular)
        self.comboBox_2.addItems(urunler)        
        self.comboBox.activated.connect(self.kutuSecim)
        self.comboBox_2.activated.connect(self.urunSecim)
        self.pushButton.clicked.connect(self.hesapla)
        
        self.kutu = []
        self.urun = []
    
    def hesapla(self):
        # Seçilen Kutua Kaç Adet Sığıyor Hesaplanı
        self.urunSayisi = int(self.textEdit.toPlainText())
        self.destedekiAdet = int(self.textEdit_2.toPlainText())
        
        gelenSonuc = Hesapla.hesapla(self.kutu,self.urun)
        self.enFazla = gelenSonuc[0]
        self.desteSayisi = int(self.urunSayisi/self.destedekiAdet)
        self.gerekliKoli = self.desteSayisi/self.enFazla
        self.label_7.setText(str(self.desteSayisi))
        self.label_13.setText("Toplam Deste Sayısı ----------------->" + str(self.desteSayisi) + "\n "
                              "Seçilen Kutuya Sığan Deste Sayısı --->" + str(gelenSonuc[0]) + "\n"
                              "Gerekli Olan Koli Sayısı------------->" + str(int(self.gerekliKoli)) +"\n"
                              "Artan Deste Sayısı------------------->" + str(self.desteSayisi - self.enFazla*int(self.gerekliKoli)))
    
                        
    def kutuSecim(self):
        self.kutu = self.comboBox.currentText().split(",")
        self.kutu[0] = float(self.kutu[0])
        self.kutu[1] = float(self.kutu[1])
        self.kutu[2] = float(self.kutu[2])
        #print(self.kutu)
    def urunSecim(self):
        self.urun = self.comboBox_2.currentText().split(",")
        self.urun[0] = float(self.urun[0])
        self.urun[1] = float(self.urun[1])
        self.urun[2] = float(self.urun[2])

        
class Ana_Ekran(base_3,form_3):
    def __init__(self):
        super(base_2,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.giris)
        self.pushButton_2.clicked.connect(self.manuel) 
        self.pushButton_3.clicked.connect(self.kutuOtomatik) 
        self.pushButton_4.clicked.connect(self.close) 
        self.pushButton_5.clicked.connect(self.kutuAdetManuel) 
         
    def giris(self):
        self.child_win = EkranBir()
        self.child_win.show() 
    def manuel(self):
        self.child_win = elleHesapla()
        self.child_win.show()
    def kutuOtomatik(self):
        self.child_win = koliAdetOtomatik()
        self.child_win.show()  
    def kutuAdetManuel(self):
        self.child_win = koliAdetManuel()
        self.child_win.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ana_Ekran()
    ex.show()
    sys.exit(app.exec_())