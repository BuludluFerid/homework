'''Aşağıdakı ədədlərin tərsinə çevrilmiş hallarının cəmini alın. Əgər cəmin ilk rəqəmi təkdirsə
silinərək qalan hissə qaytarılmalı (məs, 532→32), əks halda isə 2 qatı ilə əvəzlənib geri qaytarılmalıdır (numeric data tipində).'''

# x = 124
# y = 651
# reverse_x = int(str(x)[::-1])
# reverse_y = int(str(y)[::-1])
# sum = reverse_x + reverse_y
# if (int(str(sum)[0]) % 2 == 1) :
#     print(int(str(sum)[1:]))
# else:
#     print(sum*2)
'''İstifadəçi 3 fərqli inputda adını, soyadını və ata adını daxil edir. Onun adı proqramda
ata adı böyük hərflərlə və ardından ad və soyadın baş hərfələrinin nöqtələrlə ayrılmış şəkildə qeyd olunmalıdır. Örnək:
Javier Bardem Pablo -> JAVIER B. P'''

# first_name = input("Adınızı daxil edin: ")
# last_name = input("Soyadınızı daxil edin: ")
# father_name = input("Ata adını daxil edin: ")


# father_name_initials = father_name.upper()
# first_initial = first_name[0].upper()
# last_initial = last_name[0].upper()

# name = f"{father_name_initials} {first_initial}. {last_initial}"
# print(name)

# 256.91872 ədədinin nöqtədən sonrakı və əvvəlki 2-ci ədədə qədər yuvarlaqlaşdırın. (2 fərqli cavab almalısınız)

# num = 256.91872
# print(round(256.91872,2))
# print(round(256.91872,-2))

# Verilən floatın tam hissəsinin neçə ədəddən ibarət olduğunu göstərən proqram hazırlayın. Bunun üçün input və print funksiyalarından istifadə edin.

# num = float(input("float ədədi daxil edin:"))
# int_part = int(abs(num))
# num_digits = len(str(int_part))
# print("Ədədin tam hissəsi ", num_digits, "rəqəmdən ibarətdir.")

'''İstifadəçi ID nömrəsini daxil edəcək. ID nömrə10 simvoldan ibarət olmalı,
Bunun ilk 3 hərfi hər hansı bir ölkənin qısaltması olmalı (məs, AZE, TUR, USA),
Həmin qısaltmalar böyük hərflə yazılan ingilis şriftləri olmalı,
Daha sonrakı 7 character isə ancaq rəqəmlərdən ibarət olmalıdır.'''

# id = input('ID-nizi daxil edin:')
# if len(id) == 10 :
#     if id.isascii() :
#         if id[:3].isupper() :
#             if id[3:].isnumeric():
#                 if id.isalnum() :
#                    print('Daxil etdiyiniz ID doğrudur')
#                 else :
#                    print('Daxil etdiyiniz ID yanlışdır')
#             else :
#                 print('Yanlız ilk 3 simvol hərf ola bilər')
#         else :
#             print('Hərflər böyüklə yazılmalıdır')
#     else:
#         print('ID-niz yanlız ingilis hərflərindən ibarət ola bilər')
# else :
#     print('İD-niz yanlız 10 simvoldan ibarət olmalıdır')
        
# -20-dən 20-ə qədər (20 daxil olmaqla) olan ədədlər arasından mənfi tək ədədləri, sıfırı və müsbət cüt ədələri print edin.
# for i in range(-20,21):
#        if i < 0 :
#        print (i)
#    elif i == 0 :
#        print (i)
#    elif i > 0 :
#        print(i)
# print('Bitdi')
       
# Verilmiş bir ədədin faktorialını hesablayın
# n = int(input("Ededi daxil edin :"))
# fakt = 1
# for i in range(1,n+1):
#     fakt *=i
# print(fakt)

# Verilmiş stringin içərsiində neçə ədəd n hərfi olduğunu göstərən kod yazın.
# sentence = 'Python is Number 1 programming language.'
# a = 0
# for i in sentence :
#     if sentence[i] == "n" or sentence[i] == "N":
#         a+=1
# print("nlerin sayi",a)

# Verilmiş stringdən indexi cüt sayda olan elementləri print edin.
# name_surname = "Rufet Quliyev"
# for i in range (len(name_surname)):
#     if i % 2 == 0:
#         print(name_surname[i])

