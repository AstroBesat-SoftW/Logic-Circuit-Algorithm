#  Burada örnek F--AND=A,B dediysek. Burada kaç adet bilinmeyen var ve ne diye kaydettin soruyor
# Bu örnekte A ve B bilinmeyen yani 2 adet var biri A diğeri B
girdiler = []
adet_2 = int(input("Kaç adet Girdi yazacaksın?\n= "))

for i in range(adet_2):
    girdi = input("Girdi ne? [Orn: A,B..]\n> ")
    girdiler.append(girdi)

