def topla(s1,s2):
    return s1+s2
def cikar(s1,s2):
    return s1-s2
def carp(s1,s2):
    return s1*s2
def bol(s1,s2):
    return s1/s2
def bilgilendir():
    print("Toplama: 1, Çıkarma 2, Çarpma: 3, Bölme: 4, Bilgilendirme: i, Çıkış: q")
print("Hesap Makinesi v1.0")
bilgilendir()
while True:
    islem = input("İşlem ID'si giriniz: ")
    if islem == "q":
        print("Program sonlandırılıyor... ")
        break
    elif str(islem) == "i":
        bilgilendir()
        continue
    sayi1 = int(input("İlk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    if islem == "1":
        print("Sonuç:",topla(sayi1,sayi2))
    elif islem == "2":
        print("Sonuç:", cikar(sayi1, sayi2))
    elif islem == "3":
        print("Sonuç:", carp(sayi1, sayi2))
    elif islem == "4":
        print("Sonuç:", bol(sayi1, sayi2))
    else:
        print("Lütfen geçerli bir ID giriniz. ")