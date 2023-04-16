'''
Istifadəçinin daxil etdiyi stringi binary şəklində göstərin.
'''
# text = 'Men Python 3 oyrenirem'
# binary_result = ""

# for char in text: 
#     ascii_code = ord(char)
#     binary_code = bin(ascii_code)[2:]
#     binary_result += binary_code + " "
# print(binary_result)
'''
Istifadəçi input olaraq color: rgb(127, 255, 12) şəklində 
CSS rəngi daxil edəcək. Siz istifadəçinin daxil etdiyi rəngi 
16-lıq sistemdəki qarşılığına çevirin.
'''

# input_color = "color: rgb(244, 123, 12)"
# rgb = input_color.split('rgb(')[1].split(')')[0].split(', ')
# hex_list = [hex(int(i))[2:].zfill(2) for i in rgb]
# output_color = "color: #" + "".join(hex_list)
# print(output_color)


'''
Aşağıdakı listin tuple tipində olan elementlərinin 0-cı indeksi ədədi,
1-ci indeksi isə həmin ədədin hansı say sistemindən olduğunu bildirir;
string tipində olan elementləri isə 16-lıq sistemdən olan ədədləri təmsil edir. 
Bu elementlərin decimal dəyərini alaraq ASCII cədvəlində bir hərfə qarşılıq 
gəlib gəlmədiyini yoxlayan kod yazmalısınız. Output keylər-i bu elementlər, 
value-ları isə Bool dəyər olan dictionary olmalıdır
(Bir hərfə qarşılıq gəlirsə True,əks halda False).
'''
# numbers = [(65, 10), '7F', (106, 8), '7A', '2A', (52, 16), '6B', (49, 16), ('041', 8), (55, 10)]
# output = {}

# for n in numbers:
#     if type(n) == tuple :
#         decimal_value = int(str(n[0]), n[1])
#     else:
#         decimal_value = int(n, 16)
    
#     if 32 <= decimal_value <= 126:
#         output[n] = True
#     else:
#         output[n] = False

# print(output)

''' isascii() metodundan istifadə etmədən hər hansı bir stringin isascii olduğunu yoxlayan kod yazın.'''
s = "Hello World!"
is_ascii = True

for c in s:
    if ord(c) >= 128:
        is_ascii = False
        break

if is_ascii:
    print("The string is ASCII")
else:
    print("The string is not ASCII")




