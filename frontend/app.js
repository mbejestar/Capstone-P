document.addEventListener("DOMContentLoaded", function() {  
    fetchTeams();  
});  

function fetchTeams() {  
    fetch('http://127.0.0.1:8000/api/teams/')  
        .then(response => response.json())  
        .then(data => {  
            const teamsList = document.getElementById('teams-list');  
            teamsList.innerHTML = '';  

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
                teamsList.appendChild(teamDiv);  
            });  
        })  
        .catch(error => {  
            console.error('Error fetching teams:', error);  
        });  
}  
