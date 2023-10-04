// This is the script.js file

function showModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "block";
}

function hideModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}

var form = document.getElementById("form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    alert("Thank you for your submission. We will contact you soon.");
    hideModal();
});
