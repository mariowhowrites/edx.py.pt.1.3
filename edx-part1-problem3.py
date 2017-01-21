# Ok, plan of attack. We need to start at the first letter and work our way down.
# Begin at first two letters. Is the second letter's index equal/greater than that of the first letter?
# If not, first two are out. Move onto third.
# If they are, they're longest streak. Check third, fourth, etc. until you've reached end of streak.
# Start at end of streak, begin process again. Stop before end of streak.

alphabet = "abcdefghijklmnopqrstuvwxyz"
s = "ijmkirfanuakoewkjcn"
stringLength = len(s)
firstLetter = s[0]
secondLetter = s[1]
firstLetterPositionInAlphabet = 0
secondLetterPositionInAlphabet = 0
longestString = ""
currentString = ""
stringIndex = 0
alphaIndex = 0

findingLongestPhrase = True
while findingLongestPhrase:
    if stringIndex == stringLength - 1:
        print("Loop ended! Longest alphabetical string in s is: " + longestString)
        break
    else:
        print("Beginning of loop. Current longest string is " + longestString + " Currently checking the string from: " + str(stringIndex))
        firstLetter = s[stringIndex]
        secondLetter = s[stringIndex + 1]
        print("First letter being compared is: " + firstLetter, "Second letter being compared is: " + secondLetter + ". Current comparison string = " + currentString )

    findingLetterPositions = True
    firstLetterPositionInAlphabet = 0
    secondLetterPositionInAlphabet = 0
    alphaIndex = 0
    while findingLetterPositions:
        print(firstLetterPositionInAlphabet, secondLetterPositionInAlphabet)
        if firstLetterPositionInAlphabet != 0 and secondLetterPositionInAlphabet != 0:
            findingLetterPositions = False
            break
        else:
            if firstLetter == alphabet[alphaIndex]:
                firstLetterPositionInAlphabet = alphaIndex + 1
            if secondLetter == alphabet[alphaIndex]:
                secondLetterPositionInAlphabet = alphaIndex + 1;
        alphaIndex += 1

    print("Done finding first/second letter alphabet indices. First letter index position is: " + str(firstLetterPositionInAlphabet), "second letter index position is: " + str(secondLetterPositionInAlphabet))

    # Alright, we have our two letters. Now we need to find out what to do with them.
    # The options are A) do nothing and skip to next letter, B) add to existing string if it exists, C) create new string if current string does not exist
    findingState = True
    while findingState:
        if secondLetterPositionInAlphabet < firstLetterPositionInAlphabet:
            print("Second is less than first, skip to next letter of phrase and reset current string")
            currentString = ""
            findingState = False
            break
        elif currentString == "":
            currentString = firstLetter + secondLetter
            findingState = False
            break
        else:
            currentString += secondLetter
            findingState = False
            break

    if len(currentString) > len(longestString):
        print("New longest string found. Assigning " + currentString + " as the new longest string. It replaces " + longestString + " as the longest string.")
        longestString = currentString

    stringIndex += 1




    # Ok, what's our process?
# One, start at the beginning.
# Build our current string. To begin, that'd be letters one and two.
# If second letter >= first, start comparing process.
    # Is this string our longest? Assign it.
    # Now, compare the last letter of string with the one after it.
    # If
# If not, skip to end of phrase and move on.

# My question currently is: when do we build our string? When is it important to build a string?
# We want this
