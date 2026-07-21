# task1

# say = int(input("Neçə ədəd daxil edəcəksiniz: "))

# cem = 0

# for i in range(say):

#     eded = int(input("Ədəd daxil edin: "))

#     while eded < 0:
#         print("Mənfi ədəd daxil etdiniz.")
#         eded = int(input("Yenidən müsbət ədəd daxil edin: "))

#     cem += eded

# print("Cəm:", cem)

# task2

# ?

# task3

# sagird_sayi = int(input("nece sagird var: "))

# for i in range(sagird_sayi):
#     ad = input("Sagirdin adi: ")
#     q1 = int(input("1-ci qiymet: "))
#     while q1 < 0 or q1 > 100:
#         q1 = int(input("Yeniden daxil edin: "))
        
#     q2 = int(input("2-ci qiymet: "))
#     while q2 < 0 or q2 > 100:
#         q2 = int(input("Yeniden daxil edin: "))
        
#     q3 = int(input("3-cu qiymet: "))
#     while q3 < 0 or q3 > 100:
#         q3 = int(input("Yeniden daxil edin: "))
    
#     orta = (q1 + q2 + q3) / 3
    
#     print("ad:", ad)
#     print("orta bal:", orta)
    
#     if orta >= 60: 
#         print("kecib")
#     else:
#         print("kesilib")

# task4

# ededler = []
# cem = 0

# for i in range(10):
#     eded = int(input("Ədəd daxil edin: "))
#     ededler.append(eded)

# for eded in ededler:
#     cem += eded

# print("Cəm:", cem)

# task5

# sozler = []

# for i in range(6):
#     soz = input("Söz daxil edin: ")
#     sozler.append(soz)

# for soz in sozler:
#     print(soz, "->", len(soz))


# task6

# sozler = []

# for i in range(5):
#     soz = input("Söz daxil edin: ")
#     sozler.append(soz)

# baslayir = 0
# bitir = 0
# uzundur = 0

# for soz in sozler:

#     if soz.startswith("a"):
#         baslayir += 1

#     if soz.endswith("a"):
#         bitir += 1

#     if len(soz) > 5:
#         uzundur += 1

# print("'a' ilə başlayan sözlərin sayı:", baslayir)
# print("'a' ilə bitən sözlərin sayı:", bitir)
# print("Uzunluğu 5-dən böyük olan sözlərin sayı:", uzundur)

# task7

sozler = []
boyuk_sozler = []

for i in range(5):
    soz = input("Söz daxil edin: ")
    sozler.append(soz)

for soz in sozler:
    boyuk_sozler.append(soz.upper())

print(boyuk_sozler)
