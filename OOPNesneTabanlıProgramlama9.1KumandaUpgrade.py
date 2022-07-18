import time
import random


# Televizyon durumu , televizyon ses , kanal_listesi , Kanal , kanal değiştirme & yukarı kanal aşağı kanal , numara tabanlı kanala gitmek


class Kumanda(): #kumanda sınıfımızı oluşturduk
    def __init__(self,tv_durum="Kapalı",tv_ses = 0 , kanal_listesi = ["Trt","KanalD","Star","Jojo"],kanal ="Trt",kanal_degistirmek = ""):
        self.tv_durum = tv_durum
        self.kanal_listesi = kanal_listesi
        self.tv_ses = tv_ses
        self.kanal = kanal
        self.kanal_degistirmek = kanal_degistirmek
    
    def tv_ac(self):
        if (self.tv_durum =="Açık"):
            print("Televizyonu zaten açık")
        else:
            print("Televizyon açılıyor")
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if(self.tv_durum =="Kapalı"):
            print("Televizyonunuz zaten kapalı")
        else:
            print("Televizyonunuz kapatılıyor")
            self.tv_durum = "Kapalı"
            
    def ses_ayarları(self):
        while True:
            girdi = input("Sesi azalt : "<" \n Sesi aç : ">" \n Çıkış : çıkış ")
            if (girdi == "<"):
                if (self.tv_ses !=0):
                    self.tv_ses -= 1
            elif(girdi == ">"):
                if(self.tv_ses !=31):
                    self.tv_ses += 1
                    
    def kanal_duzenlemek(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        
        time.sleep(1)
        print("Kanal başarıyla eklendi")
        
    def kanal_duzenlemek2(self,kanal_ismi):
        
        for i in range(self.kanal_listesi):
            if (i in self.kanal_listesi):
                self.kanal_listesi.remove(kanal_ismi)
                 
                time.sleep(1)
        
                print("Kanal başarıyla silindi")
            else:
                raise Exception("Boyle bir kanal mevcut değildir.")
            
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_list)-1)
        self.kanal_listesi[rastgele]
        
        print("Şu anki kanal",self.kanal)
    
    def kanal_degistirmek(self):
        
        cevap = input("Yukarı kanal : "+" \n Aşağı Kanal : "-" \n Çıkış : çıkış" )
        
        if (cevap == "+"):
            print("Yeni kanalınız : {}".format(self.kanal)+1)
            
        if (cevap == "-"): 
            print("Yeni kanalınız {}".format(self.kanal)-1)
            
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        
        return " Tv Durumu : {} \n Tv Ses : {} \n Kanal Listesi : {} Şu anki Kanal : {} \n".format(self.tv_durum,self.tv_ses,self.kanal,self.kanal)
    

print("""
      
      Televizyon Uygulaması
      
      1. Tv Aç
      2. Tv Kapat
      3. Ses Ayarları 
      4. Kanal Ekle 
      5. Kanal Sil
      6. Rastgele Kanala Geçme
      7. Kanal Degistirmek
      8.Televizyon bilgileri
      
      Çıkmak için 'q' ya basın.
   
      
      
      """)

kumanda = Kumanda()    
while True():       
    işlem = input("İşlemi seçiniz :")
    
    if (işlem == "q" ):
        print("Program sonlandırılıyor")
        
    if ( işlem  == "1"):
        kumanda.tv_ac()
    if ( işlem  == "2"):
        kumanda.tv_kapat()
    if ( işlem  == "3"):
        kumanda.ses_ayarları()
    if ( işlem  == "4"):
        kumanda.kanal_duzenlemek
        kanal_isimleri =input("Kanal isimlerini ',' ile ayırarak giriniz :")
        kanal_listesi = kanal_isimleri.split(",")  
            
        for eklenecekler in kanal_listesi:
            kumanda.kanal_duzenlemek(eklenecekler)
    if ( işlem  == "5"):
        kanal_isimleri =input("Kanal isimlerini ',' ile ayırarak giriniz :")
        kanal_listesi = kanal_isimleri.split(",")  
            
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
            kumanda.kanal_duzenlemek2
            
    if ( işlem  == "6"):
        kumanda.rastgele_kanal()
    if ( işlem  == "7"):
        kumanda.kanal_degistirmek()   
    if ( işlem  == "8"):
        print(kumanda) 
    else:
        print("Geçersiz işlem")
            