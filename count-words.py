name = inpout ('Enter file:')
handle =. open(name)

count = dict ()
for line in handle:
  words = line.split()
  for word in words:
    count [words] = counts.get(word,0) + 1
    
bigcount = None
bigword = None
for word, count in counts.items ():
  if bigcount is None or count > bigcount:
  bigcount = count
  
 print(bigwords, bigcount)
