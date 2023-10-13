// Properties - Are data or information about the object

// Methods - Are things the object can do

// Using the console object and the log method to log a statment to the console
console.log("Hello World");

// Data Types

// String - Represents characters enclosed in quote marks
console.log("I am string!");

// Number
console.log(100);

// Boolean - True or False
console.log(true);
console.log(false);

// REMEMBER numbers inside quote marks are strings
console.log("1000");

// Null - An abscense of any value 
console.log(null);

// Undefined - Data without a defined type
console.log(undefined);


// Variables in JavaScript:

// var - variable declaration keyword
// AVOID USING VAR!!!

var variable = "Var is a method of declaring variables that you should avoid";

// = - Single Equals - Assignment Operator - Used to asign a value

console.log(variable);

// Let - Method for declaring variables that will change

let changeable = "A value stored in a 'let' variable is able to have its value reassigned";

console.log(changeable);

changeable = "A new value";

console.log(changeable);
console.log(changeable);

// let changeable = "Whatever value"

// Const - for varaible values that wont change

const constant = "A variable that can not be assigned a new value";

console.log(constant);

// We cannot ressign a constant value
// constant = "New Value"

// Properties and Methods

// Properties
let exampleString = "Hello World";

// .length - returns the number of characters in a string
console.log(exampleString.length);

// Methods

// Remember that a methiod must be followed by parenthesis in order to invoke it
console.log(exampleString.toUpperCase());

console.log(exampleString);

// Math Library

// In-built JavaScript Mathematical methods

// Math.random - Generates a psuedorandom number between 0 and 1 
console.log(Math.random());

// Multiplying the Math.random result by 10 gives us a number between 1-10 still with decimals
console.log(Math.random() * 10);

// Math.round - rounds thew result to a whole number
console.log(Math.round(Math.random() * 10));

// .ceil always rounds up
console.log(Math.ceil(Math.random() * 10));

// .floor always rounds down
console.log(Math.floor(Math.random() * 10));

// Accessing Variables / Template Literals
let firstName = "Christian";
let lastName = "Perry";

console.log(firstName);
console.log(lastName);

console.log("My name is" + firstName + lastName);

console.log("My name is" + " " + firstName + " " + lastName);

// Template Literals 
console.log(`My name is ${firstName} ${lastName}.`);








