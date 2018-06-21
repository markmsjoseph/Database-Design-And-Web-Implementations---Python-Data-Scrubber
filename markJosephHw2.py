
#open a text file in read mode
f = open("SAT_Results.csv", "r")


#make a blank list that stores all the new lines we will write to the file
newLinesInFile = []


for line in f:
    wordsInLine = line.split(",")#separate words in line by comma
    newWordsInLine = [] #make a blank list that will store the fixed words in this line
    newScrubbedLine = []
    newarr = []

    #remove the first unnecessary column
    for word in wordsInLine[1:]:
        newWordsInLine.append(word)

    #capatilize all words
    for word in newWordsInLine:
        newWord = word.capitalize()
        newScrubbedLine.append(newWord)
    print(newScrubbedLine)
    #convert the list of words in this line to a string, so it can be written to a file easily
    newScrubbedLine = ",".join(newScrubbedLine)
      #add this line to the list of new lines that we will write to the file
    newLinesInFile.append(newScrubbedLine)

f.close()


print("writing to file")

#now.... open a file in write mode so we can write all the new lines to it
f = open("newSAT_Data.csv", "w")

#loop through all the lines we want to write
for line in newLinesInFile:
    #write each line
    f.write(line)

#done, so close the file
f.close()

print("contents written to new file")

