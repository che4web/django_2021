<template >

<div class="row row-cols-1  row-cols-sm-2 row-cols-md-3 g-4" id="cardArea">

    <input v-model="message" @input="getDish">
    <dish-card v-for="dish in dishList" :dish="dish" :key="dish.id">
    </dish-card>
    </div>
</template>
<script>

import DishCard from './DishCard.vue'
export default {
    name:'dish-list',
    data(){
        return {
            dishList:[],
            message:''
        }
    },
  components: {
    DishCard,
  },
    methods:{
        async  getDish(){

            let params = new URLSearchParams({
                name: this.message
            })
            let response = await fetch('/api/dish/?'+ params)
            this.dishList  = await response.json()
        }
    }
}
</script>
