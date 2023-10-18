function saveData() {
    const inputData = document.getElementById("dataInput").value;
    if (inputData) {
        const currentTime = new Date().toISOString();  // Use current time as a unique key
        localStorage.setItem(currentTime, inputData);
        displayData();
        document.getElementById("dataInput").value = "";  // Clear input after saving
    }
}

function displayData() {
    const savedDataList = document.getElementById("savedDataList");
    savedDataList.innerHTML = "";  // Clear current list
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        const value = localStorage.getItem(key);
        const listItem = document.createElement("li");
        listItem.textContent = value;
        savedDataList.appendChild(listItem);
    }
}

window.onload = function() {
    displayData();  // Display saved data on page load
}