# 1-dən 100-ə qədər olan ədədlər arasından verilmiş list içərisində 
# olmayanları print edin (və ya onların cəmini əldə edin)
# list = [2, 7 ,35 ,89 ,77]
# sum = 0
# for i in range (1,101):
#     if i not in list :
#         sum += i
# print(sum)

# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62] list içərisindəki ən böyük və ən kiçik ədədi dinamik şəkildə tapın.

# max = 0
# min = 0
# numbers.sort()
# min = numbers [0]
# max = numbers [-1]
# print(max,min)
# print(numbers)

# Aşağıda tələbələrin semestr nəticələri qeyd edilmişdir. Buna əsasən qeyd olunmuş statistik məlumatları
# eyni anda print edin.
#     1. Tələbə sayı
#     2. Ümumi ortalama.
#     3. Kəsilən tələbələrin ümumi faizi (51- qiymət alanlar)
#     4. Yüksək nəticə göstərən tələbələrin ümumu faizi (80+ qiytət alanlar)
# r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# telebe_sayi = 0
# kesilen_telebeler = 0
# kecen_telebeler = 0
# for i in r:
#     telebe_sayi += i
#     if i <51 :
#         kesilen_telebeler += 1
#     elif i>80 :
#         kecen_telebeler += 1
# umumi_ortalama = telebe_sayi/len(r)
# kesilen_telebe_faiz = (kesilen_telebeler*100)/len(r)
# kecen_telebe_faiz = (kecen_telebeler*100)/len(r)
# print("Umumi ortalama :",umumi_ortalama,"Kesilen telebelerin umumi faizi",kesilen_telebe_faiz,"Kecen telebelerin umumi faizi",kecen_telebe_faiz,"Telebelerin sayi:",len(r))

# İstifadəçinin girdiyi ədədi tək ədədlərdən ibarət tərsinə çevirilmiş list şəklinə salın.
# Listin bütün elementlərinin integer olmasına diqqət edin. Örnək:
# input: 834255
# output: [5, 5, 2, 4, 3, 8]
# n = input("Ededi daxil edin:")
# reverse_n = n[::-1]
# l = []
# for i in reverse_n:
#     if int(i) % 2:
#         l.append(int(i))
# print(l)

# 1-dən 100-ə kimi olan bütün ədədlərin toplamını tapın (1+2+3+...+99+100)

# for dövrü ilə

# sum = 0
# for i in range(1,100):
#     sum += i
# print(sum)

# while dövrü ilə

# sum = 0
# number = 1
# while number < 100:
#     sum += number
#     number += 1
# print(sum)

# 100000-dən aşağı doğru gedərək 9999-a bölünən ilk ədədi konsolda göstərin.

# for dövrü ilə

# for i in range (100000,1,-1):
#     if i % 9999 ==0 :
#        print(i)
#        break

# while dövrü ilə

# number = 100000
# while number <= 100000 :
#     if number % 9999==0 :
#        print(number)
#        break
#     number -= 1
        

# 'Men her gun Python oyrenirem’ bu stringin saitlər çıxarılmış vəziyyətini konsolda göstərin.

# for dövrü ilə

# sentence = 'Men her gun Python oyrenirem'
# saitler = 'aeiouAIOUE'

# new_sentence= ''

# for i in sentence:
#     if i not in saitler:
#         new_sentence += i
# print(new_sentence)

# while dövrü ilə

# sentence = 'Men her gun Python oyrenirem'
# saitler = 'aeiouAEIOU'

# new_sentence = ''
# i = 0

# while i < len(sentence):
#     if sentence[i] not in saitler:
#         new_sentence += sentence[i]
#     i += 1
# print(new_sentence)

# İstifadəçinin daxil etdiyi cümlədə neçə heca olduğunu deyən program hazırlayın.

# sentence = input('Cümleni daxil edin:')
# heca_sayı = 0
# saitler = 'aioueAIOUE'
# for i in sentence :
#     if i in saitler:
#         heca_sayı += 1
# print ('hecaların sayı :',heca_sayı)

# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci'] şəklində fermaya sahib bir fermer bizdən bəzi köməkliklər istəyir. Fermerə kömək etmək üçün aşağıdakı tapşırıqları yerinə yetirin.

# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']

# a) Fermada keçinin sırasını tapın

# print(ferma.index('keci'))

# b) Fermadakı heyvanları ad sırasına görə sıralayın

# ferma_sorted = sorted(ferma)

# print(ferma_sorted)

# c) Fermadan bir at çıxarıb, ən sağdan bir toyuq əlavə edin

# ferma.pop(3)
# ferma.append('toyuq')
# print(ferma)

