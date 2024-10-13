function reverseString(string) {
    return string.split('').reverse().join('')
}

var thestring = prompt("Enter a string to check if it is Palindrome or not:")

if (reverseString(thestring) == thestring) {
    console.log("Palindrome")
}
else {
    console.log("Not Palindrome")
}

// Explanation
// We made a function `reverseString` to reverse the string and return it.
// Then in the function we first used `split` function to make it an array.
// Then we reversed the array using `reverse` function.
// Then we used `join` function to again make the string out of the array by joining each array element 
// without any space( blank string '' )