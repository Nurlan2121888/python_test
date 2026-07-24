# task1
# def hesabla(a, b, emeliyyat):

#     if emeliyyat == "+":
#         return a + b

#     elif emeliyyat == "-":
#         return a - b

#     elif emeliyyat == "*":
#         return a * b

#     elif emeliyyat == "/":
#         return a / b

#     else:
#         return "Yanlış əməliyyat!"


# birinci = int(input("Birinci ədədi daxil edin: "))
# ikinci = int(input("İkinci ədədi daxil edin: "))
# emeliyyat = input("Əməliyyatı daxil edin (+, -, *, /): ")

# netice = hesabla(birinci, ikinci, emeliyyat)

# print(netice)

# task2

# def maas_hesabla(saatliq, saat):
#     if saat > 40:
#         normal = 40 * saatliq
#         artiq = (saat - 40) * saatliq * 1.5
#         return normal + artiq

#     else:
#         return saat * saatliq

# saatliq = int(input("Saatliq emekhaqqini daxil edin: "))
# saat = int(input("Is saatini daxil edin: "))

# print("Yekun maas: ", maas_hesabla(saatliq, saat))

# task3

# def sifreni_yoxla(sifre):
#     boyuk = False
#     kicik = False
#     reqem = False
    
#     if len(sifre) < 8:
#         return "Zeif Sifre"
#     for herf in sifre:
#         if herf.isupper():
#             boyuk = True
#         elif herf.islower():
#             kicik = True
#         elif herf.isdigit():
#             reqem = True
            
#     if boyuk and kicik and reqem:
#         return "Guclu sifre"
#     else:
#         return "Zeif sifre"
    
# sifre = input("Sifreni daxil edin: ")
# print(sifreni_yoxla(sifre))

# task4

# def endirim(qiymet, musteri):

#     if musteri == "Gold":
#         faiz = 20

#     elif musteri == "Silver":
#         faiz = 10

#     elif musteri == "Bronze":
#         faiz = 5

#     else:
#         faiz = 0

#     endirim_meblegi = qiymet * faiz / 100
#     son_qiymet = qiymet - endirim_meblegi

#     return faiz, endirim_meblegi, son_qiymet


# qiymet = float(input("Məhsulun qiymətini daxil edin: "))
# musteri = input("Müştəri tipini daxil edin (Gold, Silver, Bronze): ")

# faiz, endirim_meblegi, son_qiymet = endirim(qiymet, musteri)

# print("Endirim faizi:", faiz, "%")
# print("Endirim məbləği:", endirim_meblegi)
# print("Ödəniləcək məbləğ:", son_qiymet)

# task5
def kino_bileti(yas, telebedir):

    if yas < 12:
        qiymet = 6

    elif yas >= 65:
        qiymet = 8

    else:
        qiymet = 12

    if telebedir == True:
        endirim = qiymet * 20 / 100
        son_qiymet = qiymet - endirim
    else:
        endirim = 0
        son_qiymet = qiymet

    return qiymet, endirim, son_qiymet


yas = int(input("Yaşı daxil edin: "))
telebe = input("Tələbəsiniz? (True/False): ")

if telebe == "True":
    telebe = True
else:
    telebe = False

qiymet, endirim, son_qiymet = kino_bileti(yas, telebe)

print("Bilet qiyməti:", qiymet, "AZN")
print("Endirim:", endirim, "AZN")
print("Ödəniləcək məbləğ:", son_qiymet, "AZN")