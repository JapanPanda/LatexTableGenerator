import pyperclip

def main():
    print("Latex Table Generator v0.1")
    print("This script will generate a customizable table.") # For now only truth tables
    blankTable = getInput()
    return 0

def getInput():
    tableChoice = input("What type of table would you like:\n1. Regular\n2. Truth\n3. Customizable\n>> ")
    if tableChoice == "1" or tableChoice.lower() == "regular":
        return regTableGenerator()
    elif tableChoice == "2" or tableChoice.lower() == "truth":
        return truthTableGenerator()
    elif tableChoice == "3" or tableChoice.lower() == "customizable":
        return customTableGenerator()

def regTableGenerator(): # TODO: Add regular table support
    return

def customTableGenerator():
    return

def truthTableGenerator():
    columns = int(input("How many columns in your table?\n>> "))
    table = "\\begin{displaymath}\n\\begin{array}{"
    if columns != 0:
        table += "|c|"
        for i in range(columns - 1):
            table += "c|"
    table += "}\n"
    print(table)

    # Get the title of the columns
    print("Please define the column titles.")
    columnTitleList = []
    maxpadding = 0
    for i in range(columns):
        title = input("Column " + str(i + 1) + ": ")
        columnTitleList.append(title)
        maxpadding = len(title) if maxpadding < len(title) else maxpadding

    colMatrix = []
    max = 0
    for i in range(columns):
        print("Please enter the values for Column " + columnTitleList[i] + ". Enter /q to exit.")
        count = 1
        colValues = []
        while True:
            colValue = input("Column " + columnTitleList[i] + " Entry " + str(count) + ": ")
            count += 1
            if colValue == "/q":
                break
            else:
                maxpadding = len(colValue) if maxpadding < len(colValue) else maxpadding
                colValues.append(colValue)

        colMatrix.append(colValues)
        max = len(colValues) if max < len(colValues) else max

    for i in range(len(columnTitleList)):
        table += columnTitleList[i]
        for x in range(maxpadding - len(columnTitleList[i])):
            table += " "
        table += " & "
    table = table[:len(table) - 2]
    table += "\\\\\n\hline\n"
    for i in range(max):
        for j in range(len(colMatrix)):
            if i >= len(colMatrix[j]):
                for x in range(maxpadding):
                    table += " "
                table += " & "
            else:
                table += colMatrix[j][i]
                for x in range(maxpadding - len(colMatrix[j][i])):
                    table += " "
                table += " & "
        table = table[:len(table) - 2] + "\\\\\n"
    table += "\end{array}\n\end{displaymath}\n"
    print("Preview of the Latex: ")
    print(table)
    copy = input("Would you like to copy to clipboard? Y/N\n>> ")
    if copy == "Y":
        pyperclip.copy(table)
    return

if __name__ == "__main__":
    main()
