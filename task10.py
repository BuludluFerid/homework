'''
Daxil edilən stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın.
upunion('birlesmis', 'milletler', 'teskilati') => 'BMT
'''
# def upunion(*sentence):
#     result = ''
#     for i in sentence:
#         result += i[0].upper()
#     return result
# print(upunion('birlesmis', 'milletler', 'teskilati'))

'''
Verilmiş ədədləri tərsinə çevirib toplayan bir funksiya hazırlayın
'''
# def getReversedSum(*numbers):
#     result = 0
#     for n in numbers:
#         result += int(str(n)[::-1])
#     return result

# print(getReversedSum(123, 567, 562))
'''
Daxil edilmiş listin ən böyük ədədindən ən kiçiyini çıxarıb, nəticə verən bir funksiya hazırlayın. 
'''
# def big_dif_sml(numbers):
#     numbers.sort() 
#     return numbers[-1] - numbers[0]  
# print(big_dif_sml([6, 3, 8, 9, 2]))
'''
Birinci arqument ilk qiyməti, ikinci arqument isə yeni qiyməti göstərir. Yeni qiymətin ilkindən neçə faiz fərqləndiyini print edən funksiya düzəldin.
'''
# def find_percent(old_value, new_value):
#     if new_value > old_value:
#         percent = (new_value - old_value) / old_value * 100
#         print(f"Qiymət {percent:.0f}% artmışdır.")
#     elif new_value < old_value:
#         percent = (old_value - new_value) / old_value * 100
#         print(f"Qiymət {percent:.0f}% azalmışdır.")
#     return percent
# print(find_percent(200, 60))  
'''
Daxil edilən stringi qeyd edilən şəkildə dəyişən bir funksiya hazırlayın:
'''
# sentence = 'Kitabi sehve-sehve oxumalisan ki, orgenesen'
# def chstr (cumle):
#     dic = {'sehve': 'sehife',
#        'orgenesen': 'oyrenesen'}
#     for k,v in dic.items():
#         if k in cumle:
#             cumle = cumle.replace(k,v)
#     return cumle
# print(chstr(sentence))




