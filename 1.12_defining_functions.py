# write a function that generates a string
# that is 28 characters long
# by choosing random letters from the 26 letters in the alphabet
# plus the space
import random

def generateOne(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in range(strlen):
        res = res + alphabet[random.randrange(26)]
    return res

# score each generated string
# by comparing the randomly generated string to the goal.
def score(goal,teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame+1
    return numSame / len(goal)

# repeatedly call generate and score
def main():
    goalstring = 'methinks it is like a weasel'
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring,newstring)
    while newscore < 1:
        if newscore > best:
            print(newscore,newstring)
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring,newstring)

print(main())