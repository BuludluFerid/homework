# card_number = '5382-1739-9201-9017'
# s=card_number[:8].ljust(len(card_number),'*')
# print(s)
# number = '34'
# s = number.zfill(len(number)+3)
# print(s)
# web_site = 'http://google.com'
# s = input("Saytı daxil edin").rstrip('.com')
# l = input("Saytı daxil edin").lstrip('htp:/')
# print(s,l)
# a=input("Kodu daxil edin")
# if 8 < len(a) < 40 :
#     if a.isascii() :
#         if a.isalnum() :
#             print("Daxil etdiyiniz sifre dogrudur")
#         else :
#             print("Sifrede yanliz herf ve ya reqemlerden ibaret olmalidir")
#     else:
#         print("Sifre yanliz ingilis herflerinden duzeldile biler")
# else:
#     print("ya 8-den kicikdir ,ve ya 40-dan boykdur")
# a = input("Nömrəni daxil edin: ")
# if a.startswith('+994'):
#     if len(a)==13:
#         if a.removeprefix('+').isnumeric():
#             print("Nomre duzgun daxil edilib")
#         else:
#             print('nomre yanliz ededlerden ibaret olmalidir')
#     else:
#         print("13 ededden ibaret olmalidir")
# else:
#     print("+994 baslamalidir")
# text = "Salyut 1 kosmosa göndərilən ilk kosmik stansiya idi. O, 1971-ci ilin aprelində Sovet İttifaqı tərəfindən orbitə buraxılıb və 1971-ci ilin oktyabr ayına qədər kosmosda qaldı. Kosmosda olduğu müddətdə onu ekipajlarla birlikdə iki kosmik gəmi ziyarət etdi. Salyut 1-in məqsədi kosmik stansiyanın necə işlədiyini öyrənmək və sınaqdan keçirmək idi. İkinci məqsəd kosmosda uzun müddət qalmağın insan orqanizminə necə təsir etdiyini öyrənmək idi. Onun bir sıra problemləri var idi, lakin ondan gələcək stansiyalara kömək edən çox şey öyrənildi."
# print('kömək'in text and 'həyat'in text and 'sınaq'in text )
# word = text.index('kosmos')
# last_word = text.rindex('kosmos')
# print(word,last_word)
# print(text.startswith("Salyut")and text.endswith("ildi."))

# 1.  Listin bütün elementlərini yoxlayın, hər hansı bir ədəd 1 və ya 2 ilə başlayıb 0 və ya 9 ilə bitmirsə onu çıxarıb yeni bir listə əlavə edin. Misal:
# [256, 120, 2379, 135, 349, 159] -> [256, 135, 349]

# list = [256, 120, 2379, 135, 349, 159]
# new_list = []

# for i in list:
#     if not((str(i)[0] == '1' or str(i)[0] == '2') and (str(i)[-1] != '0' and str(i)[-1] != '9')):
#         new_list.append(i)

# print(new_list)


# 2. İstifadəçi iki ədəd daxil edəcək (num, rep). Daxil edilmiş ədədlərə uyğun aşağıdakı kimi hesablama aparan kod yazın. Örnəklər:
# num = 2
# rep = 5
# 2 + 22 + 222 + 2222 + 22222

# num = 4
# rep = 5
# sum = 0

# for i in range(1,rep+1) :
#     sum += int(str(num)*i)
# print (sum)

# 1-100 arası ədədləri 3 və 5 vahid artıraraq print edin (1, 4, 9, 12, 17, 20, 25, 28, 31, 36...)

# c = 1
# while c < 100:
#     print(c)
#     print(c+3)
#     c += 8 

# Verilmiş listin içərisində olan sadə ədələrdən yeni bir list yaradın.
# numbers = [25, 7, 12, 58, 35, 33, 24, 14, 3, 10, 9, 11, 23, 31]

# new_list = []

# for new_list in numbers :
#     check_number = 0
#     for i in range(2,10):
#         if new_list != i  and new_list % i ==0:
#             check_number += 1
#     if check_number == 0 :
#         new_list.append(i)
# print(new_list)

# for i in range (1,6):
#     print ('*'* i)

