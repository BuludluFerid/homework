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

shop = {
	"t-shirt" : 59.00,
	"jeans" : 75.00,
	"sweatshirt" : 60.00, 
	"shoe" : 124.99, 
	"jacket" : 154.90
	}

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
