f = 1
n = int(input("Pozitif tam sayi degeri giriniz : "))

if n < 0:
    print("Negatif degerlerin faktoriyeli alinamaz.")
elif n == 0:
    print("0! 1'e esittir.")
else:
    i = 1
    list = []
    print("Girilen degere kadar olan sayilarin faktoriyelleri :")
    while i <= n :
        f = f * i
        list.append(f)
        i += 1
        print(f)
    print("Bulunan degerlerin toplami" , sum(list))

