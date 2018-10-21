#ActiveCode 1
#Answer:['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']

wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

#ActiveCode 2
#Answer:['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
print(letterlist)

#ActiveCode 3
#Use list comprehension by redoing ac2
wordlist = ['cat','dog','rabbit']
print([ch for ch in ''.join(wordlist)])
print([word[i] for word in wordlist for i in range(len(word))])

#how to remove the duplicates
print(list(set([word[i] for word in wordlist for i in range(len(word))])))


