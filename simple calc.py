##Cs4051

marks = [] #array list for the user to input numerical values when question shows.

print("Here is a simple system to calculate the students marks, Please enter each students marks one a time then type 'done' once completed")


def Question4Marks():
    while True:                 # Used a while true loop to continuasly ask for the next students marks
        Question = input("List of a students marks: ") # Asks for a list of a students marks and user can input numerical values
        if Question.lower() == "done": # if Question is lowercase done then break the loop
            break
        if "," in Question:
            ques = Question.split(",")
            for que in ques:
                if que.strip().isdigit():
                    marks.append(int(que.strip()))
        elif Question.isdigit(): # if question is a digit add to the array list "marks"
            marks.append(int(Question))
        else:                   # else say please entere a number or 'done'
            print("Please either enter a number or multiple, please type 'done' when finished.")


Question4Marks()

# Prints the message "Students marks: " followed by the array list.
print("Student marks:", marks)

def checknumbs():
    while True:
        if len(marks) >= 2: #If the length of the list is greater or equal to 2 show menu and break loop.
            menufunct()
            break
        else: ## else prints message to tell user to put more than 1 set of numbers. 
            print("Please enter more than 1 set of numbers")
            marks.clear()       ##Clears the list
            Question4Marks()       ##Repeats questions to fill the list back up

numbs = len(marks)              ##Simple definition to help fast coding

print(f"you have entered {numbs} numbers")  ##Prints the following message followed by the defined length of the list.

def mean():                     ##Definition to calculate the mean using the sum of the list divided by the length of the list.
    return sum(marks) // numbs

def median():                   ##Definition to calculate the median.
    marks.sort()                ##Sorts the list from smallest to largest.
    numbs                       ##Calls previous def of the length of the list
    if numbs % 2 == 0:          ## if the length of the list has a remainder of 2 when devided by 2 equal it to 0
        return (marks[numbs//2 - 1] + marks[numbs//2]) /2   
    else:
        return marks[numbs//2]

def goback():                   ##Definition to quickly clear the list and repeat initial questioning to fill it back up.
    marks.clear()
    Question4Marks()

def stndsDevWskewness():        ##definition to calculate skewness and standard deviation   
    minus = [mark - mean() for mark in marks]       ##minus = list - meanOfTheList and names it mark
    sqMin = [mark ** 2 for mark in minus]           ##sqMin = marks to sqr of 2 and takes info from "mark"
    fmsqdev = sum(sqMin)                            ##fmsqdev = sum of the new list "sqMin"
    minusNdev = fmsqdev / numbs                     ##minusNdev = sum of sqMin divided by the length of the origional list
    res = minusNdev ** 0.5                          ## minusNdev square rooted to 0.5 = res

    skew1 = (mean()) - ((median()))                 ##skew1 = the mean of the origional list - the median of the origional list
    skew2 = 3 * skew1                               ##skew2 = 3 times skew1
    skewness = skew2 / res                          ##skewness = skew2 divided by res

    floatconv = float(skewness)                     ##converts skewness to a float
    print(f"The skewness is: {floatconv}")


def menufunct():
    while True:         ## Prints each section followed by their defined names. e.g print(one)
        one = "1. Prints the mean of the numbers"
        two = "2. Prints the median of the numbers"
        three = "3. Prints the mode of the numbers"
        four = "4. Prints the skewness"
        five = "5. Go back and enter a new set of numbers"
        six = "6. Add more numbers to the list"
        seven = "7. Export the list data"
        eight = "8. Open & read a data file"
        nine = "9. Exit the application"
        
        print(one)
        print(two)
        print(three)
        print(four)
        print(five)
        print(six)
        print(seven)
        print(eight)
        print(nine)

        menu = int(input(""))       ##defined menu as an input field and converts it to integer.

        if menu == 1:               ##Same method is used all down the list but if the user inputted 1, then contintinue.               
            print(f"The mean is {float(mean())}")
        elif menu == 2:             ##Else if the user inputted 2 continue. if not go down list until so.
            print(f"The median is {median()}")
        elif menu == 3:             ##removes duplicates, find the highest count in the list which would find the mode.
            print(f"The mode is {max(set(marks), key=marks.count)}")
        elif menu == 4:
            stndsDevWskewness()
        elif menu == 5:
            goback()
            print("Student marks:", marks)
            checknumbs()
        elif menu == 6:
            Question4Marks()
            print("Student marks:", marks)
        elif menu == 7:
            exportCData()
        elif menu == 8:
            openData()
        elif menu == 9:
            print("Exiting...")     ##Prints a exit message and breaks the loop.
            break                   
        else:                       ##If user inputted a number out before 1 and after 9 print "invalid: number out of range."
            print("Invalid: Number out of range.")

def exportCData():                  ##Displays "enter the name you want your file named as"
    filename = input("Enter the name you want to set your data file as: (set an extention too e.g .txt) ")
    
    with open(filename, 'w') as file:   ##Takes the entered name from the input before as places it in the variable "filename"
        file.write(", ".join(map(str, marks)))   ##Writes in the file the array list followed by commas seperating numbers. And makes it a string
        print(f"Data has been saved to {filename}")

def openData():
    filename = input("Enter the data file you wish to open: ")
    try:        ##Using try except it takes the inputted text and opens the file with read permittion.
        file = open(filename, 'r')
        data = file.read()  
        print(f"Data from {filename}: ")
        print(data)     ##Prints the contents of the file
        file.close()
    except:             ##If name is invalid print except message, then go back to the menu.
        print("Incorrect file name")
        menufunct()
    

checknumbs()
