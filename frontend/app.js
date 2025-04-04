document.addEventListener("DOMContentLoaded", function() {  
    fetchTeams();  
});

function fetchTeams() {  
    fetch('http://127.0.0.1:8000/api/teams/')  
        .then(response => {
            // Check if the response is okay (status 200-299)
            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }
            return response.json();  
        })  
        .then(data => {  
            const teamsList = document.getElementById('teams-list');  
            teamsList.innerHTML = '';  // Clear existing content

            // Create a document fragment for better performance
            const fragment = document.createDocumentFragment();

            data.forEach(team => {  
                const teamDiv = document.createElement('div');  
                teamDiv.className = 'team';  
                teamDiv.innerHTML = `
                    <h3>${team.name}</h3>  
                    <p>City: ${team.city}</p>  
                    <p>League: ${team.league}</p>  
                    <p>${team.description}</p>  
                    <a href="reviews.html?teamId=${team.id}">View Reviews</a>  
                `;  
                fragment.appendChild(teamDiv);  // Append to fragment
            });  

            // Append all at once to improve performance
            teamsList.appendChild(fragment);
        })  
        .catch(error => {  
            console.error('Error fetching teams:', error);
            // Optionally, you could display an error message to the user
            const teamsList = document.getElementById('teams-list');
            teamsList.innerHTML = `<p>An error occurred while fetching the teams. Please try again later.</p>`;
        });  
}
