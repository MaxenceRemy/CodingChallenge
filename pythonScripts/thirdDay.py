# --------------------------- INFORMATION ------------------------------ #

# When solving the second puzzle of one day,
# I never change the code of the first puzzle.
# I can use variables or results from the first one, and that's it.
# I don't think there are rules about this but that's what I'm sticking to.

# --------------------------- PUZZLE NUMBER 1 -------------------------- #

# This library allows to use regular expressions
import re

# This expression matches only the correct
# format of data we are searching for
# Also, it only captures the numbers, because that's all we need in the end
regex = r'mul\((\d{1,3}),(\d{1,3})\)'

# We open the file containing the corrupted data
with open('../rawData/rawMul.txt', 'r') as doc:
    # This function allow to find all strings that matches our regex
    correctData = re.findall(regex, doc.read())

# This list will contain all the results from our multiplications
totalMultipliedNumbers = []

# We iterate over the correctly formatted data
for numberPair in correctData:
    # We multiply the first number with the second,
    # after converting them to integers,
    # and we append the result to our big list
    totalMultipliedNumbers.append(int(numberPair[0]) * int(numberPair[1]))

# We then sum up all the numbers to get our final answer
finalAnswer = sum(totalMultipliedNumbers)
print(finalAnswer)

# --------------------------- PUZZLE NUMBER 2 -------------------------- #

# The goal is to extract all the strings in between a do() and a don't()
# I first tried with regex, but it didn't work for all cases,
# so here is my new method

# We open the file containing the corrupted data
with open('../rawData/rawMul.txt', 'r') as doc:
    # We add a do() at the beginning because all mul are enabled by default
    # We also add a don't() at the end so that it correctly closes our search
    corruptedData = "do()" + doc.read() + "don't()"

# This string will contain all the enabled data
finalEnabledData = ""

# Now, we run a loop as long as do() and don't() are present
while "do()" in corruptedData and "don't()" in corruptedData:
    # We find the opening do() index
    doIndex = corruptedData.index("do()")
    # We then find the closing don't()
    dontIndex = corruptedData.index("don't()")
    # We extract the text between those indexes
    # and add it to our final enabled data
    finalEnabledData = finalEnabledData + corruptedData[doIndex:dontIndex+7]
    # We then remove this part from the corrupted data
    # so that we can find the next do() and don't()
    corruptedData = corruptedData[dontIndex+7:]

# Now that we have our data, let's process it like in the first code

# This time, we don't read the document
# but we use the enabled data to find the correct mul
newCorrectData = re.findall(regex, finalEnabledData)

# This list will contain all the results from our multiplications
newTotalMultipliedNumbers = []

# We iterate over the correctly formatted and enabled data
for numberPair in newCorrectData:
    # We multiply the first number with the second,
    # after converting them to integers,
    # and append the result to our big list
    newTotalMultipliedNumbers.append(int(numberPair[0]) * int(numberPair[1]))

# We then sum up all the numbers to get our new final answer
newFinalAnswer = sum(newTotalMultipliedNumbers)
print(newFinalAnswer)
