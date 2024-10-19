<template>
  <div>
    <CategoryTree :categories="categories" v-model:selectedCategories="selectedCategories" />
  </div>
</template>

<script>
import axios from 'axios';
import CategoryTree from './CategoryTree.vue'; // Import the CategoryTree component

export default {
  name: 'CategoryList',
  components: {
    CategoryTree, // Register the CategoryTree component
  },
  data() {
    return {
      categories: [],
      selectedCategories: [], // Array to hold selected category IDs
    };
  },
  created() {
    this.fetchCategories(); // Fetch categories when the component is created
  },
  methods: {
    fetchCategories() {
      axios.get('http://localhost:8000/api/categories/all_categories/')
        .then(response => {
          this.categories = response.data.response;
        })
        .catch(error => {
          console.error('Error fetching categories:', error);
        });
    },
  },
};
</script>

<style scoped>
h1 {
  margin-bottom: 20px;
}
</style>
