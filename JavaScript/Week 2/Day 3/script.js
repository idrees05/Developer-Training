document.addEventListener("DOMContentLoaded", function() {
    const fullName = document.getElementById('name');
    const saveButton = document.getElementById('save');
    const entriesList = document.getElementById('entriesList');

    saveButton.addEventListener('click', saveToLocalStorage);
    displayFromLocalStorage();

    function saveToLocalStorage() {
        let names = JSON.parse(localStorage.getItem('names') || "[]");
        names.push(fullName.value);
        localStorage.setItem('names', JSON.stringify(names));
        displayFromLocalStorage();
    }

    function displayFromLocalStorage() {
        let names = JSON.parse(localStorage.getItem('names') || "[]");
        entriesList.innerHTML = '';
        names.forEach(name => {
            let li = document.createElement('li');
            li.textContent = name;
            entriesList.appendChild(li);
        });
    }
});


function extractCharacter(string, index, num) {
    // Using substr to extract 'num' characters starting from 'index'
    return string.substr(index, num);
}

// Example usage:
const result = extractCharacter("Hello, World!", 7, 5);
console.log(result); // Outputs "World"
