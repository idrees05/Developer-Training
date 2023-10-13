// Objects

// Learning Objectives:
// - Explore the concept of an Object
// - To access data from within an object
// - To use functions (methods) with Objects

// Properties - Data contained within an object
// Methods - Things that the object can do

// Object Syntax
// Key:Value - Pairs
const person = {
    name: "Christian",
    age: 31
}

// CoffeeShop
const coffeeShop = {
    name: "Costa",
    branchNumber: 250,
    specialOffers: true,
    drinks: [
        "Americano",
        "Latte",
        "Tea"
    ]
}

console.log(coffeeShop)

// Accessing Data using dot notation
console.log(coffeeShop.name)

// Accessing Data using bracket notation
console.log(coffeeShop["branchNumber"])

// Combining dot and bracket notation
console.log(coffeeShop.drinks[0])

// Add items to an existing object
coffeeShop.muffins = ["Blueberry", "Chocolate"]
console.log(coffeeShop)

// Overwrite / Change data in an existing object
coffeeShop.branchNumber = 100
console.log(coffeeShop)

// Add special offers
coffeeShop.breakfastOffer = "Free Bagel with any coffee!"
coffeeShop.lunchOffer = "Free coffee with any Sandwich!"

let offer = "No current offer"
let time = 1000

if (time < 1100) {
    offer = coffeeShop.breakfastOffer
    console.log(offer)
} else if (time < 1500) {
    offer = coffeeShop.lunchOffer
    console.log(offer)
}

// Methods
coffeeShop.open = function () {
    return "We are open come on in!"
}

console.log(coffeeShop.open())

coffeeShop.close = function () {
    return "Sorry we are closed come back tomorrow!"
}

console.log(coffeeShop.close())

console.log(coffeeShop)

// Alarm Object
const alarm = {
    weekendAlarm: "Sleep in its the weekend!",
    weekdayAlarm: "Get up at 7:00am.",
    checkDay: function (day) {
        if (day === "Saturday" || day === "Sunday") {
            return this.weekendAlarm
        } else {
            return this.weekdayAlarm
        }
    }
}

console.log(alarm.checkDay("Saturday"))


// Nested Objects 
const employee = {
    id: 1,
    name: 'John Doe',
    position: 'Software Engineer',
    department: {
        name: 'Engineering',
        location: 'Building A',
        supervisor: {
            name: 'Jane Smith',
            position: 'Engineering Manager'
        }
    }
}

const library = {
    name: 'Public Library',
    location: 'City Center',
    books: [
        {
            id: 'B001',
            title: 'The Great Gatsby',
            author: 'F. Scott Fitzgerald',
            details: {
                genre: 'Fiction',
                year: 1925
            }
        },
        {
            id: 'B002',
            title: 'To Kill a Mockingbird',
            author: 'Harper Lee',
            details: {
                genre: 'Fiction',
                year: 1960
            }
        }
    ]
};