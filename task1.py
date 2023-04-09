
# user_info = {
#     'firstname': 'Elvin',
#     'lastname': 'Huseynov',
#     'username': 'elivin_h_ov',
#     'password': '12345',
#     'birthday': '19-08-1997'
# }
# new_user = input('Yeni mılumatları daxil edin :')
# for i in new_user.split(', '):
#     c,d = i.split()
#     for k,v in user_info.items():
#         if c == k:
#             user_info[k] = d
# print(user_info)

# mehsullar = [["Samsung A7", 55], ["Iphone 5"], ["Xiaomi 5879", 158], ["Iphone 13", 98], ["Iphone 14", 0]]


# yeni_mehsullar = {}

# for mehsul in mehsullar:
#     if len(mehsul) == 1 :
#         yeni_mehsullar[mehsul[0]] = None
#     elif mehsul[1] == 0:
#         yeni_mehsullar[mehsul[0]] = "Sold out"
#     else :  
#         yeni_mehsullar[mehsul[0]] = mehsul[1]            
# print(yeni_mehsullar)

# n = int(input("Eded daxil edin: "))

# total = 0
# for i in range(1, n*3, 3):
#     total += 1/i
#     total = round(total,2)

# print(total)

# cumle = input('cumleni daxil edin:')
# cumle = cumle.lower()
# words = {
#         'ç' : 'c',
#         'ə' : 'e',
#         'ğ' : 'g',
#         'ı' : 'i',
#         'ö' : 'o',
#         'ş' : 's',
#         'ü' : 'u',
# }
# for k,v in words.items():
#    if k in cumle:
#        cumle = cumle.replace(k,v)
# hastag = '#'
# for i in cumle.title().split():
#     hastag += i
# print(hastag)

# dictionary = {
#   'ə': 'e',
#   'ı': 'i',
#   'ö': 'o',
#   'ü': 'u',
#   'ş': 's',
#   'ç': 'c',
#   'ğ': 'g',
# }
# result = []
# for k,v in dictionary.items():
#     result = list(dictionary.items())
# print(result)

# l = [['toddler_age', (1, 5)], ['kid_age', (5, 13)], ['teen_age', (13, 17)], ['young_age', (17, 30)], ['adult_age', (30, 'and more')]]

# new_l = {}

# for item in l:
#     new_l_range = item[0]
#     new_l_limits = item[1]
#     if new_l_limits[1] == 'and more':
#         age_range_str = str(new_l_limits[0]) + '+'
    

       
    
   


