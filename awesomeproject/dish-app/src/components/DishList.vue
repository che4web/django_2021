<template >
<div>

    <input v-model="message" @input="getDish">
<div class="row row-cols-1  row-cols-sm-2 row-cols-md-3 g-4" id="cardArea">

    <dish-card v-for="dish in dishList" :dish="dish" :key="dish.id" >
    </dish-card>
    </div>
    </div>
</template>
<script>

import DishCard from './DishCard.vue'
import {Dish} from '@/api'
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

            let params = {
                name: this.message
            }
            this.dishList  = await Dish.filter(params)
        }
    
    },
    mounted(){
        this.getDish()
        }
}
</script>
