baliqlar = {
    'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}

cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}

amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'koteks vardir',
    'yumurtlama', 'dis yoxdur'
}

surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}

quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}

sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}
'''
1) Quşların xüsusiyyətlərinə '2 ayaq' əlavə edin.
'''

# quslar.add('2 ayaq')
# print(quslar)

'''
2) Balıqların xüsusiyyətlərindən "4 ayaq" məlumatını çıxarın
'''
# baliqlar.remove('4 ayaq')
# print(baliqlar)

'''
3) Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın
'''
# print(amfibialar.intersection(cuculer))

'''
4)Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın
'''
# print(baliqlar.symmetric_difference(amfibialar))

'''
6) Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın
'''
# max_intersection = 0
# max_intersection_sinif = ""

# for sinif, xususiyyetler in sinifler.items():
#     if sinif == 'quslar':
#         continue

#     intersection_size = len(quslar.intersection(xususiyyetler))
#     if intersection_size > max_intersection:
#         max_intersection = intersection_size
#         max_intersection_sinif = sinif

# print(max_intersection_sinif)


