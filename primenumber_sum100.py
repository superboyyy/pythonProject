sum = 0
for i in range(2, 101):
    for o in range(2, i):
        if i % o == 0:
            break
    else:
        sum = sum + i
print(sum)
