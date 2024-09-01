document.addEventListener('DOMContentLoaded', () => {
    const checkedCategories = new Set();

    // Fetch and display subcategories for a given parent category
    function loadSubcategories(parentId, targetElement) {
        fetch(`/myapp/get_subcategories/?parent_id=${parentId}`)
            .then(response => response.json())
            .then(data => {
                targetElement.innerHTML = ''; // Clear existing subcategories

                data.forEach(subcategory => {
                    const checkbox = createCheckbox(subcategory, parentId, targetElement);
                    targetElement.appendChild(checkbox);
                    targetElement.appendChild(document.createElement('br'));
                });
            })
            .catch(error => console.error('Error:', error));
    }

    // Create a checkbox element for a subcategory
    function createCheckbox(subcategory, parentId, targetElement) {
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = `sub_${subcategory.id}`;
        checkbox.name = 'subcategories';
        checkbox.value = subcategory.id;
        checkbox.dataset.parentId = parentId;

        const label = document.createElement('label');
        label.htmlFor = checkbox.id;
        label.textContent = subcategory.name;

        const subSubcategoriesContainer = document.createElement('div');
        subSubcategoriesContainer.className = 'subcategories-container';

        checkbox.addEventListener('change', () => {
            if (checkbox.checked) {
                loadSubcategories(checkbox.value, subSubcategoriesContainer);
                checkedCategories.add(checkbox.value);
            } else {
                fetch(`/myapp/remove_subcategories/?parent_id=${checkbox.value}`)
                    .then(() => {
                        subSubcategoriesContainer.innerHTML = '';
                        checkedCategories.delete(checkbox.value);
                    })
                    .catch(error => console.error('Error:', error));
            }
        });

        const container = document.createElement('div');
        container.appendChild(checkbox);
        container.appendChild(label);
        container.appendChild(subSubcategoriesContainer);

        return container;
    }

    // Update the state of sibling category checkboxes
    function updateSiblingCheckboxes(currentCheckbox) {
        document.querySelectorAll('input[name="category"]').forEach(checkbox => {
            checkbox.disabled = currentCheckbox ? checkbox !== currentCheckbox && currentCheckbox.checked : false;
        });
    }

    // Initialize category and subcategory checkboxes
    function initializeCheckboxes() {
        document.querySelectorAll('input[name="category"]').forEach(categoryCheckbox => {
            categoryCheckbox.addEventListener('change', () => {
                const parentId = categoryCheckbox.value;
                const parentElement = categoryCheckbox.parentElement;
                let subcategoriesContainer = parentElement.querySelector('.subcategories-container');

                if (categoryCheckbox.checked) {
                    if (!subcategoriesContainer) {
                        subcategoriesContainer = document.createElement('div');
                        subcategoriesContainer.className = 'subcategories-container';
                        parentElement.appendChild(subcategoriesContainer);
                    }
                    loadSubcategories(parentId, subcategoriesContainer);
                    updateSiblingCheckboxes(categoryCheckbox);
                } else {
                    if (subcategoriesContainer) {
                        subcategoriesContainer.innerHTML = '';
                    }
                    fetch(`/myapp/remove_subcategories/?parent_id=${parentId}`)
                        .catch(error => console.error('Error:', error));
                    updateSiblingCheckboxes(null);
                }
            });
        });

        document.querySelectorAll('input[name="subcategories"]').forEach(subcategoryCheckbox => {
            subcategoryCheckbox.addEventListener('change', () => {
                const parentId = subcategoryCheckbox.dataset.parentId;

                if (subcategoryCheckbox.checked) {
                    fetch(`/myapp/get_subcategories/?parent_id=${subcategoryCheckbox.value}`)
                        .then(response => response.json())
                        .then(data => {
                            renderSubcategories(subcategoryCheckbox.parentElement, data);
                        })
                        .catch(error => console.error('Error:', error));
                } else {
                    fetch(`/myapp/remove_subcategories/?parent_id=${subcategoryCheckbox.value}`)
                        .then(() => {
                            const subSubcategoriesContainer = subcategoryCheckbox.parentElement.querySelector('.subcategories-container');
                            if (subSubcategoriesContainer) {
                                subSubcategoriesContainer.innerHTML = '';
                            }
                        })
                        .catch(error => console.error('Error:', error));
                }
            });
        });
    }

    initializeCheckboxes();
});
