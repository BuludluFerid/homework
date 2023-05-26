
'''1)Bu kodda baş verə biləcək errorları araşdırıb, onları handle edin'''
'''2)Təxmin edə bilməyəcəyiniz errorlar üçün bir şərt qoşun'''
'''3)Əgər istifadəçi 10-dan artıq və ya 3-dən az heyvan giribsə internetdən istədiyiniz bir erroru taparaq təyin edin.'''
# total_price = 0
# animals = input('Heyvanlari girin: ').split(', ')
# try:
#     if len(animals) < 3 or len(animals) > 10:
#         raise ValueError(f"Heyvan sayisi 3'den az ve ya 10'dan cox ola bilmez.")
#     prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }
#     print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals)))
# except KeyError as e:
#     print(f"{animals} adli heyvan yoxdur.",f"xeta mesajı{e}")
# except Exception :
#     print(f"Bilinmeyen xeta baş verdi")

'''1000-dən 0001-ə qədər sağında nöqtə ilə düzülmüş bir text faylı hazırlayın'''

# with open("numbers.txt", "w") as f:
#     for i in range(1000, 0, -1):
#         f.write(str(i).zfill(4) + ".\n")

# with open("numbers.txt", "r") as f:
#     lines = f.readlines()

# for line in lines:
#     print(line.strip())


# with open('ders.txt',encoding="UTF-8", mode='r') as file:
#     lines = file.readlines()[1:]
#     sorted_lines = sorted(lines, key=lambda x: x.split(',')[2], reverse=True)
#     print(sorted_lines)




    
    
    
    
    
    




