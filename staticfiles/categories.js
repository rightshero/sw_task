        document.addEventListener('DOMContentLoaded', function() {
            let checkedCategories = new Set();
    
            function loadSubcategories(parentId, targetElement) {
                fetch(`/myapp/get_subcategories/?parent_id=${parentId}`)
                    .then(response => response.json())
                    .then(data => {
                        targetElement.innerHTML = '';
                        data.forEach(subcategory => {
                            let checkbox = document.createElement('input');
                            checkbox.type = 'checkbox';
                            checkbox.id = `sub_${subcategory.id}`;
                            checkbox.name = 'subcategories';
                            checkbox.value = subcategory.id;
                            checkbox.dataset.parentId = parentId;
    
                            let label = document.createElement('label');
                            label.htmlFor = checkbox.id;
                            label.textContent = subcategory.name;
    
                            let subSubcategoriesContainer = document.createElement('div');
                            subSubcategoriesContainer.className = 'subcategories-container';
    
                            targetElement.appendChild(checkbox);
                            targetElement.appendChild(label);
                            targetElement.appendChild(subSubcategoriesContainer);
                            targetElement.appendChild(document.createElement('br'));
    
                            checkbox.addEventListener('change', function() {
                                if (this.checked) {
                                    loadSubcategories(this.value, subSubcategoriesContainer);
                                    checkedCategories.add(this.value);
                                } else {
                                    fetch(`/myapp/remove_subcategories/?parent_id=${this.value}`)
                                        .then(() => {
                                            subSubcategoriesContainer.innerHTML = '';
                                            checkedCategories.delete(this.value);
                                        })
                                        .catch(error => console.error('Error:', error));
                                }
                            });
                        });
                    })
                    .catch(error => console.error('Error:', error));
            }
    
            function updateSiblingCheckboxes(currentCheckbox) {
                let allCategoryCheckboxes = document.querySelectorAll('input[name="category"]');
                allCategoryCheckboxes.forEach(checkbox => {
                    checkbox.disabled = false; // Re-enable all checkboxes initially
                });
    
                if (currentCheckbox) {
                    allCategoryCheckboxes.forEach(checkbox => {
                        if (checkbox !== currentCheckbox) {
                            checkbox.disabled = currentCheckbox.checked;
                        }
                    });
                }
            }
    
            function renderSubcategories(categoryElement, subcategories) {
                let subcategoriesContainer = categoryElement.querySelector('.subcategories-container');
                if (!subcategoriesContainer) {
                    subcategoriesContainer = document.createElement('div');
                    subcategoriesContainer.className = 'subcategories-container';
                    categoryElement.appendChild(subcategoriesContainer);
                }
    
                subcategories.forEach(subcategory => {
                    let checkbox = document.createElement('input');
                    checkbox.type = 'checkbox';
                    checkbox.id = `sub_${subcategory.id}`;
                    checkbox.name = 'subcategories';
                    checkbox.value = subcategory.id;
                    checkbox.dataset.parentId = categoryElement.id;
    
                    let label = document.createElement('label');
                    label.htmlFor = checkbox.id;
                    label.textContent = subcategory.name;
    
                    let subSubcategoriesContainer = document.createElement('div');
                    subSubcategoriesContainer.className = 'subcategories-container';
    
                    subcategoriesContainer.appendChild(checkbox);
                    subcategoriesContainer.appendChild(label);
                    subcategoriesContainer.appendChild(subSubcategoriesContainer);
                    subcategoriesContainer.appendChild(document.createElement('br'));
    
                    checkbox.addEventListener('change', function() {
                        if (this.checked) {
                            fetch(`/myapp/get_subcategories/?parent_id=${this.value}`)
                                .then(response => response.json())
                                .then(data => renderSubcategories(this.parentElement, data))
                                .catch(error => console.error('Error:', error));
                        } else {
                            fetch(`/myapp/remove_subcategories/?parent_id=${this.value}`)
                                .then(() => {
                                    let subSubcategoriesContainer = this.parentElement.querySelector('.subcategories-container');
                                    if (subSubcategoriesContainer) {
                                        subSubcategoriesContainer.innerHTML = '';
                                    }
                                })
                                .catch(error => console.error('Error:', error));
                        }
                    });
                });
            }
    
            document.querySelectorAll('input[name="category"]').forEach(function(categoryCheckbox) {
                categoryCheckbox.addEventListener('change', function() {
                    let parentId = this.value;
                    let parentElement = this.parentElement;
                    let subcategoriesContainer = parentElement.querySelector('.subcategories-container');
    
                    if (this.checked) {
                        if (!subcategoriesContainer) {
                            subcategoriesContainer = document.createElement('div');
                            subcategoriesContainer.className = 'subcategories-container';
                            parentElement.appendChild(subcategoriesContainer);
                        }
                        loadSubcategories(parentId, subcategoriesContainer);
                        updateSiblingCheckboxes(this);
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
    
            document.querySelectorAll('input[name="subcategories"]').forEach(function(subcategoryCheckbox) {
                subcategoryCheckbox.addEventListener('change', function() {
                    let parentId = this.dataset.parentId;
    
                    if (this.checked) {
                        fetch(`/myapp/get_subcategories/?parent_id=${this.value}`)
                            .then(response => response.json())
                            .then(data => renderSubcategories(this.parentElement, data))
                            .catch(error => console.error('Error:', error));
                    } else {
                        fetch(`/myapp/remove_subcategories/?parent_id=${this.value}`)
                            .then(() => {
                                let subSubcategoriesContainer = this.parentElement.querySelector('.subcategories-container');
                                if (subSubcategoriesContainer) {
                                    subSubcategoriesContainer.innerHTML = '';
                                }
                            })
                            .catch(error => console.error('Error:', error));
                    }
                });
            });
        });
