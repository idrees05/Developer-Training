// Conditions in JavaScript 

// == - Double equals checks if the values either side of it are equal.

// leftValue == rightValue 

// Is the value of the weather variable equal to a string of "Sunny"
// console.log(weather == "Sunny")

// An if statement evaluates a condtion and runs the relevant code block depending onf whether it is true or false

// If / Else 
let weather = "Foggy";

if (weather === "Sunny") {
    console.log("Bring your sunglasses!");
} else if (weather === "Rain") {
    console.log("Grab an umbrella.");
} else if (weather === "Snow") {
    console.log("It's Snowing!");
} else {
    console.log("I'm not sure maybe bring a jacket.");
};

// Comparison Operators 

// == - Equal To
let a = "10";
console.log(a == 10);
// != - Not Equal to
console.log(a != 10);

// === - Strictly Equal To
// Checks the value and the data type
console.log(a === 10);
// !== - Not Equal Value or Equal Data Type
console.log(a !== 10);

// > - Greater Than

// < - Less Than

// >= - Greater than or equal to

// <= - Less than or equal to

// Logical Operators:

// || - or

// && - and

// ! - not

// Traffic Light Example
let trafficLight = "Amber";

// If the traffic light is on red or amber log "Stop" to the console.
if (trafficLight === "Red" || trafficLight === "Amber") {
    console.log("Stop!");
} else {
    console.log("Go!");
};

// if (trafficLight !== "Green") {
//     console.log("Stop!");
// } else {
//     console.log("Go!");
// };

// Number Comparison

let num = 12;

if (num > 5 && num <= 10) {
    console.log(`${num} is between 5 and 10`);
} else {
    console.log(`${num} is NOT between 5 and 10`);
};


// Switch Statement

let day = "Monday";

switch (day) {
    case "Monday":
        console.log("Weekend is over. Happy Monday!")
        break;
    case "Tuesday":
        console.log("Second day of the week!")
        break;
    case "Wednesday":
        console.log("Halfway through the week!")
        break;
    case "Thursday":
        console.log("It's almost Friday!")
        break;
    case "Friday":
        console.log("Happy Friday!")
        break;
    default:
        console.log("It's the weekend!")
};


// Switch Statement 2 - Grade Example

let testScore = 40

switch (true) {
    case testScore >= 70:
        console.log("Distinction")
        break;
    case testScore >= 60:
        console.log("Merit")
        break;
    case testScore >= 50:
        console.log("Pass")
        break;
    default:
        console.log("Failed")
};
