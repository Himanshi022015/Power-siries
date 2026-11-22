
n = int(input("How many terms do you want? "))
print("Power Series")

for i in range(1, n + 1):
    term = i + i
    print("%d + %d = %d" % (i, i, term))
