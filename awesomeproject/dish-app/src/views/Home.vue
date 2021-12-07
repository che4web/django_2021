<template>
  <div class="home">
      <div class="container">
    <dish-list />
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import DishList from '@/components/DishList.vue'

export default {
  name: 'Home',
  components: {
    DishList
  }
}
</script>
