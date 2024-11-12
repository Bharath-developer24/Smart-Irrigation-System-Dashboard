document.addEventListener('DOMContentLoaded', function() {
    // Simulate loading sensor data
    setTimeout(function() {
        document.getElementById('soil-moisture').textContent = '45%'; // Replace with actual data
        document.getElementById('temperature').textContent = '25°C'; // Replace with actual data
    }, 1000);

    // Simulate loading recent events
    setTimeout(function() {
        const eventsContainer = document.getElementById('events');
        // Example event data
        const events = [
            { date: '2024-09-05', description: 'Irrigation started at 08:00 AM.' },
            { date: '2024-09-04', description: 'Irrigation ended at 06:00 PM.' }
        ];

        if (events.length > 0) {
            eventsContainer.innerHTML = events.map(event => 
                `<p>${event.date}: ${event.description}</p>`
            ).join('');
        } else {
            eventsContainer.innerHTML = '<p>No recent events.</p>';
        }
    }, 1500);
});
