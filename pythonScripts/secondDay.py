# --------------------------- INFORMATION ------------------------------ #

# When solving the second puzzle of one day,
# I never change the code of the first puzzle.
# I can use variables or results from the first one, and that's it.
# I don't think there are rules about this but that's what I'm sticking to.

# --------------------------- PUZZLE NUMBER 1 -------------------------- #

# We create the safe or unsafe list for all the reports
safeOrUnsafe = []

# We open the raw data
with open('../rawData/rawReports.txt', 'r') as doc:
    # For each line in the document...
    for line in doc:
        # We use the spaces to split the numbers
        splitNumbers = line.split()
        # We use map to apply the int function to all the numbers
        # and we convert the whole thing to a list
        report = list(map(int, splitNumbers))

        # We first check that the report is either ascending or descending
        if report == sorted(report) or report == sorted(report, reverse=True):
            # If that's the case, we check that the levels are
            # no more than 3 apart but at least 1 apart
            # We will store True or False in this list for each tested pair
            acceptableDiff = []
            # We iterate over each level and its n+1
            for nbr, nPlusOne in zip(report, report[1:]):
                # If the pair doesn't meet the conditions, we append False
                if abs(nPlusOne-nbr) > 3 or abs(nPlusOne-nbr) < 1:
                    acceptableDiff.append(False)
                # If it does, we append True
                else:
                    acceptableDiff.append(True)

            # We call it safe only if no False are present
            # and we append the result to the final list
            if all(acceptableDiff):
                safeOrUnsafe.append(True)
            else:
                safeOrUnsafe.append(False)

        # If it's not ascending or descending, we directly call it unsafe
        else:
            safeOrUnsafe.append(False)

# We count the number of True in the complete list
totalSafeReports = sum(safeOrUnsafe)
# And this gives us the final answer
print(f"The total number of safe reports is {totalSafeReports}")


# --------------------------- PUZZLE NUMBER 2 -------------------------- #

def isSafe(report: list):
    """ This function tells if a report is safe by checking
    if it matches our criteria.

    It takes a report (a list) as input
    and returns True for safe and False for unsafe.
    """
    # We first check that the report is either ascending or descending
    if report == sorted(report) or report == sorted(report, reverse=True):
        # If that's the case, we check that the levels are
        # no more than 3 apart but at least 1 apart
        # We check each level and it n+1
        for nbr, nPlusOne in zip(report, report[1:]):
            # If it doesn't meet the conditions, we directly return False
            if abs(nPlusOne-nbr) > 3 or abs(nPlusOne-nbr) < 1:
                return False

    # If it's not ascending or descending, we return False too
    else:
        return False

    # But if it passed all the tests, then we can return True
    return True

# Now, we can go through all the reports, and for those which are unsafe,
# try to remove one number at a time


# We open the raw data
with open('../rawData/rawReports.txt', 'r') as doc:

    # For each line in the document...
    for line in doc:
        # We use the spaces to split the numbers
        splitNumbers = line.split()
        # We use map to apply the int function to all the numbers
        # and we convert the whole thing to a list
        report = list(map(int, splitNumbers))
        # If the report is unsafe, we can try to remove one level at a time
        # to see if we can make it safe
        if isSafe(report) is False:
            # We iterate over each individual level
            for i in range(len(report)):
                # We make a temporary copy of the report
                # to avoid modifying the original
                tempReport = report.copy()
                # We delete the level at index i
                tempReport.pop(i)
                # If after the removal of one number it becomes safe,
                # we add one True to our previous list and we can stop here
                if isSafe(tempReport) is True:
                    safeOrUnsafe.append(True)
                    break


# We count the number of True in the complete list
# and this gives us the new final answer
newTotalSafeReports = sum(safeOrUnsafe)
print(f"The total number of safe reports with Problem Dampening enabled is "
      f"{newTotalSafeReports}")
