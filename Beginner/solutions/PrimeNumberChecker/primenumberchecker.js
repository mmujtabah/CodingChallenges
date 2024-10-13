// Take user input for the number
const num = parseInt(prompt("Enter the number: "), 10);

// Assume the number is prime unless proven otherwise
let isPrime = true;

// Loop through all numbers from 2 to one less than the input number
// If any number divides the input number evenly, it's not prime
for (let i = 2; i < num; i++) {
    if (num % i === 0) {  // If there's no remainder, num is divisible by i
        isPrime = false;  // Mark the number as not prime
        break;  // Exit the loop since we found a divisor
    }
}

// Check if the number is 1, which is neither prime nor composite
if (!isPrime) {
    console.log("Not Prime");  // If a divisor was found, the number is not prime
} else if (num === 1) {
    console.log("1 is neither prime nor composite");  // Special case for 1
} else {
    console.log("Prime");  // If no divisors were found, the number is prime
}
