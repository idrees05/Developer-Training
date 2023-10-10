let age = 20; // Change this value for testing
if (age < 18) {
    console.log("Sorry, I can't serve you");
} else {
    console.log("No problem, what would you like to drink?");
}

let password = "myPassword123"; // Change this value for testing
if (password.length < 8) {
    console.log("Password is too short");
} else {
    console.log(password);
}

let number1 = 15; // Change this value for testing
if (number1 % 3 === 0 || number1 % 5 === 0) {
    console.log("This number is divisible by 3 or 5");
} else {
    console.log("This number is not divisible by 3 or 5");
}

let number2 = 15; // Change this value for testing
if (number2 % 3 === 0 && number2 % 5 === 0) {
    console.log("fizz buzz");
} else if (number2 % 3 === 0) {
    console.log("fizz");
} else if (number2 % 5 === 0) {
    console.log("buzz");
} else {
    console.log(number2);
}
