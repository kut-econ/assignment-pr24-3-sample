# 課題で提示されたタスクを実行するコードを以下に記述しなさい。
# タスクごとにセルを分けて記述してください。
#%%
# Task 1. 素数リストprime_numbersの作成と出力

prime_numbers = []
i = 2
while len(prime_numbers) < 100:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)
    i += 1

# prime_numbersの要素を出力
for i in range(len(prime_numbers)):
    if i % 10 == 9:
        print(prime_numbers[i])
    else:
        print(prime_numbers[i],end=' ')
# %%
# Task 2. prime_numbersの要素を逆順に出力

# prime_numbersを逆順にしたリストを作成
rev = prime_numbers[::-1]
for i in range(len(rev)):
    if i % 10 == 9:
        print(rev[i])
    else:
        print(rev[i],end=' ')

# %%
# Task 3. prime_numbersの要素のうち偶数番目のものを出力

# 偶数番目の素数からなるリストを作成
even = prime_numbers[1::2]
for i in range(len(even)):
    if i % 10 == 9:
        print(even[i])
    else:
        print(even[i],end=' ')

# %%
# Task 4. prime_numbersの要素のうち素数番目のものを出力

j = 0
for i in range(len(prime_numbers)):
    if i+1 in prime_numbers:
        j += 1
        if j % 5 == 0:
            print(prime_numbers[i])
        else:
            print(prime_numbers[i],end=' ')
