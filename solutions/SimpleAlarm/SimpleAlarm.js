// Solution for Challenge "SimpleAlarm"

console.log("Please choose a unit for timer: "); // Asks user for choice of measurement
console.log("\t 1) Seconds");
console.log("\t 2) Minutes");

const choice = parseInt(prompt("Enter the choice number : ")); // Gets the choice number given by user.
// Uses parseInt to convert it into integer format.

let timeInSeconds = 0; // Blank variable initialization

if (choice === 1) { // If user chooses seconds
    timeInSeconds = parseInt(prompt("Enter the time in seconds (do not use decimals): "));
} else if (choice === 2) { // If user chooses minutes
    timeInSeconds = parseInt(prompt("Enter the time in minutes (do not use decimals): ")) * 60;
    // Multiplied by 60 as 1 minute = 60 seconds
    // So it will be converted into seconds for our use.
} else {
    console.log("WRONG CHOICE\n Exiting...");
    // Exits the program if wrong number is entered.
    exit();
}

let i = 0;
// setInterval function syntax
// setInterval( function here , time in milli seconds)

const interval = setInterval(() => {
    console.log(`Remaining Time: ${timeInSeconds - i} seconds.`);
    // timeInSeconds is the time given. "i" is the current time.
    // Time remaining will be total time - current time
    i++; // Increase i by 1.
    if (i >= timeInSeconds) { // When current time becomes equal total time.
        clearInterval(interval); // Clears this executation if time is over.
        console.log("Time is over."); // Displays message that time is over.
    }
}, 1000); // It will execute this after every one second.
