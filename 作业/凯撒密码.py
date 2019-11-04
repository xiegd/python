def lock(str):
    alp = 'abcdefghijklmnopqrstuvwxyzabcABCDEFGHIJKLMNOPQRSTUVWXWZABC'
    str2 = ''
    for n in range(len(str)):
        if str[n] !=  ' ':
            str2 += str.replace(str[n],alp[alp.find(str[n]) + 3])[n]
    return str2


def unlock(str):
    alp1 = 'CBAZWXWVUTSRQPONMLKJIHGFEDCBAcbazyxwvutsrqponmlkjihgfedcba'
    alp = 'abcdefghijklmnopqrstuvwxyzabcABCDEFGHIJKLMNOPQRSTUVWXWZABC'
    str2 = ''
    for n in range(len(str)):
        if str[n] !=  ' ':
            str2 += str.replace(str[n],alp[alp.find(str[n]) - 3])[n]
    return str2

def test():
    sen = input()
    print(lock(sen),'\n',unlock(lock(sen)))


test()