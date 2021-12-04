<template lang="pug">
    .col
        .class.card.h-100 
                img(class="card-img-top" :src="dish.photo")
                span фото нет
                .card-body
                    h5(class="card-title") {{dish.name}}
                    p тип {{dish.get_typ_display}} 
                    p  время {{dish.cooking_time}}
                    p {{dish.recipe}}
                    a  изменить
                    a(onclick ="return false" :href=" dish.get_absolute_url " class="btn btn-primary") подробнее
                    button(class="btn like-button" :class="dish.is_like? 'btn-secondary':'btn-success'" v-on:click="like") lke
</template>
<script>
export default {
    name:'dish-card',
    props: ['dish'],
    methods:{
       async  like(){
       let  response =  await  fetch('http://127.0.0.1:8000/dish/like/', {
                                        method: 'POST',
                                        headers: {
                                            'X-CSRFToken': "{{ csrf_token }}",
                                            'Content-Type': 'application/json;charset=utf-8'
                                        },
                                            body: JSON.stringify({"pk":this.dish.id})
                                        });

        let status   = await response.json()
           if (status.status=='OK'){
                this.dish.is_like=true
           }
 

        }
    },
}
</script>
