users = {
    'gozde': {
        'ad': 'gozde',
        'yas': 36,        
        'grup': ['akademisyen']
    },
    'mustafa': {
        'ad': 'mustafa',
        'yas': 36,        
        'grup': ['akademisyen', 'ogrenci']
    }
}

print(users['gozde'])

print(users['mustafa'])

print(users['mustafa']['grup'])

spaceships = {
    'Krait Mk II': {'Manufacturer': 'Faulcon DeLacy',
                    'Year Produced': 3304,
                    'Cost' : 40201966,
                    'Seats' : 3},
    'Cobra Mk III': {'Manufacturer': 'Faulcon DeLacy',
                    'Year Produced': 3100,
                    'Cost' : 306879,
                    'Seats' : 2},
    'Asp Explorer': {'Manufacturer': 'Lakon Spaceways',
                    'Year Produced': 3300,
                    'Cost' : {'Advance Payment' : 661153, 'Full Payment' : 1028390},
                    'Seats' : 2}
}

print(spaceships['Krait Mk II'])

print(spaceships['Cobra Mk III']['Manufacturer'])

print(spaceships['Asp Explorer']['Cost']['Full Payment'])