# --------------------------- INFORMATION ------------------------------ #

# When solving the second puzzle of one day,
# I never change the code of the first puzzle.
# I can use variables or results from the first one, and that's it.
# I don't think there are rules about this but that's what I'm sticking to.

# --------------------------- PUZZLE NUMBER 1 -------------------------- #

# We will first transform the raw string into a numpy array,
# that will be easier to manipulate in all directions
# It's perfect for our case because the data has always
# the same number of characters on one line

# We import numpy because it's easy to use and powerful
import numpy as np

# We open the raw data
with open('../rawData/rawWordSearch.txt', 'r') as doc:
    # This list will contain all the separate lines
    rawWordSearchList = []
    # We iterate over each line of the raw text
    for line in doc:
        # We append each line as well as converting it to a list of letter
        # and deleting the newline characters
        rawWordSearchList.append(list(line.replace('\n', '')))
    # Because we have now have nested lists,
    # numpy can easily create an array with the correct shape
    rawWordSearchArray = np.array(rawWordSearchList)

# This will tell us the total number of apparitions of the word XMAS
totalApparitions = 0


def countHorizontalWords(array: np.ndarray):
    """ This function counts the number of time the word XMAS appears
    in both direction on every horizontal line of the array
    and adds this number to the total counter.

    It takes a numpy array as input and returns the number of
    XMAS occurences found.
    """
    # This will contain the number of times XMAS appears
    wordCount = 0
    # We iterate over each line of the array
    for line in array:
        # We convert the list of characters to a single string
        horizontalLine = ''.join(line)
        # We count the number of times the two versions of the word
        # appear and we add that to the total counter
        wordCount += (horizontalLine.count('XMAS') +
                      horizontalLine.count('SAMX'))
    # We return the number of occurences in this array
    return wordCount


# We will begin by searching for the word horizontally
# and add the count to the total counter
totalApparitions += countHorizontalWords(rawWordSearchArray)

# We will now search vertically, so let's feed a
# 90 degrees rotated array into our function
totalApparitions += countHorizontalWords(np.rot90(rawWordSearchArray, k=1))


def extractDiagonals(array: np.ndarray):
    """ This function counts the number of times the word XMAS
    appears on left to rights diagonals,
    starting both from the top line and the left column.

    It takes a numpy array as input and returns the number
    of XMAS occurences found.
    """
    # This will contain the number of times XMAS appears
    wordCount = 0
    # We get the number of lines and columns in the array
    nbrRows, nbrCols = array.shape
    # Because np.diagonal takes an offset for the point where it
    # starts its diagonal from, we iterate from the bottom-left
    # of the array to the top-right
    for i in range(-nbrRows + 1, nbrCols):
        # We get the diagonal letters and join them into a string
        diagonalLine = ''.join(np.diagonal(array, offset=i))
        # We count the number of times the two versions of the word appear
        # and we add that to the total counter
        wordCount += diagonalLine.count('XMAS') + diagonalLine.count('SAMX')
    # We return the number of apparitions in this array
    return wordCount


# Thanks to our functions, we will just need
# to flip the array to get all the diagonals

# Let's start with the left to right diagonals
totalApparitions += extractDiagonals(rawWordSearchArray)

# Then let's mirror the array to get the diagonals from right to left
totalApparitions += extractDiagonals(np.fliplr(rawWordSearchArray))

# We have now our final answer
print(f"Total number of apparitions of the word XMAS in all directions : "
      f"{totalApparitions}")


# --------------------------- PUZZLE NUMBER 2 -------------------------- #

# My method is to find the coordinates of all the A,
# because they are always the center of an X-MAS
# Then, just look at its neighbours and see
# if it matches 1 of the 4 combinations possible

# We can reuse the array from before and extract all A coordinates
aCoordinates = np.argwhere(rawWordSearchArray == 'A')

# This will contain the number of times an X-MAS pattern appears
totalXMasCounter = 0

# We get the number of rows and columns for later
nbrRows, nbrCols = rawWordSearchArray.shape

# We will now loop through all the A coordinates
# and look at the letter in the top-left, top-right,
# bottom-left and bottom-right of each A
for coordinates in aCoordinates:
    # We store the coordinates in short variables
    x, y = coordinates[0], coordinates[1]
    # We check that we are still within the boundaries of the array
    if x - 1 < 0 or x + 1 >= nbrRows or y - 1 < 0 or y + 1 >= nbrCols:
        # If not, we skip to the next A
        continue
    # We define the coordinates of the diagonals first neighbours
    topL = rawWordSearchArray[x - 1, y - 1]
    topR = rawWordSearchArray[x - 1, y + 1]
    botL = rawWordSearchArray[x + 1, y - 1]
    botR = rawWordSearchArray[x + 1, y + 1]
    # We search for 1 of the 4 patterns that work
    if (
        (topL, botR) in [('S', 'M'), ('M', 'S')] and
        (topR, botL) in [('S', 'M'), ('M', 'S')]
    ):
        # If it matches one, then we add 1 to our total counter
        totalXMasCounter += 1

# We now have the final answer
print(f"The total number of X-MAS is : {totalXMasCounter}")
