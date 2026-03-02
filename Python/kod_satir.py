# Kod Girdisi almak örn: F--AND=A,B

tanimlar = []
adet = int(input("Kaç adet kod yazacaksın?\n= "))

for i in range(adet):
    tanim = input(f"{i + 1}. Satırı Yaz\n> ")
    tanimlar.append(tanim)

