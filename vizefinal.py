print("Girilen Notlara Gore Ortalama Hesaplama")

vize = int(input("Vize notunuzu giriniz : "))
final = int(input("Final notunuzu giriniz : "))
sunum = input("Sunum yaptin mi ? (e/h) : ")
proje = input("Proje yaptin mi ? (e/h) : ")

while sunum == "e" and proje == "e":
    sunum = 10
    proje = 30
    ortalama = ((vize * 25)/100) + ((final * 35)/100) + sunum + proje
    print("Donem sonu ortalamaniz ", ortalama,"'dir.")
    break

while sunum == "e" and proje == "h":
    sunum = 10
    proje = 0
    ortalama = ((vize * 25)/100) + ((final * 35)/100) + sunum + proje
    print("Donem sonu ortalamaniz ", ortalama,"'dir.")
    break

while sunum == "h" and proje == "e":
    sunum = 0
    proje = 30
    ortalama = ((vize * 25)/100) + ((final * 35)/100) + sunum + proje
    print("Donem sonu ortalamaniz ", ortalama,"'dir.")

while sunum == "h" and proje == "h":
    sunum = 0
    proje = 0
    ortalama = ((vize * 25)/100) + ((final * 35)/100) + sunum + proje
    print("Donem sonu ortalamaniz ", ortalama,"'dir.")

if ortalama >= 50:
    print(ortalama," ortalama ile dersi gectiniz.")
else:
    print(ortalama," ortalam ile dersten kaldiniz.")