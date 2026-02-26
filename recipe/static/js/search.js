// search.js - FIXED VERSION (Django-safe)

document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    const recipeContainer = document.getElementById('recipeContainer');
    const cards = document.querySelectorAll('.card');

    if (!searchInput || !recipeContainer) return;

    searchInput.addEventListener('input', function () {
        const query = this.value.toLowerCase().trim();
        let foundResults = false;

        // Filter cards
        cards.forEach(card => {
            const recipeName = card.querySelector('h2')?.textContent.toLowerCase() || "";
            const recipeDesc = card.querySelector('p')?.textContent.toLowerCase() || "";

            if (recipeName.includes(query) || recipeDesc.includes(query)) {
                card.style.display = 'flex';
                foundResults = true;
            } else {
                card.style.display = 'none';
            }
        });

        // Handle no results
        const existingNoResults = document.querySelector('.no-results');
        if (existingNoResults) existingNoResults.remove();

        if (!foundResults && query.length > 0) {
            const noResults = document.createElement('div');
            noResults.className = 'no-results';
            noResults.innerHTML = `
                <p>No recipes found for "${query}"</p>
                <button class="ask-ai-btn">
                    Ask AI Chef for "${query}"
                </button>
            `;
            recipeContainer.appendChild(noResults);

            // AI button redirect (FIXED)
            noResults.querySelector('.ask-ai-btn').addEventListener('click', () => {
                window.location.href =
                    `${AI_RECIPE_URL}?q=${encodeURIComponent(query)}`;
            });
        }
    });

    // Prevent empty form submission
    if (searchForm) {
        searchForm.addEventListener('submit', function (e) {
            if (searchInput.value.trim() === '') {
                e.preventDefault();
            }
        });
    }
});
