# 1. strings to integers - wszystkie elementy
# 2. integers to strings - wszystkie elementy


def strs_to_integers(sentence:list) -> int:
    return list(map(int, sentence))

print(strs_to_integers(['1','2','3','4']))
print(type(strs_to_integers(['1','2','3','4'])))

def ints_to_strs(sentence:list) -> str:
    return list(map(str, sentence))

print(ints_to_strs([1,2,3,4]))
print(type(ints_to_strs([1,2,3,4])))