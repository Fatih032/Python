n = int(input("Hesaplanacak akım sayısı:"))
kablotürü = input("Kullanılacak Kablo Türü(örnek: 3x , 4x vs.) : ")
mesafe = int(input("Mesafeyi giriniz : "))
if(kablotürü=="3x"):
    if(mesafe<500):
        for i in range(1, n+1):
            güc = float(input(str(i)+".Gücü giriniz:"))
            sonuç = round((güc/526)*1.1, 2)
            if(0<sonuç<=100):
                print(sonuç," A < 100 A olduğu için 3x16+10 mm^2 N2XH uygundur.")
            elif(100<sonuç<=127):
                print(sonuç," A < 127 A olduğu için 3x25+16 mm^2 N2XH uygundur.")
            elif(127<sonuç<=158):
                print(sonuç," A < 158 A olduğu için 3x35+16 mm^2 N2XH uygundur.")
            elif(158<sonuç<=192):
                print(sonuç," A < 192 A olduğu için 3x50+25 mm^2 N2XH uygundur.")
            elif(192<sonuç<=246):
                print(sonuç," A < 246 A olduğu için 3x70+35 mm^2 N2XH uygundur.")
            elif(246<sonuç<=298):
                print(sonuç," A < 298 A olduğu için 3x95+50 mm^2 N2XH uygundur.")
            elif(298<sonuç<=346):
                print(sonuç," A < 346 A olduğu için 3x120+70 mm^2 N2XH uygundur.")
            else:
                print("Hatalı giriş yaptınız.")

        
    elif(500<=mesafe<1000):
        for i in range(1, n+1):
            güc = float(input(str(i)+".Gücü giriniz:"))
            sonuç = round((güc/526)*1.1, 2)

            if(0<sonuç<=100):
                print(sonuç," A < 100 A olduğu için 3x16+10 mm^2 N2XH uygundur.")
            elif(100<sonuç<=127):
                print(sonuç," A < 127 A olduğu için 3x25+16 mm^2 N2XH uygundur.")
            elif(127<sonuç<=158):
                print(sonuç," A < 158 A olduğu için 3x35+16 mm^2 N2XH uygundur.")
            elif(158<sonuç<=192):
                print(sonuç," A < 192 A olduğu için 3x50+25 mm^2 N2XH uygundur.")
            elif(192<sonuç<=246):
                print(sonuç," A < 246 A olduğu için 3x70+35 mm^2 N2XH uygundur.")
            else:
                print("Hatalı giriş yaptınız.")
    

elif(kablotürü=="4x"):
    if(mesafe<500):
        for i in range(1, n+1):
            güc = float(input(str(i)+".Gücü giriniz:"))
            sonuç = round((güc/526)*1.1, 2)
            if(0<sonuç<=23):
                print(sonuç," A < 23 A olduğu için 4x1,5 mm^2 N2XH uygundur.")
            elif(23<sonuç<=32):
                print(sonuç," A < 32 A olduğu için 4x2,5 mm^2 N2XH uygundur.")
            elif(32<sonuç<=42):
                print(sonuç," A < 42 A olduğu için 4x4 mm^2 N2XH uygundur.")
            elif(42<sonuç<=54):
                print(sonuç," A < 54 A olduğu için 4x6 mm^2 N2XH uygundur.")
            elif(54<sonuç<=75):
                print(sonuç," A < 75 A olduğu için 4x10 mm^2 N2XH uygundur.")
            elif(75<sonuç<=100):
                print(sonuç," A < 100 A olduğu için 4x16 mm^2 N2XH uygundur.")
            elif(100<sonuç<=127):
                print(sonuç," A < 127 A olduğu için 4x25 mm^2 N2XH uygundur.")
            elif(127<sonuç<=158):
                print(sonuç," A < 158 A olduğu için 4x35 mm^2 N2XH uygundur.")
            elif(158<sonuç<=192):
                print(sonuç," A < 192 A olduğu için 4x50 mm^2 N2XH uygundur.")
            elif(192<sonuç<=246):
                print(sonuç," A < 246 A olduğu için 4x70 mm^2 N2XH uygundur.")
            elif(246<sonuç<=298):
                print(sonuç," A < 298 A olduğu için 4x95 mm^2 N2XH uygundur.")
            elif(298<sonuç<=346):
                print(sonuç," A < 346 A olduğu için 4x120 mm^2 uygundur.")
            else:
                print("Hatalı giriş yaptınız.")

    elif(500<=mesafe<1000):
        for i in range(1, n+1):
            güc = float(input(str(i)+".Gücü giriniz:"))
            sonuç = round((güc/526)*1.1, 2)
            if(0<sonuç<=23):
                print(sonuç," A < 23 A olduğu için 4x1,5 mm^2 N2XH uygundur.")
            elif(23<sonuç<=32):
                print(sonuç," A < 32 A olduğu için 4x2,5 mm^2 N2XH uygundur.")
            elif(32<sonuç<=42):
                print(sonuç," A < 42 A olduğu için 4x4 mm^2 N2XH uygundur.")
            elif(42<sonuç<=54):
                print(sonuç," A < 54 A olduğu için 4x6 mm^2 N2XH uygundur.")
            elif(54<sonuç<=75):
                print(sonuç," A < 75 A olduğu için 4x10 mm^2 N2XH uygundur.")
            elif(75<sonuç<=100):
                print(sonuç," A < 100 A olduğu için 4x16 mm^2 N2XH uygundur.")
            elif(100<sonuç<=127):
                print(sonuç," A < 127 A olduğu için 4x25 mm^2 N2XH uygundur.")
            elif(127<sonuç<=158):
                print(sonuç," A < 158 A olduğu için 4x35 mm^2 N2XH uygundur.")
            elif(158<sonuç<=192):
                print(sonuç," A < 192 A olduğu için 4x50 mm^2 N2XH uygundur.")
            elif(192<sonuç<=246):
                print(sonuç," A < 246 A olduğu için 4x70 mm^2 N2XH uygundur.")
            else:
                print("Hatalı giriş yaptınız.")
        else:
            print("Hatalı giriş yaptınız.")
else:
    print("Hatalı giriş yaptınız.")


    



    