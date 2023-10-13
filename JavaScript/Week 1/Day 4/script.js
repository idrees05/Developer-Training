// Functions

// Learning Objectives:

// - To explore functions and look at how they work
// - To incorporate functions into our code
// - To recognise the different types of function syntax


// Delcaring a Function:
function greeting() {
    console.log("Hello World")
}
// Function declarations / expressions allow us to call a function before is has been defined

// Calling / Invoking a function:
greeting()

// User Status Function
let userOnline = false

function userStatus() {
    if (!userOnline) {
        userOnline = true
        console.log("User Signed-In!")
    } else {
        userOnline = false
        console.log("User Signed-Out!")
    }
}

userStatus()

// Parameters and Arguments
function add(num1, num2) {
    console.log(num1 + num2)
}

add(10, 20)

// Scope Example
const name = "Lydia"
const age = 21
const city = "San Francisco"

function getPersonInfo() {
    const name = "Sarah"
    const age = 22
    return `${name} is ${age} and lives in ${city}`
}

console.log(getPersonInfo())

// Functions that call other functions
function double(num) {
    return num * 2
}

function quadruple(num) {
    return double(num) * 2
}

console.log(quadruple(10))

// Function Declaration
function squaredDeclaration(number) {
    return number * number
}
console.log(squaredDeclaration(3))
// Arrow Function
const squaredArrow = (number) => {
    return number * number
}
console.log(squaredArrow(4))

// Arrow Function with Implicit Return 
const squaredArrow2 = (number) => number * number

console.log(squaredArrow2(10))

// "Anonymous" function
const squaredAnon = function (number) {
    return number * number
}

console.log(squaredAnon(5))





