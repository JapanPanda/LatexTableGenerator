import pyperclip

def main():
    print("Latex Table Generator v0.1")
    print("This script will generate a customizable table.") # For now only truth tables
    blankTable = getInput()
    copy = input("Would you like to copy to clipboard? Y/N\n>> ")
    if copy == "Y":
        pyperclip.copy(blankTable)
    return 0

def getInput():
    tableChoice = input("What type of table would you like:\n1. Regular\n2. Truth\n3. Customizable\n>> ")
    if tableChoice == "1" or tableChoice.lower() == "regular":
        return regTableGenerator()
    elif tableChoice == "2" or tableChoice.lower() == "truth":
        return truthTableGenerator()
    elif tableChoice == "3" or tableChoice.lower() == "customizable":
        return customTableGenerator()

class LatexTable():
    """Latex Table Class"""
    def __init__(self):
        self.table = ""
        self.maxpadding = 0
        self.type = 0
        self.columns = 0
        self.colMatrix = []
        self.colTitleList = []


def regTableGenerator():
#     \begin{table}[]
# \begin{tabular}{|c|l|l|}
# \hline
# p                       & q & p or q \\ \hline
# T                       & T & T      \\ \hline
# T                       & F & T      \\ \hline
# F                       & T & T      \\ \hline
# \multicolumn{1}{|l|}{F} & F & F      \\ \hline
# \end{tabular}
# \end{table}
    columns = int(input("How many columns in your table?\n>> "))
    table = "\\begin{table}[]\n\\begin{tabular}{"
    if columns != 0:
        table += "|c|"
        for i in range(columns - 1):
            table += "c|"
    table += "}\n\hline"
    return

def customTableGenerator():
    return

def truthTableGenerator():
    outputTable = LatexTable()
    outputTable.type = 2
    outputTable.table = "\\begin{displaymath}\n\\begin{array}{"
    outputTable.columns = getNumColumns(outputTable)
    outputTable.colTitleList = getColTitles(outputTable)
    getMainBody(outputTable)
    outputTable.table += "\end{array}\n\end{displaymath}\n"
    print("Preview of the Latex: ")
    print(outputTable.table)
    return outputTable.table

def getMainBody(outputTable):
    colMatrix = []
    max = 0
    for i in range(outputTable.columns):
        print("Please enter the values for Column " + outputTable.colTitleList[i] + ". Enter /q to exit.")
        count = 1
        colValues = []
        while True:
            colValue = input("Column " + outputTable.colTitleList[i] + " Entry " + str(count) + ": ")
            count += 1
            if colValue == "/q":
                break
            else:
                outputTable.maxpadding = len(colValue) if outputTable.maxpadding < len(colValue) else outputTable.maxpadding
                colValues.append(colValue)

        colMatrix.append(colValues)
        max = len(colValues) if max < len(colValues) else max


    for i in range(len(outputTable.colTitleList)):
        outputTable.table += outputTable.colTitleList[i]
        for x in range(outputTable.maxpadding - len(outputTable.colTitleList[i])):
            outputTable.table += " "
        outputTable.table += " & "
    outputTable.table = outputTable.table[:len(outputTable.table) - 2]
    outputTable.table += "\\\\\n\hline\n"
    for i in range(max):
        for j in range(len(colMatrix)):
            if i >= len(colMatrix[j]):
                for x in range(outputTable.maxpadding):
                    outputTable.table += " "
                outputTable.table += " & "
            else:
                outputTable.table += colMatrix[j][i]
                for x in range(outputTable.maxpadding - len(colMatrix[j][i])):
                    outputTable.table += " "
                outputTable.table += " & "
        outputTable.table = outputTable.table[:len(outputTable.table) - 2] + "\\\\\n"

def getNumColumns(outputTable):
    columns = int(input("How many columns in your table?\n>> "))
    if columns != 0:
        outputTable.table += "|c|"
        for i in range(columns - 1):
            outputTable.table += "c|"
    outputTable.table += "}\n"
    return columns

def getColTitles(outputTable):
    print("Please define the column titles. (If needed, use the appropriate latex symbol, ex: logical or is \\lor)")
    columnTitleList = []
    for i in range(outputTable.columns):
        title = input("Column " + str(i + 1) + ": ")
        columnTitleList.append(title)
        outputTable.maxpadding = len(title) if outputTable.maxpadding < len(title) else outputTable.maxpadding
    return columnTitleList

if __name__ == "__main__":
    main()
