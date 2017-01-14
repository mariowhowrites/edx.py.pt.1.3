currentString = ""
longestString = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetIndex = 0
stringIndex = 0
s = "qeyyzkobsteu"
stringLength = len(s)



currentHead = s[0]

# print("Beginning string length: " + str(stringLength))

# basic gameplan here is to match first letter with a spot in the alphabet.
# If first two letters are two letters in the alphabet, continue.
# If not, skip to the end of the sequence and begin checking again.
# At the end of the string, spit out the longest variable you found.

findingPhrase = True

while findingPhrase:
    if stringIndex == stringLength - 1:          # if we're at the end of the string
        print("All done finding the phrase!")
        findingPhrase = False
        break                                    # exit the loop, present results
    elif stringIndex == 0:                                        # if we're at the beginning, we need to assign the first 2 to our longestString
        longestString = s[:2]
        print("About to start. Assigning the first two letters to longestString: " + longestString)
    else:                                        # otherwise, we need to find a string to compare. we match the string header with a letter in the alphabet string, and then we compare header + 1 with alphabet + 1
        findingIndex = True
        x = 0
        while findingIndex:
            if alphabet[x] == currentHead:
                alphabetIndex = x
                findingIndex = False
            else:
                x += 1

    # At this point, we can begin to compare the string to the alphabet.
    # First, we've got to build our new excerpts and compare them.
    # We don't want to move the string index quite yet.
    # We either want to move it once if we don't find a match, or to end of current matched string if it matches.

    #print(stringIndex)

    stringExcerpt = s[stringIndex] + s[stringIndex + 1]
    alphabetExcerpt = alphabet[alphabetIndex] + alphabet[alphabetIndex + 1]
    print("Setting stringExcerpt to: " + stringExcerpt + ". Setting alphabetExcerpt to: " + alphabetExcerpt)

    if stringExcerpt == alphabetExcerpt:
        while stringExcerpt == alphabetExcerpt:
            print("StringExcerpt before: " + stringExcerpt + " alphabetString before: " + alphabetExcerpt)
            stringExcerpt += s[stringIndex + len(stringExcerpt)] # adding one letter to stringExcerpt
            alphabetExcerpt += alphabet[alphabetIndex + len(alphabetExcerpt)] # adding one letter to alphabetExcerpt
            print("StringExcerpt after: " + stringExcerpt + " alphabetString after: " + alphabetExcerpt)
        comparisonString = stringExcerpt[:len(stringExcerpt)-1]
        if len(comparisonString) > len(longestString):
            print("Current longest string: " + longestString + ". Proposed longest string: " + comparisonString)
            longestString = comparisonString
        stringIndex += len(comparisonString)
    else:
        #print("Moving on...")
        stringIndex += 1
        currentHead = s[stringIndex]
    #print(stringIndex, stringLength)

print("Longest substring in alphabetical order is: " + longestString)
