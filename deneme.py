kutular= [[20,30,40],[50,60,70],[77,33,51],[35,35,24]]
desteler = [[2,3,4],[5,6,7],[2,5,6],[4,8,10],[7,2.5,7.5]]
#kutu = kutular[0]
#deste = desteler[0]

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
        
        hataVarmi.hataVarmi(hesapDegerleri,kutu)
            
        
        
        

        
class YeniHesap:
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
class hataVarmi():
    def hataVarmi(hesaplar,gelenKutu):
        enCok = hesaplar[0]
        kutu = gelenKutu
        print("En Çok")
        print(str(enCok))
        print(str(kutu))
        
        

Hesapla.hesapla(kutular[3],desteler[4])

    

    