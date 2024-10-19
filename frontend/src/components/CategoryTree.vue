
<template>
    <div>
      <div v-for="category in localCategories" :key="category.id" class="category-item">
        <label :for="'category-' + category.id">
          <input
            type="checkbox"
            :value="category.id"
            :id="'category-' + category.id"
            v-model="selectedCategories"
            @change="toggleInput(category.id)"
          />
          {{ category.name }}
        </label>
  
        <!-- Text box and submit button for creating child category -->
        <div v-if="showInput[category.id]">
          <input
            type="text"
            v-model="newChildName[category.id]"
            placeholder="New child category name"
          />
          <button @click="createChildCategory(category)">Submit</button>
        </div>
  
        <div v-if="category.children && category.children.length > 0" class="children">
          <CategoryTree :categories="category.children" v-model:selectedCategories="selectedCategories" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'CategoryTree',
    props: {
      categories: {
        type: Array,
        required: true,
      },
      modelValue: {
        type: Array,
        required: true,
      },
    },
    data() {
      return {
        newChildName: {}, // Store new child names by parent ID
        showInput: {}, // Track which category inputs should be shown
      };
    },
    computed: {
      selectedCategories: {
        get() {
          return this.modelValue;
        },
        set(value) {
          this.$emit('update:modelValue', value);
        },
      },
      localCategories() {
        return this.categories; // Return the categories prop for rendering
      },
    },
    methods: {
      toggleInput(categoryId) {
        // Toggle the visibility of the input field for the selected category
        this.showInput[categoryId] = !this.showInput[categoryId];
      },
      createChildCategory(category) {
        const name = this.newChildName[category.id];
        if (name) {
          const newChild = { name, parent: category.id };
          console.log(newChild);
          axios.post('http://localhost:8000/api/categories/', newChild)
            .then((response) => {
              const newCategory = response.data.response; 
              this.addChildCategory(category.id, newCategory); // Update local categories with the new child
              this.newChildName[category.id] = ''; // Clear input
              this.showInput[category.id] = false; // Hide input after submission
            })
            .catch(error => {
              console.error('Error creating category:', error);
            });
        }
      },
      addChildCategory(parentId, childCategory) {
         // Find the parent category and add the new child category
        const parentCategory = this.findCategoryById(parentId, this.localCategories);
        
        if (parentCategory) {
        // Make sure the new category object has the correct structure
        const formattedChild = {
            id: childCategory.id, // Ensure we're using the correct ID
            name: childCategory.name, // Ensure we're using the correct name
            children: childCategory.children || [] // Initialize children as an empty array if not present
        };
        
        // Add new child to parent's children array
        parentCategory.children = parentCategory.children || [];
        parentCategory.children.push(formattedChild);
        }
      },
      findCategoryById(id, categories) {
        // Recursive function to find a category by ID
        for (const category of categories) {
          if (category.id === id) {
            return category;
          }
          if (category.children) {
            const found = this.findCategoryById(id, category.children);
            if (found) {
              return found;
            }
          }
        }
        return null; // Return null if not found
      },
    },
  };
  </script>
  
<style scoped>
  .category-item {
    margin-left: 20px; /* Indentation for nested categories */
  }
  
  .children {
    margin-left: 20px; /* Additional indentation for children */
  }


.category-item label {
  margin-right: 10px; /* Space between checkbox and text */
}

input[type="checkbox"] {
  width: 20px; /* Custom width for checkboxes */
  height: 20px; /* Custom height for checkboxes */
  margin-right: 10px; /* Space between checkbox and label text */
}

input[type="text"] {
  margin-top: 10px; /* Space above the input box */
  padding: 5px; /* Padding for input box */
  border: 1px solid #ccc; /* Border for input box */
  border-radius: 4px; /* Rounded corners for input box */
  width: 200px; /* Width for input box */
}

button {
  margin-left: 10px; /* Space between input box and button */
  padding: 5px 10px; /* Padding for button */
  border: none; /* Remove default border */
  border-radius: 4px; /* Rounded corners for button */
  background-color: #28a745; /* Green background color */
  color: white; /* White text color */
  cursor: pointer; /* Pointer cursor on hover */
  transition: background-color 0.3s; /* Smooth background color transition */
}

button:hover {
  background-color: #218838; /* Darker green on hover */
}


</style>

  