document.addEventListener('DOMContentLoaded', function() {
    const locationInput = document.getElementById('locationInput');
    const searchButton = document.getElementById('searchButton');
    const errorMessage = document.getElementById('errorMessage');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const weatherInfo = document.getElementById('weatherInfo');
    const locationName = document.getElementById('locationName');
    const temperature = document.getElementById('temperature');
    const condition = document.getElementById('condition');
    const humidity = document.getElementById('humidity');

    async function getWeather(location) {
        try {
            showLoading();
            const response = await fetch('/api/weather/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ location }),
            });

            if (!response.ok) {
                throw new Error(response.status === 503
                    ? 'Weather service is currently unavailable'
                    : 'Failed to fetch weather data'
                );
            }

            const data = await response.json();
            displayWeather(data);
        } catch (error) {
            showError(error.message);
        } finally {
            hideLoading();
        }
    }

    function displayWeather(data) {
        errorMessage.style.display = 'none';
        weatherInfo.classList.remove('hidden');

        locationName.textContent = data.location;
        temperature.textContent = `${data.temp}°C`;
        condition.textContent = data.condition;
        humidity.textContent = `${data.humidity}%`;
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        weatherInfo.classList.add('hidden');
    }

    function showLoading() {
        loadingSpinner.classList.remove('hidden');
        searchButton.disabled = true;
        weatherInfo.classList.add('hidden');
        errorMessage.style.display = 'none';
    }

    function hideLoading() {
        loadingSpinner.classList.add('hidden');
        searchButton.disabled = false;
    }

    searchButton.addEventListener('click', () => {
        const location = locationInput.value.trim();
        if (location) {
            getWeather(location);
        }
    });

    locationInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const location = locationInput.value.trim();
            if (location) {
                getWeather(location);
            }
        }
    });
});