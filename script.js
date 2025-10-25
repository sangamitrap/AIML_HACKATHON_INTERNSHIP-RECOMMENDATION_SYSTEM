document.addEventListener('DOMContentLoaded', function() {
    const studentForm = document.getElementById('student-form');
    const loading = document.getElementById('loading');
    const recommendations = document.getElementById('recommendations');
    const cardsContainer = document.getElementById('cards-container');

    studentForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Collect form data
        const name = document.getElementById('name').value || 'Anonymous';
        const educationLevel = document.getElementById('education-level').value;
        const preferredLocation = document.getElementById('preferred-location').value;
        const sectorInterest = document.getElementById('sector-interest').value;
        const skills = document.getElementById('skills').value;
        
        // Collect filter data
        const minStipend = document.getElementById('min-stipend').value || '';
        const maxStipend = document.getElementById('max-stipend').value || '';
        const duration = document.getElementById('duration').value;
        const workType = document.getElementById('work-type').value;
        
        const studentProfile = {
            name: name,
            education_level: educationLevel,
            preferred_location: preferredLocation,
            sector_of_interest: sectorInterest,
            skills: skills,
            filters: {
                min_stipend: minStipend,
                max_stipend: maxStipend,
                duration: duration,
                work_type: workType
            }
        };
        
        // Show loading
        loading.classList.remove('hidden');
        recommendations.classList.add('hidden');
        cardsContainer.innerHTML = '';

        // Send to API
        fetch('http://localhost:5000/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(studentProfile)
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading
            loading.classList.add('hidden');
            
            if (data.recommendations && data.recommendations.length > 0) {
                recommendations.classList.remove('hidden');
                displayRecommendations(data.recommendations, name);
            } else {
                recommendations.classList.remove('hidden');
                cardsContainer.innerHTML = '<p class="loading">No recommendations found for your profile.</p>';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            loading.classList.add('hidden');
            recommendations.classList.remove('hidden');
            cardsContainer.innerHTML = '<p class="loading">Error fetching recommendations. Make sure the API is running on localhost:5000.</p>';
        });
    });

    function displayRecommendations(recs, studentName) {
        cardsContainer.innerHTML = `<p style="text-align: center; margin-bottom: 20px; color: #4299e1;">Recommendations for ${studentName}</p>`;
        
        recs.forEach(rec => {
            const card = document.createElement('div');
            card.className = 'card';
            
            card.innerHTML = `
                <h3>${rec.title}</h3>
                <p class="company">Company: ${rec.company}</p>
                <p>Location: ${rec.location}</p>
                <p>Stipend: ${rec.stipend}</p>
                <p>Duration: ${rec.duration}</p>
                <p class="score">Similarity Score: ${rec.similarity_score.toFixed(3)}</p>
                <button class="view-details-btn" data-link="${rec.link}">View Full Details</button>
            `;
            
            // Make the entire card clickable
            card.addEventListener('click', function() {
                window.open(rec.link, '_blank');
            });
            
            cardsContainer.appendChild(card);
        });
    }
});
