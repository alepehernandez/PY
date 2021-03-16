fh = open("romeo.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")

fh = open("words.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")

fh = open("mbox-short.txt")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1
print (count, "Lines")