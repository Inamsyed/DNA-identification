import csv
import sys


def main():

    numOfCmdArgs = len(sys.argv)
    if(numOfCmdArgs != 3):
        print("Incorrect Arguments")
      
    listOfPeople = sys.argv[1]
    DNASeqFile = sys.argv[2]
    rows = []
    STRs = []
    L = True

    with open(listOfPeople) as file:
        reader = csv.DictReader(file)
        STRs = reader.fieldnames
        for row in reader:
            rows.append(row)

    with open(DNASeqFile, 'r') as file:
        DNASeq = file.readline().strip()

    for individual in rows:
        for i in range(1 , len(STRs)):
            currentSTR = STRs[i]
            currentSTRCount = int(individual[currentSTR])
            DNASeqSTRCount = int(longest_match(DNASeq , currentSTR))
            if(currentSTRCount != DNASeqSTRCount):
                L = False
        if(L == True):
            print(individual['name'])
            return
        else:
            L = True
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):

        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
