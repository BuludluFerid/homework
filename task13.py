def az_to_en(text):
    char_mappings = {
        'ə': 'e',
        'ü': 'u',
        'ö': 'o',
        'ğ': 'g',
        'ı': 'i',
        'ş': 's',
        'ç': 'c',
    }
    for char in char_mappings:
        text = text.replace(char, char_mappings[char])
    return text

def ing_cevir(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        result = az_to_en(result)
        return result
    return wrapper

@ing_cevir
def salam_ver(ad, soyad):
    return 'Salam hörmətli {} {}, necəsiniz?'.format(ad, soyad)

print(salam_ver('Ferid', 'Buludlu'))
