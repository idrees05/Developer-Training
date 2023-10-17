// // Ensure the document is fully loaded before executing our script
// document.addEventListener('DOMContentLoaded', function() {
//     // Change the text of the h1 element with id 'myHeader'
//     document.getElementById('myHeader').textContent = 'JavaScript DOM';

//     // Change the text of h2 and h3 elements with class 'sameClass'
//     let headers = document.querySelectorAll('.sameClass');
//     headers.forEach(header => {
//         header.textContent = 'Text Changed using JS';
//     });

//     // Change the text of all three paragraphs
//     let paragraphs = document.querySelectorAll('p');
//     paragraphs.forEach((paragraph, index) => {
//         paragraph.textContent = `This is the modified text for paragraph ${index + 1}.`;
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    // Select the div using its ID
    let targetDiv = document.getElementById('targetDiv');

    // Create a new h1 element
    let newH1 = document.createElement('h1');
    newH1.textContent = "New Text for H1";

    // Change the font size, text and background color
    newH1.style.fontSize = "24px";       // Font size
    newH1.style.color = "white";         // Text color
    newH1.style.backgroundColor = "blue"; // Background color

    // Append the h1 to the div
    targetDiv.appendChild(newH1);
});
