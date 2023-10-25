
const apiKey = '3e743b2fa21423765bf031ce19d399a6';

document.getElementById('fetch-weather').addEventListener('click', function() {
    const city = document.getElementById('city-input').value;
    const apiUrl = `http://api.weatherstack.com/current?access_key=${apiKey}&query=${city}`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                throw new Error(data.error.info);
            }

            document.getElementById('city-name').innerText = data.location.name;
            document.getElementById('temperature').innerText = `${data.current.temperature}°C`;
            document.getElementById('description').innerText = data.current.weather_descriptions[0];
            document.getElementById('weather-icon').src = data.current.weather_icons[0];
            document.getElementById('weather-icon').style.display = 'block';

            // In a real-world scenario, here we would also update the canvas graph with relevant weather data
        })
        .catch(error => {
            document.getElementById('error-message').innerText = `Error: ${error.message}`;
        });
});

