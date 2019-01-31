import pyperclip

def main():
    print("Latei Table Generator v0.1")
    print("This script will generate a customizable table.") # For now only truth tables
    blankTable = getInput()
    return 0

def getInput():
    tableChoice = input("What type of table would you like:\n1. Truth\n2. Customize\n>> ")
    if tableChoice == "1" or tableChoice.lower() == "truth":
        return truthTableGenerator()

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
    for i in range(columns):
        title = input("Column " + str(i + 1) + ": ")
        columnTitleList.append(title)
        table += title + " & "
    table = table[:len(table) - 2]
    table += "\\\\\n\hline\n"
    colMatrix = []
    max = 0
    for i in range(columns):
        print("Please enter the values for Column " + columnTitleList[i] + ". Enter /q to exit.") # TODO: Dynamic column names (list of column titles)
        count = 1
        colValues = []
        while True:
            colValue = input("Column " + columnTitleList[i] + " Entry " + str(count) + ": ")
            count += 1
            if colValue == "/q":
                break
            else:
                colValues.append(colValue)

        colMatrix.append(colValues)
        max = len(colValues) if max < len(colValues) else max

    for i in range(max):
        for j in range(len(colMatrix)):
            if i >= len(colMatrix[j]):
                table += "  & "
            else:
                table += colMatrix[j][i] + " & "
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
