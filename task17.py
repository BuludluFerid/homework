'''Kürə və koni həcmlərini tapan funksiyalar hazırlayın'''
# import math

# def kürə_həcmi(radius):
    
#     həcim = (4/3) * math.pi * radius**3
#     return həcim

# def koni_həcmi(radius, height):

#     həcim = (1/3) * math.pi * radius**2 * height
#     return həcim

'''Permutasiya və kombinasiya tapan funksiyalar hazırlayın.'''

# import math

# def permutasiya(n, r):
    
#     permutasiya_sayi = math.factorial(n) / math.factorial(n - r)
#     return permutasiya_sayi

# def kombinasiya(n, r):
    
#     kombinasiya_sayi = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
#     return kombinasiya_sayi

'''Giveaway programi duzeldin. Adamlar bitənə qədər hər enter basanda bir ad göstərsin. '''

# import random

# def giveaway(adlar):
#     for ad in adlar:
#         input("Davam etmək üçün ENTER basın")
#         print(ad)
#     print("Giveaway bitdi.")

# adlar = input("Adları daxil edin: ").split(",")
# giveaway([ad.strip() for ad in adlar])

''' Ədəd təxmin etmə oyunu hazırlayın. Müəyən bir araılq verin 
və program həmin aralıqda bir ədəd təyin etsin. Daha sonra siz 
həmin ədədi tapana qədər oyun davam etsin. Siz gizli ədədin aşağısında 
bir təxmin etdikdə program daha yuxarı, yuxarısında təxmin etdikdə isə 
daha aşağı desin. Ən sonda ədədi neçə səfərə tapdığınızı qeyd etsin. 
Əgər 10 üzərində təxmin etdikdən sonra tapıbsızsa məğlub sayılırsız, 
əks təqdirdə qalib.'''

# import random

# def təxmin_oyunu(aralıq):
#     gizli_ədəd = random.randint(aralıq[0], aralıq[1])

#     tahmin_edildi = False
#     cəhdlər_sayı = 0

#     for cəhd in range(10):
#         cəhdlər_sayı += 1
#         tahmin = int(input("Təxmininizi edin: "))

#         if tahmin < gizli_ədəd:
#             print("Daha yuxarı!")
#         elif tahmin > gizli_ədəd:
#             print("Daha aşağı!")
#         else:
#             tahmin_edildi = True
#             break

#     if tahmin_edildi:
#         print(f"Təbriklər! Gizli ədədi {cəhdlər_sayı} cəhdlərdə tapdınız.")
#     else:
#         print(f"Mağlub oldunuz! Gizli ədəd {gizli_ədəd} idi.")

# aralıq = (1, 20)
# təxmin_oyunu(aralıq)

''' “Saat 17:00, 04.06.2022 tarixində dərsə gəlin” cümləsindən istifadə edərək tarixi datetime formatına çevirin. '''
# from datetime import datetime

# cumle = "Saat 17:00, 04.06.2022 tarixində dərsə gəlin"

# format_str = "Saat %H:%M, %d.%m.%Y tarixində dərsə gəlin"

# tarih = datetime.strptime(cumle, format_str)

# print(tarih)








