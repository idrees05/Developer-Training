// Task 1: Array of favorite Films/TV shows and looping through them
let favoriteShows = ["Breaking Bad", "The Office", "Stranger Things", "Game of Thrones", "The Mandalorian"];
favoriteShows.push("Friends", "Money Heist");  // Add 2 more items

for (let show of favoriteShows) {
    console.log(show);
}

// Task 2: Generating 10 random numbers between 1-100
for (let i = 0; i < 10; i++) {
    let randomNumber = Math.floor(Math.random() * 100) + 1;
    console.log(randomNumber);
}

// Task 3: Count backwards from 20-0
for (let i = 20; i >= 0; i--) {
    console.log(i);
}

// Task 4: Generate 5 random numbers between 1-50 and check divisibility by 5
for (let i = 0; i < 5; i++) {
    let randomNumber = Math.floor(Math.random() * 50) + 1;
    if (randomNumber % 5 === 0) {
        console.log(`${randomNumber} is divisible by 5.`);
    } else {
        console.log(`${randomNumber} is not divisible by 5.`);
    }
}
