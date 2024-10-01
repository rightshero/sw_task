// static/your_app/js/script.js

// Fetch the CSRF token from the hidden input
const csrfToken = document.getElementById('csrf_token').value;

// Attach event listeners to the category checkboxes
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.category-checkbox').forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            const categoryId = this.dataset.id;
            const subcategoriesList = this.parentNode.querySelector('.subcategories');

            // If checkbox is checked, fetch subcategories
            if (this.checked) {
                if (subcategoriesList.children.length === 0) {
                    fetchSubcategories(categoryId, subcategoriesList);
                }
                subcategoriesList.classList.add('open');
            } else {
                subcategoriesList.classList.remove('open');
            }
        });
    });
});

// Function to fetch subcategories via AJAX
function fetchSubcategories(categoryId, subcategoriesList) {
    fetch(`/categories/${categoryId}/subcategories/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken  // Include CSRF token in headers
        },
    })
    .then(response => response.json())
    .then(data => {
        // Populate the subcategories with checkboxes in the DOM
        subcategoriesList.innerHTML = data.map(subcat => `
            <li>
                <input type="checkbox" class="category-checkbox" data-id="${subcat.id}">
                <label>${subcat.name}</label>
                <ul class="subcategories"></ul>
            </li>
        `).join('');
        attachCheckboxEventListeners();  // Re-attach event listeners for new checkboxes
    })
    .catch(error => console.error('Error fetching subcategories:', error));
}

// Function to re-attach event listeners after loading new subcategories
function attachCheckboxEventListeners() {
    document.querySelectorAll('.category-checkbox').forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            const categoryId = this.dataset.id;
            const subcategoriesList = this.parentNode.querySelector('.subcategories');

            if (this.checked) {
                if (subcategoriesList.children.length === 0) {
                    fetchSubcategories(categoryId, subcategoriesList);
                }
                subcategoriesList.classList.add('open');
            } else {
                subcategoriesList.classList.remove('open');
            }
        });
    });
}
