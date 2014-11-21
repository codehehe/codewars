'''
Most Frequent Elements

Find the most frequent element or elements in the list.

Example:

find_most_frequent([1, 1, 2, 3]) == set([1])
find_most_frequent([1, 1, 2, 2, 3]) == set([1, 2])
find_most_frequent([1, 1, '2', '2', 3]) == set([1, '2'])

'''

def find_most_frequent(l):
    map={}
    for item in l:
        map[item] = map.get(item, 0) + 1
    tuples = sorted(map.iteritems(), key=lambda x : x[1], reverse = True)
    max = 0
    result = []
    for t in tuples:
        if max > t[1]:
            break
        else:
            max = t[1]
            result.append(t[0])
    return set(result)

print find_most_frequent([1, 1, 2, 3])
print find_most_frequent([1, 1, 2, 2, 3])
print find_most_frequent([1, 1, '2', '2', 3])
