fruits = {
    'orange': 10,
    'apple': 20,
    'banana': 30
}

key = None 

while True:
    try:
        key = input('Enter a key to lookup: ')
        fruits = fruits[key.lower()]
    except KeyError:
        print(f'Error! {key} does not exist.')
    except KeyboardInterrupt:
        break
    else: 
        print('Press Ctrl-C to exit.')