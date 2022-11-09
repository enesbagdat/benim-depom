print("""işlemler:
1 toplama
2 çıkarma
3 çarpma
4 bölme
5 ortalama
6 üs bulma
""")

islem = str(input("işlem gir: "))

if islem == "1":
    sayi1 = int(input("sayı1 gir : "))
    sayi2 = int(input("sayı2 gir : "))
    print("toplam:", sayi1 + sayi2)
elif islem == "2":
    sayi1 = int(input("sayı1 gir: "))
    sayi2 = int(input("sayı2 gir: "))
    print("toplam:", sayi1 - sayi2)
elif islem == "3":
    sayi1 = int(input("Sayı1 gir: "))
    sayi2 = int(input("sayı2 gir: "))
    print("toplam:", sayi1 * sayi2)
elif islem == "4":
    sayi1 = int(input("sayı1 gir: "))
    sayi2 = int(input("sayı2 gir: "))
    print("toplam:", sayi1 / sayi2)
elif islem == "5":
    sayi1 = input('1. Sayı : ')
    sayi2 = input('2. Sayı : ')
    ortalama=(int(sayi1)+int(sayi2))/2
    print("Ortalama :{0} ".format(ortalama))
elif islem == "6":
    sayi1 = int(input("sayı gir: "))
    sayi2 = int(input("üs gir: "))
    print("cevap:", sayi1 ** sayi2)
else :
    print("yanlış sayı girdin")
