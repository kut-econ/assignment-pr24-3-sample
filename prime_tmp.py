# %%
prime_numbers = []
i = 2
while len(prime_numbers) < 100:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)
    i += 1
# %%
for i in range(len(prime_numbers)):
    if i % 10 == 9:
        print(prime_numbers[i])
    else:
        print(prime_numbers[i],end=' ')

# %%
rev = prime_numbers[::-1]
for i in range(len(rev)):
    if i % 10 == 9:
        print(rev[i])
    else:
        print(rev[i],end=' ')
# %%
even = prime_numbers[1::2]
for i in range(len(even)):
    if i % 10 == 9:
        print(even[i])
    else:
        print(even[i],end=' ')

# %%
j = 0
for i in range(len(prime_numbers)):
    if i+1 in prime_numbers:
        j += 1
        if j % 5 == 0:
            print(prime_numbers[i])
        else:
            print(prime_numbers[i],end=' ')


# %%
