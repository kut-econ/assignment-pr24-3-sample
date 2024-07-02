# %%
j = 1
for i in range(1,1000):
    hundreds = i // 100
    tens = (i % 100) // 10
    ones = i % 10
    if hundreds == 3 or tens == 3 or ones == 3:
        if j % 8 == 0:
            end_str = '\n'
        else:
            end_str = ' '
        print(i,end=end_str)
        j += 1

# %%
for i in range(1,1000):
    s = 0
    for j in range(1,i):
        if i % j == 0:
            s += j
    if i == s:
        print(i,s,'完全数')
    elif s == 1:
        print(i,s,'素数')
    else:
        print(i,s)
