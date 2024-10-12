// Get the temperature unit from the user and convert it to uppercase for consistency
let tempUnit = prompt("Convert from Celsius or Fahrenheit? Enter 'C' or 'F':").toUpperCase();

// Check if the user wants to convert from Celsius to Fahrenheit
if (tempUnit === 'C') {
    // Prompt the user to enter the temperature in Celsius
    let celsius = parseFloat(prompt("Enter temperature in Celsius:"));
    // Convert Celsius to Fahrenheit using the formula
    let fahrenheit = (celsius * 9 / 5) + 32;
    // Display the converted temperature
    console.log(`${celsius}°C is ${fahrenheit}°F`);

// Check if the user wants to convert from Fahrenheit to Celsius
} else if (tempUnit === 'F') {
    // Prompt the user to enter the temperature in Fahrenheit
    let fahrenheit = parseFloat(prompt("Enter temperature in Fahrenheit:"));
    // Convert Fahrenheit to Celsius using the formula
    let celsius = (fahrenheit - 32) * 5 / 9;
    // Display the converted temperature
    console.log(`${fahrenheit}°F is ${celsius}°C`);

// Handle invalid input cases
} else {
    console.log("Invalid input. Please enter 'C' or 'F'.");
}
