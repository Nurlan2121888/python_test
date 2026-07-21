# task1

# melumat = {
#     "ad": "Nurlan",
#     "yas": 22,
#     "seher": "Baki"
# }

# secim = input("Daxil edin (1 - Keys, 2 - Values): ")

# if secim == "":
#     print("Məlumat daxil etmədiniz")

# elif secim == "1":
#     print(melumat.keys())

# elif secim == "2":
#     print(melumat.values())

# else:
#     print("Yanlış seçim")



# task2

# sozler = []

# for i in range(10):
#     soz = input(f"{i+1}-ci sözü daxil edin: ")
#     sozler.append(soz)

# unikal = set(sozler)

# saylar = {}

# for soz in sozler:
#     if soz in saylar:
#         saylar[soz] += 1
#     else:
#         saylar[soz] = 1

# print("List:")
# print(sozler)

# print("Set:")
# print(unikal)

# print("Dictionary:")
# print(saylar)



# task3

# mehsullar = {}

# for i in range(5):
#     ad = input("Məhsul adını daxil edin: ")
#     qiymet = int(input("Qiyməti daxil edin: "))

#     mehsullar[ad] = qiymet

# axtar = input("Axtarmaq istədiyiniz məhsulu daxil edin: ")

# if axtar in mehsullar:
#     print("Qiyməti:", mehsullar[axtar])
# else:
#     print("Məhsul tapılmadı")

# task4

# students = {
#     "Ali": 85,
#     "Veli": 42,
#     "Murad": 91,
#     "Aysel": 58,
#     "Nigar": 100
# }

# yuksek_ballilar = {}

# for ad, bal in students.items():
#     if bal > 60:
#         yuksek_ballilar[ad] = bal

# print(yuksek_ballilar)

# task5

# telebe1 = {
#     "ad": "Ali",
#     "yas": 20,
#     "seher": "Baki",
#     "bal": 85
# }

# telebe2 = {
#     "ad": "Murad",
#     "yas": 21,
#     "seher": "Sumqayit",
#     "bal": 91
# }

# telebe3 = {
#     "ad": "Nigar",
#     "yas": 19,
#     "seher": "Gence",
#     "bal": 95
# }

# print(telebe1)
# print(telebe2)
# print(telebe3)




# task6

# user1 = {"Ali", "Murad", "Samir", "Aysel"}
# user2 = {"Murad", "Nigar", "Ali", "Leyla"}

# ortaq = user1 & user2
# print(ortaq)



# task7

users = {
    "admin": "12345",
    "user": "11111",
    "guest": "22222"
}

login = input("Login daxil edin: ")
parol = input("Parol daxil edin: ")

if login in users and users[login] == parol:
    print("Xoş gəldiniz")
else:
    print("İstifadəçi adı və ya parol yanlışdır")


