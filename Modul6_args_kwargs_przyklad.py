# args zwracają tuple : args()
# kwargs zwracają słowniki: kwargs{} - dictionaries, to są argumenty nazwane np x=10

def sample(a,b, *args, **kwargs):
    print('a', a)
    print('b', b)
    print('args', args)
    print('kwargs', kwargs)

print(sample(2,3, 5,6, x=7, y=89))
