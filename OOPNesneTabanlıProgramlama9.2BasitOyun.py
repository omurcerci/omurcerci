import time
import random
import sys

class oyuncu():
    def __init__(self,isim,can=5,enerji=100):
        self.isim = isim
        self.can = can
        self.darbe = 0
        self.enerji =enerji
        
    def mevcut_durumu_gorüntüle(self):
        print("isim",self.isim)
        print("can",self.can)       
        print("darbe",self.darbe)
        print("enerji",self.enerji)
        
    def saldır(self,rakip):
        print("Bir saldırı gerçekleştirddiniz.")
        print("Saldırı sürüyor. Bekleyiniz")
        
        for i in range(10):
            time.sleep(3)
            print(".",end ="",flush = True)
        
        sonuç = self.saldırı_sonucunu_hesapla()
        
        if sonuç == 0:
            print("\n SONUÇ : Kazanan taraf yok.")
            
        if sonuç == 1:
            print("\n SONUÇ : Rakibinizi darbelediniz.")
            self.darbele(rakip)
            
        if sonuç == 2:
            print("\n SONUÇ : Rakibinizden darbe aldınız.")
            self.darbele(self)
            
        def saldırı_sonucunu_hesapla(self):
            return random.randint(0,2)
        
        def kaç(self):
            print("Kaçılıyor...")
            for i in range(10):
                time.sleep(3)
                print("\n",flush=True)
                
            print("Rakibiniz sizi yakaladı")
        
        def darbele(self,darbelenen):
            darbelenen.darbe += 1
            darbelenen.enerji -= 1
            if(darbelenen.darbe % 5) == 0:
                darbelenen.can -= 1
            if darbelenen.can < 1:
                darbelenen.enerji = 0
                print("Oyunu {} kazandı !",format(self.isim))
                self.oyundan_çık()
                
        def oyundan_çık(self):
            print("Çıkılıyor...")
            sys.exit()
            

print("""
      ####################################)
      
      
      Oyuncular
      
      siz = Oyuncu("Ahmet")
      
      rakip = Oyuncu("Mehmet")
      

      """)         


      
    ########################################
siz = oyuncu("Ahmet")
rakip = oyuncu("Mehmet")

    # Oyun başlangıcı       
while True:
    
    print('Şu anda rakibinizle karşı karşıyaysınız.' , 
        '  Yapmak istediğiniz hamle : ' ,
        '  Saldır : s', 
        '  Kaç : k',
        '  Çık : q', sep='\n'
          )
    
    hamle = input("\n >")
    if hamle == "s":
        siz.rakip(rakip)
        print("Rakibinizin durumu")
        rakip.mevcut_durumu_gorüntüle()
        
        print("Sizin durumunuz")
        siz.mevcut_durumu_gorüntüle()
        
    if hamle == "k":
        siz.kaç()
        
    if hamle == "q":
        siz.oyundan_çık()
        
