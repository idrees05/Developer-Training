document.addEventListener('DOMContentLoaded', function() {
    const nameDisplay = document.getElementById('nameDisplay');
    const firstNameInput = document.getElementById('firstName');
    const lastNameInput = document.getElementById('lastName');
    const saveButton = document.getElementById('saveButton');

    saveButton.addEventListener('click', function() {
        const fullName = `${firstNameInput.value} ${lastNameInput.value}`;
        nameDisplay.textContent = fullName;
    });
});
