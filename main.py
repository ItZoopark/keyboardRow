def findWords(words):
    firstRow = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    secondRow = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    thirdRow = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    res = []
    for word in words:
        count1, count2, count3 = 0, 0, 0
        for letter in word.lower():
            if letter in firstRow:
                count1 += 1
            elif letter in secondRow:
                count2 += 1
            elif letter in thirdRow:
                count3 += 1

        if count1 == len(word) or count2 == len(word) or count3 == len(word):
            res.append(word)
    print(res)


def findWords2(words):
    firstRow = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    secondRow = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    thirdRow = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    res = []
    for word in words:
        word_set = set(word.lower())
        if word_set.issubset(firstRow):
            res.append(word)
        elif word_set.issubset(secondRow):
            res.append(word)
        elif word_set.issubset(thirdRow):
            res.append(word)
    print(res)


def findWords3(words):

    row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

    dic = {}
    for l in row1:
        dic[l] = 1
    for l in row2:
        dic[l] = 2
    for l in row3:
        dic[l] = 3
    res = []
    for word in words:
        flag = True
        for i in range(len(word) - 1):
            if dic[word[i].lower()] != dic[word[i + 1].lower()]:
                flag = False
                break
        if flag:
            res.append(word)

    return dic


# a = {1, 2, 3, 4}
# b = {2, 4, 5}
#
# print(b.issubset(a))
# secondRow = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords3(words))
# word = set(words[1])
# print(word)
# print(secondRow)
# print(word.issubset(secondRow))
# print().issubset(secondRow))
