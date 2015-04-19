# 1.8
def anagrams(words):
    hashTable = {}
    for word in words:
        sortedWord = "".join(sorted(word)) # can also do string.join(sorted(word), "")
        if sortedWord in hashTable:
            hashTable[sortedWord].append(word)
        else:
            hashTable[sortedWord] = [word]

    li = []
    for key in hashTable.keys():
        val = hashTable[key]
        if len(val) > 1:
            li.append(val)

    return li

dict = ["dog", "logarithm", "god", "algorithm", "snute"]
print anagrams(dict)
print

