europe = {
    'Germany': {
        'capital': 'Berlin',
        'minimum wage per year': 23_712,
        'social welfare': 70,
        'developed': True      
    },
    'Norway': {
        'capital': 'Oslo',
        'minimum wage per year': 30_531,
        'social welfare': 80,
        'developed': True      
    },
    'Albania': {
        'capital': 'Tirana',
        'minimum wage per year': 4_176,
        'social welfare': 45,
        'developed': False      
    },
    'Moldova': {
        'capital': 'Kishinev',
        'minimum wage per year': 4_800,
        'social welfare': 40,
        'developed': False      
    },
    'Austria': {
        'capital': 'Vienna ',
        'minimum wage per year': 30_550,
        'social welfare': 72,
        'developed': False      
    }        
}

asia_europe = {
    'Azerbaijan': {
        'capital': 'Baku',
        'minimum wage per year': 2_280,
        'social welfare': 20,
        'developed': False      
    },
    'Armenia': {
        'capital': 'Yerevan',
        'minimum wage per year': 3_036,
        'social welfare': 18,
        'developed': False      
    },
    'Georgia': {
        'capital': 'Tbilisi',
        'minimum wage per year': 5_208,
        'social welfare': 30,
        'developed': False      
    },
    'Kazakhstan': {
        'capital': 'Astana',
        'minimum wage per year': 1_728,
        'social welfare': 20,
        'developed': False      
    },
    'Turkey': {
        'capital': 'Ankara ',
        'minimum wage per year': 5_868,
        'social welfare': 33,
        'developed': False      
    }        
}

"""
3) Hər iki dict-dən istifadə edərək inkişaf etmiş və inkişaf etməmiş ölkələri məlumatları ilə birgə ayrı dict-lərə keçirin; 
"""

# def separate_countries_by_development(d1, d2):
#     developed_countries = {}
#     undeveloped_countries = {}

#     for country, data in d1.items():
#         if data["developed"]:
#             developed_countries[country] = data
#         else:
#             undeveloped_countries[country] = data

#     for country, data in d2.items():
#         if data["developed"]:
#             developed_countries[country] = data
#         else:
#             undeveloped_countries[country] = data
            
#     return developed_countries, undeveloped_countries

# developed, undeveloped = separate_countries_by_development(europe, asia_europe)

# print("Developed countries:")
# for country, data in developed.items():
#     print(country, data)

# print("\nUndeveloped countries:")
# for country, data in undeveloped.items():
#     print(country, data)


