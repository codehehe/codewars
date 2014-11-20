'''

| HEAD | <----------- TAIL ------------> |
[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
| <----------- INIT ------------> | LAST |

nice solution

head = lambda array: array[0]
tail = lambda array: array[1:]
init = lambda array: array[:-1]
last = lambda array: array[-1]

'''

def head(list):
    return list[0] if len(list) > 0 else None



def tail(list):
    return list[1:len(list)] if len(list) > 0 else []



def init(list):
    return list[0: len(list)-1] if len(list) > 0 else []



def last(list):
    return list[len(list) - 1] if len(list) > 0 else None


print head([5,1])
print tail([1])
print init([1,5,7,9])
print last([7,2])


