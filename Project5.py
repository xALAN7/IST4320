# Application Development Alan Santos  007793429

def TestScore():
    while True:  #Start an infinite loop to request the appropriate test scores
        #Accept three test scores
        TestScoresInput = input("Enter your three test scores ranging from 0 to 100: ")

        #Clean up input to make floats free from commas or spaces
        try:
            TestScore2 = [float(score) for score in TestScoresInput.replace(",", " ").split()]

            #Verify the number of test scores
            if len(TestScore2) != 3:
                print("Please input three (3) test scores only.")
                continue  #Restarts the loop if requirement is not met

            # Verify test score ranges
            if all(0 <= score <= 100 for score in TestScore2):
                return TestScore2  #Returns the correct test scores
            else:
                print("Sorry.The test scores must be between 0 and 100. Try again.")

        except ValueError:  #Outputs if no numbers are present
            print("Invalid input. Please enter numerical values only.")

#Prints the scores
TestScore3 = TestScore()
print("The valid test scores are:", TestScore3)

#Calculate and print the average of the three tests scores
TestScoreAverage = sum(TestScore3) / len(TestScore3)
print("Average score:", TestScoreAverage)
if TestScoreAverage >= 90 and TestScoreAverage <= 100:
    LetterGradeAverage = 'A'
elif TestScoreAverage >= 80 and TestScoreAverage <= 90:
    LetterGradeAverage = 'B'
elif TestScoreAverage >= 70 and TestScoreAverage <= 80:
    LetterGradeAverage = 'C'
elif TestScoreAverage >= 60 and TestScoreAverage <= 70:
    LetterGradeAverage = 'D'
else:
    print(score, '= F')

#Print the average score with the letter grade
print(f"Average score with letter grade: {TestScoreAverage} = {LetterGradeAverage}")

#Adds a space the output above and below
print("")

print("Individual test scores with their letter grade:")
# Prints the letter grade equivalent for each score individually
for score in TestScore3:
    if score >= 90 and score <= 100:
        print(score, '= A')
    elif score >= 80 and score <= 90:
        print(score, '= B')
    elif score >= 70 and score <= 80:
        print(score, '= C')
    elif score >= 60 and score <= 70:
        print(score, '= D')
    else:
        print(score, '= F')
        