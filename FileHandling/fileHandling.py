import os

def get_path_to_current_dir(path) -> str:
    return f"{os.path.dirname(os.path.abspath(path))}{os.sep}"

def get_amount_of_lines_in_file(filepath):
    line_count = 0

    with open(filepath, "r") as file:
        for _ in file:
            line_count += 1

    return line_count

def read_file(filepath):

    '''
    Parameter should be filepath + filename and extension.\n
    Reads a txt file at specified location.\n
    \n
    Returns a list with contents of file in type str.\n
    '''

    with open(filepath) as file:
        fileLines = file.readlines()
    return fileLines

def add_text_to_file(filepath, lineToAdd):
    
    '''
    Adds text to the specified file
    Does not add a linebreak to parameter string "lineToAdd"
    '''

    if os.path.isfile(filepath):
        with open(filepath, 'a') as file:
            file.write(lineToAdd)
    else:
        raise Exception("Failed to write to the file.")

def get_line_number_from_file(filepath, stringToSearchFor):

    '''
    Returns a list with all the places lineToSearchFor was equal to the index of the file
    Returns a list with integers
    '''

    file = read_file(filepath)
    splitList = []
    for line in file:
        splitList.append((line.split("\n"))[0])

    lineNumberList = []
    for i in range(len(file)):
        if str(stringToSearchFor) == str(splitList[i]):
            lineNumberList.append(i)
    
    return lineNumberList

def replace_line_in_file(filepath, lineNumber, lineToAdd):

    '''
    Deletes old file and creates a new file with the wanted changes.\n
    Remember that file has start index 0.\n
    Adds a breakline after lineToAdd.
    '''

    document = read_file(filepath)
    lineToAdd = lineToAdd + "\n"
    
    for i in range(lineNumber):
        document[lineNumber] = lineToAdd
    
    os.remove(filepath)
    open(filepath, "x")

    for i in range(len(document)):
        add_text_to_file(filepath, document[i])

def check_if_string_in_file_exists(filepath, stringToSearchFor):

    '''
    Returns true if stringToSearchFor exists the given file.\n
    Removes linebreak so stringToSearchFor should not contain linebreak.
    '''

    file = read_file(filepath)

    fileOutput = []

    for line in file:
        fileOutput.append(line.split("\n"))

    stringExist = False

    for outputString in fileOutput:
        if outputString[0] == stringToSearchFor:
            stringExist = True

    return stringExist