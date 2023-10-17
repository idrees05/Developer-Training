document.addEventListener('DOMContentLoaded', function() {
    const divElement = document.getElementById('hoverDiv');

    // Initial styles
    divElement.style.width = '200px';
    divElement.style.height = '100px';
    divElement.style.backgroundColor = '#eee';
    divElement.style.display = 'flex';
    divElement.style.justifyContent = 'center';
    divElement.style.alignItems = 'center';
    divElement.style.transition = 'background-color 0.3s, width 0.3s, height 0.3s';

    divElement.addEventListener('mouseover', function() {
        divElement.innerText = 'Go away!';
        divElement.style.backgroundColor = 'red';
        divElement.style.width = '300px';
        divElement.style.height = '150px';
    });

    divElement.addEventListener('mouseout', function() {
        divElement.innerText = 'Hover over me!';
        divElement.style.backgroundColor = '#eee';
        divElement.style.width = '200px';
        divElement.style.height = '100px';
    });
});
