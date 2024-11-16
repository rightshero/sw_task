$(document).ready(function() {
    // Load saved state from localStorage
    function loadState() {
        const savedState = localStorage.getItem('categoryState');
        if (savedState) {
            const checkedBoxes = JSON.parse(savedState);
            checkedBoxes.forEach(id => {
                const checkbox = $(`#cat_${id}`);
                checkbox.prop('checked', true);
                const container = $(`#subcategories_${id}`);
                if (container.length) {
                    container.show();
                }
            });
        }
    }

    // Save current state to localStorage
    function saveState() {
        const checkedBoxes = $('.category-checkbox:checked').map(function() {
            return $(this).data('id');
        }).get();
        localStorage.setItem('categoryState', JSON.stringify(checkedBoxes));
    }

    function createSubcategories(categoryId) {
        $.ajax({
            url: createSubcategoriesUrl,
            data: { 'category_id': categoryId },
            dataType: 'json',
            success: function(data) {
                const container = $(`#subcategories_${categoryId}`);
                if (!container.children('.category-item').length) {
                    renderSubcategories(container, data.subcategories);
                }
                container.show();
                saveState();
            },
            error: function() {
                const container = $(`#subcategories_${categoryId}`);
                container.empty();
                container.append('<div class="error">Error creating subcategories</div>');
            },
        });
    }

    function renderSubcategories(container, subcategories) {
        subcategories.forEach(function(subcategory) {
            const subcategoryHtml = `
                <div class="category-item">
                    <input type="checkbox" 
                           id="cat_${subcategory.id}" 
                           class="category-checkbox" 
                           data-id="${subcategory.id}"
                           data-level="${subcategory.level}">
                    <label for="cat_${subcategory.id}">${subcategory.name}</label>
                    <div id="subcategories_${subcategory.id}" class="subcategories"></div>
                </div>
            `;
            container.append(subcategoryHtml);
        });
    }

    $(document).on('change', '.category-checkbox', function() {
        const categoryId = $(this).data('id');
        const container = $(`#subcategories_${categoryId}`);
        
        if (this.checked) {
            if (!container.children('.category-item').length) {
                createSubcategories(categoryId);
            } else {
                container.show();
                saveState();
            }
        } else {
            container.hide();
            saveState();
        }
    });

    // Load saved state on page load
    loadState();

    // Save state when leaving page
    $(window).on('beforeunload', function() {
        saveState();
    });
});