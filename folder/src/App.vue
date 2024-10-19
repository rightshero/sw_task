<template>
  <div id="app">
    <CategoryList />
  </div>
</template>

<script>
import CategoryList from './components/CategoryList.vue'; // Import your CategoryList component

export default {
  name: 'App',
  components: {
    CategoryList, // Register the CategoryList component
  },
};
</script>

<style>
/* Global styles can be added here */
body {
  font-family: Arial, sans-serif; /* Basic font styling */
  margin: 0;
  padding: 0;
}

#app {
  max-width: 800px; /* Set a max width for the app */
  margin: 0 auto; /* Center the app horizontally */
  padding: 20px; /* Add padding around the app */
}

h1 {
  text-align: center; /* Center the heading */
}
</style>