# data = ['Ferid', 'Rufet', 123, 250.5, False, [1, 3, 5], None, 0]

# data_type = []
# for info in data :
#     data_type = str(type(info))
#     data_type = data_type[data_type.index("'")+1:data_type.rindex("'")]
#     data_and_type = str[info]
#     print(data_type)


''' 2.  İstifadəçinin girdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın.'''   
'''Input: This is an example! '''

# sentence = input("Enter a sentence: ")
# sentence_2 = sentence.split(" ")
# new_list = []
# for i in sentence_2 :
#     new_list.append(i[::-1])
# print(new_list)
# a = " " . join(new_list)
    
# reversed_sentence = " ".join(new_list)
    
'''3. info = ["Resul", "Serifov", 35]`

Yuxarıdakı listi dinamik olaraq `["Resul Serifov", 25]` vəziyyətinə gətirin.'''

# info = ["Resul", "Serifov", 35]

# full_name = " ".join(info[:2])

# age = info[-1] - 10
# info = [full_name, age]

# print(info)


'''4. Aşağıdakı datada məhsulların ad və qiymətləri qeyd olunmuşdur.'''

# shop = {
# 	"t-shirt" : 59.00,
# 	"jeans" : 75.00,
# 	"sweatshirt" : 60.00, 
# 	"shoe" : 124.99, 
# 	"jacket" : 154.90
# 	}

'''Dictionary əsasən istifadəçi sizə məhsul adı girəcək. Bu məhsulun mağazada olan qiymətini göstərən proqram hazırlayın. Girilən məhsul mağaza da olmadığı halda "None" qaytarın.'''

# product = input ("Mehsulu daxil edin")

# print(shop.get(product, None))

    
'''Mağazaya yeni məhsullar və qiymətlərini əlavə edin.'''

# new_product = {
#     " shoes" : 55.00,
# }
# shop.update(new_product)
# print(shop)

'''Mağazada nə qədər məhsul olduğunu göstərin'''

# print(len(shop))

'''Verilmiş dictionary-də positionu front-end developer olan işçilərin iş saatlarını 

- 5 saat artırın, iş təcrübəsi ən az 2 il olan işçilərin maaşını 10% artırın, 
- Back-end developerlərin maaşını 12% artırın. 
- İş təcrübəsi ən az 1 il olan dizaynerlərin maaşını isə 5% artırın'''

# employees = {
#     'Ali Aliyev': {
#         'position': 'front-end developer',
#         'salary': '1800 AZN',
#         'work experience': '2 years', 
#         'working hours': 30
#     },
#     'Gunel Rzayeva': {
#         'position': 'front-end developer',
#         'salary': '900 AZN',
#         'work experience': '3 months', 
#         'working hours': 25 
#     },
#     'Nargiz Mahmudova': {
#         'position': 'back-end developer',
#         'salary': '2300 AZN',
#         'work experience': '3 years', 
#         'working hours': 40
#     },
#     'Ruslan Aghayev': {
#         'position': 'back-end developer',
#         'salary': '2000 AZN',
#         'work experience': '2 years', 
#         'working hours': 40
#     },
#     'Aslan Mammadov': {
#         'position': 'UI/UX designer',
#         'salary': '800 AZN',
#         'work experience': '6 months', 
#         'working hours': 30
#     },
#     'Rena Qasimova': {
#         'position': 'UI/UX designer',
#         'salary': '1100 AZN',
#         'work experience': '1 years', 
#         'working hours': 30
#     }
# }

# for employee, data in employees.items():
#     if data['position'] == 'front-end developer':
#         data['working hours'] += 5
#         if 'years' in data['work experience'] and int(data['work experience'][0]) >= 2:
#             data['salary'] = str(int(data['salary'].split()[0]) * 1.1) + ' AZN'
# employees = {employee: data for employee, data in employees.items() if data['position'] != 'deleted'}

# print(employees)

'''Istifadəçi sizə "5 salam" şəklində solda ədəd, ortada, boşluq, sağda isə bir input verəcək. Buna əsasən sağdakı yazını istifadəçinin qeyd etdiyi ədəd qədər yazıb, istifadəçiyə qatarın. Örnək yuxaridakı inputun outputu salam salam salam salam salam '''
           


