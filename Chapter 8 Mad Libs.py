import re

madLibsFile= open('Mad Libs.txt')

madLibsFile = madLibsFile.read()

madLibsWords = madLibsFile.split()

adjectiveRegex = re.compile(r'(ADJECTIVE)')
nounRegex = re.compile(r'(NOUN)')
adverbRegex = re.compile(r'(ADVERB)')
verbRegex = re.compile(r'(VERB)')

for i in range(len(madLibsWords)):
    if adjectiveRegex.search(madLibsWords[i]):
        adjective = input('Enter an adjective:\n')
        madLibsWords[i] = adjectiveRegex.sub(adjective,madLibsWords[i])
    elif nounRegex.search(madLibsWords[i]):
        noun = input('Enter a noun\n')
        madLibsWords[i] = nounRegex.sub(noun,madLibsWords[i])
    elif adverbRegex.search(madLibsWords[i]):
        adverb = input('Enter an adverb:\n')
        madLibsWords[i] = adverbRegex.sub(adverb,madLibWords[i])
    elif verbRegex.search(madLibsWords[i]):
        verb = input('Enter an verb:\n')
        madLibsWords[i] = verbRegex.sub(verb,madLibsWords[i])
        

newMadLibs = (' ').join(madLibsWords)
print(newMadLibs)

newFile = open('newMadLibs.txt','w')
newFile.write(newMadLibs)
newFile.close()


