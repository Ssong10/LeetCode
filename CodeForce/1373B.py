def next_string(string):
    global result
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            result += 1
            tmp = string[:i] + string[i+2:]
            return next_string(tmp)
    

for tc in range(int(input())):
    s = input()
    result = 0
    next_string(s)
    if result % 2:
        print('DA')
    else:
        print('NET')