''' Asağıdaki alqoritmlərin sürətini ölçün.'''
# import timeit

# def algorithm1():
#     text = 'I live in New York'
#     textreverse = text[::-1]
#     vowels = 'aeiuo'
#     result = ''
#     for char in textreverse:
#         if char not in vowels:
#             result += char
#     return result

# def algorithm2():
#     text = list('I live in New York')
#     text.reverse()
#     vowels = 'aeiuo'
#     for char in text:
#         if char not in text:
#             text.remove(char)
#     return ''.join(text)


# time1 = timeit.timeit(algorithm1, number=100000)
# print("1-ci alqoritmin vaxtı:", time1)


# time2 = timeit.timeit(algorithm2, number=100000)
# print("2-ci alqoritmin vaxtı:", time2)

''' Geri sayim programi hazirlayin. Input olaraq bir deyer verin və program həmin dəyərdən 0-a doğru saniyə-saniyə geri saysın. 0-a çatdıqda bitdi desin.'''

# import time

# def countdown(start):
#     for i in range(start, -1, -1):
#         print(i)
#         time.sleep(1)
#     print("Bitdi")


# start_value = int(input("Ədədi daxil edin: "))

# countdown(start_value)

''' Oldugunuz dirde dersler deye bir folder yaradin. 
Sonra hemin foldere ders1.txt ve ders2.txt elave edin.
Daha sonra ders1.txt silin ve ders2.txt adini deyisib,
Python Notlar yazin. Sonra ic-ice Python/General Python 
deye folderler hazirlayin. Ardindan Python Notlar faylini
ora elave edin. Daha sonra eyni faylin kopyasini Desktopa atin. 
En sonda da dersler folderini silin.'''

# import os
# import shutil

# os.mkdir('dersler')

# open('dersler/ders1.txt', 'w')
# open('dersler/ders2.txt', 'w')

# os.remove('dersler/ders1.txt')

# os.rename('dersler/ders2.txt', 'dersler/Python Notlar.txt')

# os.makedirs('dersler/Python/General Python')

# shutil.move('dersler/Python Notlar.txt', 'dersler/Python/General Python/Python Notlar.txt')

# shutil.copy('dersler/Python/General Python/Python Notlar.txt', 'Desktop/Python Notlar.txt')

# shutil.rmtree('dersler')