# d) Ən soldan bir keci əlavə edin

# ferma.insert(0,'keci')
# print(ferma)

# e) Fermanın yarısını dinamik bir şəkildə silin

# del ferma[len(ferma)//2:]

# print(ferma)

# f) Yeni gələn ['at', 'qoyun', 'inek', 'inek', 'qoyun'] heyvanları fermaya əlavə edin

# new_animals = ['at', 'qoyun', 'inek', 'inek', 'qoyun']
# ferma.extend(new_animals)
# print(ferma)

# g) Fermadakı heyvanları 3 qatına çıxarın

# ferma *= 3
# print(ferma)

# h) Fermadakı heyvanları tərsinə sıralayın

# ferma.reverse()
# print(ferma)

# i) Fermadakı inəklərin sayının ümumi fermanın neçə faizi olduğunu tapın

# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']
# inek_sayi= ferma.count('inek')
# umumi_heyvanlar = len(ferma)
# ineklerin_faizi = (inek_sayi / umumi_heyvanlar) * 100


# print(f"Fermadakı ineklerin sayının ümumi fermaya görə faizi : {ineklerin_faizi}%")

# j) Oxşar fermadan istəyən basqa bir fermerə fermamızın kopyasını verini

# ferma.copy()
# print(ferma)

# k) Fermadan heyvanları çıxarın

# ferma.clear()
# print(ferma)

# Aşağıdakı result listinin 0-cı indexinə numbers listi daxilindəki müsbət ədədlərin cəmini, 1-ci indexə isə mənfi ədədlərin cəmini yerləşdirin. 

# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]

# for i in numbers :
#     if i>=0 :
#         result[0]+= i
#     if i<=0 :
#         result[1]+= i
# print(result)


''' Listin içərisindəki ədədlərin rəqəmlərinin cəmindən ibarət bir list hazırlayın. Örnək:
[3587, 2454, 19305, 17, 33, 42, 427, 317] - > [23, 15, 18, 8, 6, 6, 13, 11] '''

# list = [3587, 2454, 19305, 17, 33, 42, 427, 317] 
# digit_sums = []

# for num in list :
#     digits = [int(digit) for digit in str(num)]
#     digit_sums.append(sum(digits))
# print(digit_sums)

'''Verilmiş listin içərisindən 0, None, False, boş string, boş list kimi dataları çıxarın.'''

# data = ['Python', ' ', 0, 0.0, [], 256, None, 'Coding', 0.256, True, 598, [1, 2, 3], [None]]   
 
# for i in data :
#     if i  :

# print(new_data)


'''Verilmiş listdən heç bir elementin təkrarlanmadığı yeni bir list yaradın.'''
    
# numbers = [256, 35, 14, 48, 49, 57, 57, 65, 256, 65, 48, 2, 3, 14, 54, 56, 56, 349]
# new_list = []
# for i in numbers :
#     if i not in new_list :
#         new_list.append(i)
# print(new_list)

'''Listin ən böyük və ən kiçik elementlərindən başqa bütün elementlərinin cəmini əldə edin.'''

# numbers = [6, 2, 1, 8, 10,]

# toplam = sum(numbers) - min(numbers) - max(numbers)

# print(toplam)


   
        
user = {
    'name': 'Elnur',
    'height': 179,
    'phone': {
        'model': 'Iphone',
    },
    'orders': ['book', 'mouse', 'mousepad']
}

'''Aşağıdakıları terminalda göstərin:'''

# a) İstifadəçinin boyunu artırın

# user['height'] = '185'

# print(user)

# b) Telefonun markasını dəyişərək Samsung edin

# user['phone']['model'] = 'Samsung'

# print(user)

# c) İstifadəçinin adını silin

# del user['name']
# print(user)

# d) İstifadəçinin ilk sifarişini silin

# del user['orders'][0]
# print(user)

# e) İstifadəçinin sifarişlərinin başına ball əlavə edin

# f) Sonuna headphones əlavə edin


''' Aşağıdakı fake dataya əsasən login sistemi qurun.'''

# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]

# username = input('İstifadəçi adınızı daxil edin: ')
# password = input('Şifrənizi daxil edin: ')

# for user in users:
#     if user['username'] == username:
#         if user['blocked']:
#             print('Siz daxil ola bilməzsiniz')
#         elif user['password'] == password:
#             print(f"{user['name']}, giriş etdiniz")
#         else:
#             print('Şifrəniz yanlışdır')
#         break
# else:
#     print('Belə bir istifadəçi yoxdur')






        
        
        













