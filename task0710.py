# task1
# ededler = []

# ededler.append(int(input("1-ci ədədi daxil edin: ")))
# ededler.append(int(input("2-ci ədədi daxil edin: ")))
# ededler.append(int(input("3-cü ədədi daxil edin: ")))

# ededler.sort()

# en_kicik = ededler[0]
# en_boyuk = ededler[2]

# ededler.remove(en_kicik)
# ededler.remove(en_boyuk)

# netice = tuple(ededler)

# print(netice)

# task2
# ededler = [5, 8, 2, 1, 5, 9, 2, 6, 1, 8]

# ededler = list(set(ededler))
# ededler.sort()

# netice = tuple(ededler)

# print(netice)

# task 3

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# list1.extend(list2)
# list1.pop(0)
# list1.pop(0)
# list1.pop(0)

# list1.pop(-1)
# list1.pop(-1)
# print(list1)

# task4 (arasirib yazmisam)
# adlar = []

# while True:
#     ad = input("Ad daxil edin: ")

#     if ad == "stop":
#         break

#     adlar.append(ad)

# unikal = []

# for ad in adlar:
#     if ad not in unikal:
#         unikal.append(ad)

# print("Unikal adlar:", unikal)
# print("Unikal adlarin sayi:", len(unikal))

# task5

# ededler = [12, 4, 8, 15, 20, 7, 10, 5]

# cutler = []
# tekler = []

# for eded in ededler:
#     if eded % 2 == 0:
#         cutler.append(eded)
#     else:
#         tekler.append(eded)
        
# print("cut ededler:", cutler)
# print("tek ededler", tekler)

# task6 (arasdirib yazmisam)

# import random

# ededler = []

# for i in range(10):
#     ededler.append(random.randint(1, 100))
    
# print(ededler)

# maksimum = max(ededler)
# minimum = min(ededler)

# orta = sum(ededler) / len(ededler)

# cut_say = 0
# tek_say = 0

# for eded in ededler:
#     if eded % 2==0:
#         cut_say += 1
#     else:
#         tek_say += 1
# print("maksimum:", maksimum)
# print("minimum:", minimum)
# print("orta qiymet", orta)
# print("cut sayi:", cut_say)
# print("tek sayi:", tek_say)

# task7

# tuble1 = (1, 2, 3, 4)
# tuble2 = (5, 6, 7, 8)

# list1 = list(tuble1)
# list2 = list(tuble2)

# list1.extend(list2)

# list1.sort()

# netice = tuple(list1)

# print(netice)

# task8

# ededler= []

# for i in range (1, 101):
#     ededler.append(i)
    
# besler = []
# qalanlar = []

# for eded in ededler:
#     if eded % 3 == 0:
#         continue
#     elif eded % 5 == 0:
#         besler.append(eded)
#     else:
#         qalanlar.append(eded)
    
# netice = tuple(qalanlar)

# print("5-e bolunenler:", besler)
# print("qalanlar:", netice)

# task9

# melumatlar = [10, 5.5, "salam", True, 25, 3.13, "python", False]

# integerler = []

# for element in melumatlar:
#     if type(element) == int:
#         integerler.append(element)
        
# print(integerler)    