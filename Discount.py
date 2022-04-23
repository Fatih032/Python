# indirim hesaplayan python kodu
price = float(input("Fiyatı giriniz: "))
discount = float(input("İndirim yüzdesini giriniz: "))
discounted_price = price - (price * discount / 100)
print("İndirimli fiyat:", discounted_price)