import os
import re

#os.chdir('/nfs/2017/a/adeokule/Desktop/')
os.chdir(r'C:\Users\Akshey.Deokule21\APCSP_CreateTask')

myfile = open("words.txt", 'r', encoding = "utf8")
mystuff = myfile.read()
mystuff += ' ' * 2

def syllables(word):
    wordSyl = word.lower().strip(".:;?!")
    countSyl = 0
    vowels = 'aeiouy'
    if wordSyl[0] in vowels:
        countSyl +=1
    for index in range(1,len(wordSyl)):
        if wordSyl[index] in vowels and wordSyl[index-1] not in vowels:
            countSyl +=1
    if wordSyl.endswith('e'):
        countSyl -= 1
    if wordSyl.endswith('le'):
        countSyl+=1
    if countSyl == 0:
        countSyl +=1
    if len(wordSyl) <= 3:
    	countSyl = 1
    if "n't" in wordSyl:
    	countSyl += 1
    return countSyl

count = len(re.findall(r'\w+', mystuff))

def sentences(paragraph):
    sentencecounte = 0
    openq = '“'
    closeq = '”'
    period = '.'
    opqstart = ([pos for pos, char in enumerate(paragraph) if char == openq])
    print (opqstart)
    closeqsend = ([pos for pos, char in enumerate(paragraph) if char == closeq])
    print (closeqsend)
    periodend = ([pos for pos, char in enumerate(paragraph) if char == period])
    print (periodend)
    y = 0
    #print (paragraph[periodend[y]+2])
    #print ((paragraph[periodend[y]+2]).isalpha())
    for y in range(len(periodend)):
        if (paragraph[periodend[y]+2]).isalpha() == True and (paragraph[periodend[y]+2]).isupper() == True:
            sentencecounte += 1
        if (paragraph[periodend[y]+2]) == "“":
            sentencecounte += 1
        y += 1
    try:
        count = 0
        countlist = 0
        for count in range(len(periodend)):
            if periodend[count] > opqstart[countlist] and periodend[count] < ((closeqsend[countlist])-1):
                if periodend[count+1] > closeqsend[countlist]:
                    countlist -= 1
                sentencecounte -= 1
            count +=1
    except IndexError:
        print ("No quotes")
    return sentencecounte

syllablecounte = syllables(mystuff)
sentencecount = sentences(mystuff)
print (('Syllable Count = %s') %syllablecounte)
print (('Word Count = %s') %count)
print (('Sentence Count = %s') %sentencecount)
  
ReadingEase = 206.835-(1.015*(count/sentencecount))-(84.6*(syllablecounte/count))
ReadingLevel = (0.39*(count/sentencecount)) + (11.8*(syllablecounte/count)) - 15.59

print (('Reading Level = %s') %(ReadingLevel))

if ReadingLevel > 100.00:
	print ('4th grade and lower reading level.')
	print ('Very easy to understand for younger age children.')

if ReadingLevel >= 90.00 and ReadingLevel <= 100.00:
	print ('5th grade reading level.')
	print ('Very easy to read. Easily understood by an average 11-year-old student.')

if ReadingLevel >= 80.00 and ReadingLevel < 90.00:
	print ('6th grade reading level.')
	print('Easy to read. Conversational English for consumers.')

if ReadingLevel >= 70.00 and ReadingLevel < 80.00:
	print ('7th grade reading level.')
	print('Fairly easy to read.')

if ReadingLevel >= 60.00 and ReadingLevel < 70.00:
	print ('8th-9th grade reading level.')
	print('Plain English. Easily understood by 13- to 15-year-old students.')

if ReadingLevel >= 50.00 and ReadingLevel < 60.00:
	print ('10th-12th grade reading level.')
	print('Fairly difficult to read.')

if ReadingLevel >= 30.00 and ReadingLevel < 50.00:
	print ('Collegiate reading level.')
	print('Difficult to read.')

if ReadingLevel >= 0.00 and ReadingLevel < 30.00:
	print ('College Grad reading level.')
	print('Very difficult to read. Best understood by university graduates.')

myfile.close() 