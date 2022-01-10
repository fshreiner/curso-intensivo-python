# Podemos armazenar dicionários em dicionários, porém com cuidado, pois isto
# pode se tornar rapidamente complicado de se trabalhar
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: {}".format(username))
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: {}".format(full_name.title()))
    print("\tLocation: {}".format(location.title()))
