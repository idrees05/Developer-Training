// Task 1: Personalised Greeting
function greet(name) {
    console.log(`Hello, ${name}! How are you today?`);
}

// Task 2: Odd or Even Checker
function isOddOrEven(number) {
    if (number % 2 === 0) {
        console.log("The number is even.");
    } else {
        console.log("The number is odd.");
    }
}

// Task 3: ATM Functionality
const accountBalance = 5000;  // example balance
const storedPin = 1234;       // example pin

function atm(pin, withdrawalAmount) {
    if (pin !== storedPin) {
        console.log("Incorrect PIN. Transaction denied.");
    } else if (withdrawalAmount > accountBalance) {
        console.log("Insufficient funds. Transaction denied.");
    } else {
        console.log("Transaction approved.");
    }
}

// Arrow functions
// Arrow functions were introduced in ECMAScript 6 (ES6). They offer a shorter syntax to write function expressions. 
// They don't have their own 'this' value. 

// Single parameter arrow function without parentheses:
const greetArrow = name => console.log(`Hello, ${name}!`);

// Single expression arrow function with implicit return:
const isEven = num => num % 2 === 0;

// Converting function declaration to arrow function:
const isOddOrEvenArrow = number => {
    if (number % 2 === 0) {
        console.log("The number is even.");
    } else {
        console.log("The number is odd.");
    }
}
