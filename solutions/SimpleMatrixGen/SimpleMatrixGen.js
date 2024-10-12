// Solution for Challenge "SimpleMatrixGen"

// Function showMatrix
function showMatrix(matrix) {
    // Displays a matrix
    matrix.forEach(row => { // Grabs every row of matrix
        console.log(row.toString()); // Then displays it
    });
}

let rows = parseInt(prompt("Enter number of rows: ")); // Gets number of rows in integer format.
let columns = parseInt(prompt("Enter number of columns: ")); // Gets number of columns in integer format.
// parseInt() function changes the given input into integer
// If there is no integer, such as inputs like "hello" will result in error.

console.log(`Generating Matrix of ${rows} x ${columns}`);
// Displays what matrix is being generated

let matrix = []; // Initialized Blank Array for Matrix
for (let i = 0; i < rows; i++) { // Grabs every row of matrix according to given rows.
    let row = []; // Initializes a blank array for row
    for (let j = 0; j < columns; j++) { // Takes every column of the row according to given columns
        row.push(0); // Inserts the value 0 for now.
    }
    matrix.push(row); // Inserts the generated row in the matrix.
}

showMatrix(matrix); // Displays the matrix

console.log("Now enter the values of matrix. Pattern : ({row} , {column})");
// Displays Pattern of which values should be entered
// (row , column)

for (let row = 0; row < matrix.length; row++) { // Grabs every row of matrix
    for (let column = 0; column < matrix[row].length; column++) { // Then grabs every column/element of that row
        let value = parseInt(prompt(`Enter value for (${row},${column}) :`)); // Gets value as integer from user
        matrix[row][column] = value; // Inserts the value in the specific place.
        // matrix[row] is the specific row of matrix we are currently looping/iterating through.
        // matrix[row][column] is the specific element/column of row we are setting the value of.
    }
}

showMatrix(matrix); // FINALLY DISPLAYS THE MATRIX AND EXITS.
