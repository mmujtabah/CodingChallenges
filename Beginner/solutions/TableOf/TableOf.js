var number = parseInt(prompt("Enter the number to take the table of:"))
// parseInt is a function which converts string into integer.
for (let i = 1; i <= 10; i++) {
    console.log(`${number} x ${i} = ${number * i}`)
    // Use `` to make a python like f string format.
    // Use ${ur variable name} to put a  variable in string.
}