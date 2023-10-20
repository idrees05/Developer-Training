let callCounter = 0;
let interval;

function callFunctionTenTimes() {
    if (callCounter < 10) {
        console.log("Function called!");
        callCounter++;
    } else {
        clearInterval(interval);
        console.log("Calling of function is cancelled.");
    }
}

interval = setInterval(callFunctionTenTimes, 200); // Calling the function every 200 milliseconds
