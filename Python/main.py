from kod_satir import *
from mantik_kapilari import *

def devre_calistir(tanimlar, girdiler):
    degerler = {}

    # Kullanıcı girdilerini aliyorum
    for giris in girdiler:
        degerler[giris] = int(input(f"{giris} için değer girin (0 veya 1): "))

    # Tanımları sırayla işle
    tanimlar_sirasi = tanimlar.copy()  # Tanımların kopyasını aldığım yer
    islenmis_tanimlar = set()  # İşlenen tanımları takip etmek içn

    while tanimlar_sirasi:
        silinecekler = []
        for tanim in tanimlar_sirasi:
            cikis, ifade = tanim.split("--")  
            kapi, girisler = ifade.split("=")
            girisler = girisler.split(",")

            # Girişlerin hepsi hesaplanmış mı kontrol ettiğim kısım
            #A,B GİRİŞ
            #1,0 DEGER
            
            if all(g in degerler for g in girisler):
                if kapi == "AND":
                    degerler[cikis] = AND(degerler[girisler[0]], degerler[girisler[1]])
                
                elif kapi == "OR":
                    degerler[cikis] = OR(degerler[girisler[0]], degerler[girisler[1]])
                elif kapi == "DEGIL":
                    degerler[cikis] = NOT(degerler[girisler[0]])
                print(degerler[cikis])             
                silinecekler.append(tanim)  # eğer işlendi ise tanım öikarmak için
                islenmis_tanimlar.add(tanim)

        # ve siradan kaldırıyorum tanimlari
        for tanim in silinecekler:
            tanimlar_sirasi.remove(tanim)

        # kontrol ekledim
        if not silinecekler:
            print("Bazı tanımlar için yeterli veri yok! Devre hesaplanamadı.")
            return
    
   
    print(f"Sonuç: F = {degerler.get('F', 'Hesaplanamadı')}")



from girdiler import *

# Tekrar tekrar girdi almak istediğimden açtım
while True:
    devre_calistir(tanimlar, girdiler)

    
    tekrar = int(input("Yeni değer girmek istiyor musunuz? [1: Evet, 0: Hayır]\n= "))
    
    if tekrar == 0:
        print("Program sonlandırılıyor...")
        break
