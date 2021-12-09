<template >
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card   dish_photo">
                    <img :src="object.photo" class="card-img" alt="...">
                    <div class="card-img-overlay">
                        <h5 class="card-title">{{object.name}}</h5>
                        <p class="card-text"></p>
                        <p class="card-text"></p>
                    </div>
                </div>
            </div>
        </div>



        <div class="ingredient-row">
            <div class="row">
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title"> Ингрединеты</h5>
                            <ol>
                                <li v-for="item in ingredient_set" :key="item.id">{{item.food_name}} -- 
                                    <input v-model="item.quantity" @input="saveIngredietn(item)"> {{item.get_unit_display}} | {{item.energy }}</li> 
                            </ol>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title"> БЖУ</h5>
                            <ol>
                                <li> Белки-- {{object.pfc.protein}} </li> 
                                <li> Жиры- {{object.pfc.fat}}</li> 
                                <li> Углеводы-- {{object.pfc.carbohydrate}} </li> 
                                <li> Калории--  {{object.pfc.energy}}</li> 
                            </ol>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-md-12">
                <h2>Рецепт</h2>
                <div>{{object.recipe}}</div>
            </div>
        </div>
    </div>

</template>
<script>
import {Dish,Ingredient} from "@/api"

export default {
    name:'dish-dish',
    data(){
        return {
            dishList:[],
            message:'',
            object:{},
            ingredient_set:[],
            pfc:{},
            pfc_aggr:{},
        }
    },
    components: {
    },
    methods:{
        async saveIngredietn(item){
            await Ingredient.save(item)
        },
        async  getDish(){
            this.object  = await  Dish.get(this.$route.params.id)
            this.ingredient_set= await Ingredient.filter( {dish:this.$route.params.id})
        }
    },
    mounted(){
        this.getDish()
    }
}
</script>
