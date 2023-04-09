'''Sizə string şəklində bir abreviatura və list şəklində həmin abreviaturaya qarşılıq gələn sözlər verilir. Bu datalardan hər hərfin key, hər hərfə qarşılıq gələn sözün isə value olduğu bir dictionary əldə edin.'''

# abreviatura = 'AMEAM'
# words = ['Azerbyacan','Milli','Elmler','Akademiyasi', 'Mezunlari']

# abbr_dict = {}
# count_dict = {}
# for i in range(len(abreviatura)):
#     letter = abreviatura[i]
#     if letter not in count_dict:
#         abbr_dict[letter] = words[i]
#         count_dict[letter] = 1
#     else:
#         count_dict[letter] += 1
#         abbr_dict[f"{letter}({count_dict[letter]})"] = words[i]

# print(abbr_dict)

'''Verilmiş dictionary-dən aşağıdakı list-i yaradın. '''

# age_dict = {'toddler_age': '1-5', 'kid_age': '5-13', 'teen_age': '13-17', 'young_age': '17-30', 'adult_age': '30+'}

'''[['toddler_age', (1, 5)], ['kid_age', (5, 13)], ['teen_age', (13, 17)], ['young_age', (17, 30)], ['adult_age', (30, 'and more')]]'''

# age_list = []
# for key, value in age_dict.items():
#     if value.endswith('+'):
#         age_list.append([key, (int(value[:-1]), 'and more')])
#     else:
#         start, end = value.split('-')
#         age_list.append([key, (int(start), int(end))])
        
# print(age_list)

