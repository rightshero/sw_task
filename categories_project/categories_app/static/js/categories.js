$(document).ready(function () {
  function createSubcategory(parentId, name) {
    return $.ajax({
      url: "/category/",
      method: "POST",
      data: {
        parent_id: parentId,
        name: name,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      dataType: "json",
    });
  }

  function createTwoSubcategories(parentId, parentName) {
    $.when(
      createSubcategory(parentId, `SUB ${parentName}1`),
      createSubcategory(parentId, `SUB ${parentName}2`)
    ).then(function (response1, response2) {
      var container = $(`#subcategories-${parentId}`);
      [response1[0], response2[0]].forEach(function (data) {
        var newCategoryHtml = `
                      <div class="category">
                          <input type="checkbox" id="category-${data.id}" data-id="${data.id}">
                          <label for="category-${data.id}">${data.name}</label>
                          <div class="subcategories" id="subcategories-${data.id}"></div>
                      </div>
                  `;
        container.append(newCategoryHtml);
      });
    });
  }

  $(document).on("change", 'input[type="checkbox"]', function () {
    var categoryId = $(this).data("id");
    var categoryName = $(`label[for="category-${categoryId}"]`).text();
    var subcategoriesContainer = $(`#subcategories-${categoryId}`);

    if ($(this).is(":checked")) {
      createTwoSubcategories(categoryId, categoryName);
    } else {
      subcategoriesContainer.empty();
    }
  });
});
