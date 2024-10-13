// Solution for Challenge "GetTheSpeedToReach"

console.log("Welcome to GetTheSpeedToReach Challenge. Select mode for measurement:\n\n");
console.log("\t 1) M/S Meter per second \n \t 2) KM/H Kilometer per hour\n");

const choice = parseInt(prompt("Enter the number of the item you want to choose: "));
// Takes choice as integer

// Initialized blank variables
let distance = 0;
let time = 0;
let speed = 0;
let outputUnit = "";

if (choice === 1) { // Choice for m/s
    console.log("Selected Meter per second. \n");
    outputUnit = "m/s";
    distance = parseFloat(prompt("Enter distance from your destination (meters):"));
    time = parseFloat(prompt("Enter time in which you want to reach there (seconds):"));
} else if (choice === 2) { // Choice for km/h
    console.log("Selected Kilometer per hour.");
    outputUnit = "km/h";
    distance = parseFloat(prompt("Enter distance from your destination (kilometers):"));
    time = parseFloat(prompt("Enter time in which you want to reach there (hours):"));
} else { // Error message
    console.log("WRONG CHOICE. EXITING...");
    exit();
}

// S = vt
// v = S/t After arranging

speed = distance / time; // formula

console.log(`You need ${speed.toFixed(1)} ${outputUnit} speed to reach your destination.`);

// Added .toFixed(1) to the speed so it will only show 1 decimal digit.
