diff = lambda l1, l2: [x for x in l1 if x not in l2]


def solution(riddle):
    # write your code in Python 3.6
    s = list(riddle)
    import string
    letters = list(string.ascii_letters.lower())
    newlist = diff(letters, s)
    j = -1
    for i in riddle:
        if i == '?':
            j = j + 1
            riddle = riddle.replace('?',newlist[j] , 1)  # Only replace the first x with y
    return riddle



print(solution('??aacc'))
print(solution('a?b?caacc'))

