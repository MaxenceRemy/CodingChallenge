# --------------------------- INFORMATION ------------------------------ #

# When solving the second puzzle of one day,
# I never change the code of the first puzzle.
# I can use variables or results from the first one, and that's it.
# I don't think there are rules about this but that's what I'm sticking to.

# --------------------------- PUZZLE NUMBER 1 -------------------------- #

# We create two empty lists
list1 = []
list2 = []

# We open the raw data
with open('../rawData/rawLists.txt', 'r') as doc:
    # For each line in the document...
    for line in doc:
        # We use spaces to split the numbers
        splitNumbers = line.split()
        # We append and convert to int the first number of the line
        # into our first list
        list1.append(int(splitNumbers[0]))
        # And we do the same for the second list
        list2.append(int(splitNumbers[1]))

# We now sort the lists in ascending order
list1.sort()
list2.sort()

# For each number in the first list, we calculate the absolute difference
# with the one in the second list
# We will store all the differences in a new list
differences = []

# We iterate over the two lists at the same time
for number1, number2 in zip(list1, list2):
    # And we append the absolute difference to our difference list
    differences.append(abs(number1 - number2))

# We now compute the sum to get the total difference
totalDifference = sum(differences)
# And here is the result
print(f"Total difference between the two lists : {totalDifference}")


# --------------------------- PUZZLE NUMBER 2 -------------------------- #

# We create a new list for the total similarity score
similarityScore = []

# We iterate over the first list
for number in list1:
    # We count, for the number in the first list,
    # how many times it appears in the second list
    nbrOfOccurences = list2.count(number)
    # We calculate the similarity score and we append it to the similarity list
    similarityScore.append(number * nbrOfOccurences)

# We now calculate the sum to get the total similarity score
totalSimilarityScore = sum(similarityScore)
# And here is our final answer
print(f"Total similarity score : {totalSimilarityScore}")
