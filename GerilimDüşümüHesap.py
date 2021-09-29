
trafosayısı = int(input("Trafo Sayısını giriniz:"))
linyesayısı = int(input("Linye Sayısını giriniz:"))

sonuç1=0
sonuç2=0
for i in range(1,trafosayısı+1):
    TG1 = float(input(str(i)+".Trafo Gücü:"))
    uzunluk = float(input(str(i)+".Mesafe:"))
    tkablotürü = float(input(str(i)+".Kablo Kesit Alanı:"))
    sonuç1=sonuç1+(TG1*uzunluk)/tkablotürü
    
for i in range(1,linyesayısı+1):
    linyegücü = float(input(str(i)+".Linye Gücü:"))
    mesafe = float(input(str(i)+".Mesafe:"))
    kablotürü = float(input(str(i)+".Kablo Kesit Alanı:"))
    sonuç2=sonuç2+(linyegücü*mesafe)/kablotürü


yenisonuç1 = sonuç1 * 0.0124

yenisonuç2 = sonuç2 * 0.074

if (yenisonuç2<=1.5):
    breakpoint
else:
    print("Linye gerilim düşümü = "+str(yenisonuç2)+" > 1.5 olduğu için linye gerilim düşümünü azaltınız.")


yenisonuç = round(yenisonuç1+yenisonuç2, 2)



print("Sonuç = ",yenisonuç)
if(yenisonuç <= 5 and yenisonuç >= 0 ):
    print("Gerilim düşümü = "+str(yenisonuç)+" < 5 olduğu için uygundur.")
else:
    print("Gerilim düşümü = "+str(yenisonuç)+" > 5 olduğu için uygun değildir.Lütfen gerilim düşümünü azaltınız.")