'''[2384, 12385, 13226, 653, 12362423] list içərisindəki ədədlərin key olduğu və value-ların həmin ədədlərin rəqəm sayı olduğu bir dictionary hazırlayın'''

# numbers = [2384, 12385, 13226, 653, 12362423]

# num_dict = {num: len(str(num)) for num in numbers}

# print(num_dict)

'''-100-dən müsbət 100-ə qədər ədədlər arasında 7-yə bölünən ədədlərin 3-ə vurulmasından ibarət bir list qurun. Bunun üçün range və list comprehensions istifadə edin.'''

# result = [num * 3 for num in range(-100, 101) if num % 7 == 0]

# print(result)

# qiymetler = {'Nescafe 500 gr': 8, 'Tess 350 gr': 4.5, 'Jacobs 500 gr': 9.5, 'Cappucino J': 6.4}
# mehsullar = ['Nescafe 500 gr', 'Jacobs 500 gr']
# vergi_faizi = 0.08

# total_price = 0
# for k,v in qiymetler.item():
#     if k in mehsullar:
#         total_price += v 
# vergi = total_price + total_price *vergi_faizi
# print(vergi)

'''bu listdən yeni bir dictionary hazırlayın. Həmin dictionarynin keyləri ədədlər, valueləri isə mübət və ya mənfi yazılı stringlər olacaq.
Ornək: {10: 'tek', -21: 'cut', ...}'''

# numbers = [58, 78, 96, 33, 25, 29, 12, 46]
# res = {n: ('cüt' if n % 2== 0 else 'tək') for n in numbers}
# print(res)

'''Aşağıdakı listdən istifadə edərək qrammatik səhvi düzəldib print edin'''

# cumle = "sehvelerden en yaxsi sehife bu sehvedir"
# l = ["sehve", "sehife"]
# result = cumle.replace(*l)
# print(result)


# for i in range(30):
#     bin_num = bin(i)[2:]
#     oct_num = oct(i)[2:]
#     hex_num = hex(i)[2:]
#     print("{:<10}{:<10}{:<10}{:<10}".format(i, bin_num, oct_num, hex_num))

'''
Verilmiş stringin sözlərindən bir hashtag yaradan kod yazın. 
Cümləni hashtag-a çevirərkən Azərbaycan şriftləri ingilis şriftləri 
ilə əvəz olunmalıdır (Bütün hərflər nəzərə alınmalıdır) və hashtag 
camelcase ilə yazılmalıdır. Örnək:
'''

# sentence_1 = "Heyvanlara qaygı mərkəzi"
# words = {
#         'ə': 'e',
#         'ü': 'u',
#         'ö': 'o',
#         'ı': 'i',
#         'ğ': 'g',
#         'ş': 's',
#         'ç': 'c',
#     }
# def replace_letters(sentence):
#     for k,v in words.items():
#         if k in sentence:
#             sentence = sentence.replace(k,v)
#     return sentence
# print(replace_letters(sentence_1))


'''
Lambda ilə factorial hesablayan recursive function hazırlayın.
'''

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print((lambda n: factorial(n))(4))

'''
Aşağıdakı ədədlər arasında rəqəmlərinin cəmi ən yüksək olanı çıxarın.
85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400
'''

# def get_digit_sum(n):
#     digits = [int(d) for d in str(n)]
#     return sum(digits)

# numbers = [85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400]

# max_number = max(numbers, key=get_digit_sum)

# print(max_number)


'''
Aşağıdakı dataları tiplərinə görə sıralamaq lazımdır. Sıra bu şəkildə olacaq: Listlər, Dictonarylər, Booleanlar, İntegerlər, Floatlar, Stringlər.
[{'a': 1, 'b': 2}, 5, 7.8, 'asdf', 23, ['a', 'b'], True,  False]
'''

# item = [{'a': 1, 'b': 2}, 5, 7.8, 'asdf', 23, ['a', 'b'], True, False]

# types = {list: 1, dict: 2, bool: 3, int: 4, float: 5, str: 6}

# sorted_data = sorted(item, key=lambda x: types[type(x)])

# print(sorted_data)






