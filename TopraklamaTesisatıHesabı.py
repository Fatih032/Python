import math

işlem = input("Hesaplanacak Topraklama Türünü giriniz(örneğin gözlü,ring,çubuk):")

#Gözlü topraklayıcı hesabı
if(işlem=="gözlü"):
    uzunluk = float(input("Uzunluğu giriniz: "))
    alan = float(input("Alanı giriniz: "))
    eşdeğerçap = ((4*alan)/3.14)**0.5
    özgültoprakdirenci = 80
    ra =round(özgültoprakdirenci/(2*eşdeğerçap)+(özgültoprakdirenci/uzunluk),2)
    print("Özgül Topraklayıcı Direnci: ",ra)
#Ring topraklayıcı hesabı
elif(işlem=="ring"):
    uzunluk = float(input("Uzunluğu giriniz: "))
    alan = float(input("Alanı giriniz: "))
    eşdeğerçap = ((4*alan)/3.14)**0.5
    özgültoprakdirenci = 150
    ra=round((2*özgültoprakdirenci)/(3*eşdeğerçap), 2)
    print("Ring Topraklayıcı Direnci: ",ra)
#Çubuk topraklayıcı hesabı
elif(işlem=="çubuk"):
    n = float(input("Topraklayıcı Çubuk adedini giriniz: "))
    l = float(input("Topraklayıcı Çubuk uzunluğunu giriniz: "))
    d = float(input("Topraklayıcı Çubuk kesit alanını giriniz: "))
    ra=round((150/(2*3.14*l))*math.log((4*l)/d,math.e),2)
    ra = round(ra/6,2)
    print("Çubuk topraklama Diranci: ",ra)

else:
    print("Hatalı giriş yaptınız.Yeniden deneyin.")
    





