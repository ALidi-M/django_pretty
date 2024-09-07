function toggleTemperature() {
    console.log('Toggle button clicked'); // Debugging log
    const elements = document.querySelectorAll('.temperature');
    elements.forEach(element => {
        console.log('Processing element:', element.innerText); // Debugging log
        const currentTemp = parseFloat(element.innerText);
        if (element.dataset.unit === 'F') {
            const newTemp = ((currentTemp - 32) * 5 / 9).toFixed(2);
            element.innerText = newTemp + '° C';
            element.dataset.unit = 'C';
        } else {
            const newTemp = ((currentTemp * 9 / 5) + 32).toFixed(2);
            element.innerText = newTemp + '° F';
            element.dataset.unit = 'F';
        }
        console.log('New temperature:', element.innerText); // Debugging log
    });
}