# Solution for Challenge "SimpleMatrixGen"

# Function showMatrix
def showMatrix(matrix):
    # Displays a matrix
    for row in matrix: # Grabs every row of matix
        print(str(row)) # Then displays it


rows = int(input("Enter number of rows: ")) # Gets number of rows in integer format. 
columns = int(input("Enter number of columns: "))  # Gets number of columns in integer format. 
# int() function changes the given input into integer
# If there is no integer, such as inputs like "hello" will result in error.


print(f"Generating Matrix of {rows} x {columns}") 
# Displays what matrix is being generated

matrix = [] # Initalizied Blank Array for Matrix
for i in range(rows): # Grabs every row of matrix according to given rows.
    row = [] # Initializes a blank array for row
    for i in range(columns): # Takes every column of the row according to given columns/
        row.append(0) # Inserts the value 0 for now.
    matrix.append(row) # Inserts the generated row in the matrix.

showMatrix(matrix) # Displays the matrix

print("Now enter the values of matrix. Pattern : ({row} , {column})") 
# Displays Pattern of which values should be entered
# (row , column)

for row in range(len(matrix)): # Grabs every row of matrix
    for column in range(len(matrix[row])): # Then grabs every column/element of that row
        value = int(input(f"Enter value for ({row},{column}) :")) # Gets value as integer from user
        matrix[row][column] = value # Inserts the value in the specific place.
        # matrix[row] is the specific row of matrix we are currently looping/iterating through.
        # matrix[row][column] is the specific element/column of row we are setting the value of.

showMatrix(matrix)  # FINALLY DISPLAYS THE MATRIX AND EXITS.