async function onLikePress(){
        let pk = this.attributes['dish-id'].value
        await fetch('http://127.0.0.1:8000/dish/like/', {
                                        method: 'POST',
                                        headers: {
                                            'X-CSRFToken': "{{ csrf_token }}",
                                            'Content-Type': 'application/json;charset=utf-8'
                                        },
                                            body: JSON.stringify({"pk":pk})
                                        });
        this.classList.remove("btn-success");
        this.classList.add("btn-secondary");
}
async function search(){
    let  inp = document.getElementById('searchInput')
    let params = new URLSearchParams({
                name: inp.value
            })
    let response = await fetch('http://127.0.0.1:8000/api/dish/?'+ params)
    let data  = await response.json()

    let  ar = document.getElementById('cardArea')
    ar.innerHTML=''

    for(let el of data){
        let newEl = document.createElement('div')
        newEl.innerHTML=`
            <div class="col">
                <div class="card h-100" name="dish_id_${el.id}" some_att="${el.id}"  > 
                    <img class="card-img-top" src="${el.photo}" >
                    фото нет
                    <div class="card-body">
                        <h5 class="card-title"> ${el.name} </h5>
                        <p> тип ${el.get_typ_display} </p>
                        <p>  время${el.cooking_time} </p>
                        <p>${el.recipe}</p>
                        <a href=""> изменить</a>
                        </td>
                        <a  onclick ="return false" href=" ${ el.get_absolute_url }" class="btn btn-primary">подробнее</a>
                        <button  class="btn ${el.is_like? 'btn-secondary':'btn-success'} like-button" dish-id="${el.id}">like</button>
                        
                    </div>
                </div>
            </div>
        `
        document.querySelectorAll('.like-button').forEach(el=>el.onclick=onLikePress)

            ar.appendChild(newEl)
    }

        
    return false
    }
let btn = document.getElementById('searchButton')
btn.onclick=search

let inp = document.getElementById('searchInput')
inp.oninput=search
async function searchFood(){
    let response = await fetch('http://127.0.0.1:8000/dish/food/json/')
    let data  = await response.json()


    for(let el of data){
        let newEl = document.createElement('div')
        newEl.innerHTML=`
            <div class="col">
                <div class="card h-100" name="dish_id_${el.id}" some_att="${el.id}"  >
                ${el.name}
                </div>
            </div>
        `
            ar.appendChild(newEl)
    }
        
    return false
    }

function borsch(){
    let  inp = document.getElementById('searchInput')
    inp.value="Борсч"
    search().then(

    )
    
}

inp = document.getElementById('borsch')
inp.onclick= borsch

Vue.component('dish-card', {
  // Компонент todo-item теперь принимает
  // "prop", то есть входной параметр.
  // Имя входного параметра todo.
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
  template: `
            <div class="col">
                <div class="card h-100" > 
                    <img class="card-img-top" :src="dish.photo" >
                    фото нет
                    <div class="card-body">
                        <h5 class="card-title"> {{dish.name}} </h5>
                        <p> тип {{dish.get_typ_display}} </p>
                        <p>  время {{dish.cooking_time}} </p>
                        <p>{{dish.recipe}}</p>
                        <a href=""> изменить</a>
                        </td>
                        <a  onclick ="return false" :href=" dish.get_absolute_url " class="btn btn-primary">подробнее</a>
                        <button  class="btn like-button" :class="dish.is_like? 'btn-secondary':'btn-success'" v-on:click="like"  >like</button>
                        
                    </div>
                </div>
            </div>
    `
})

var app = new Vue({
  el: '#app',
  data: {
    message: 'Привет, Vue!',
    dishList:[]
  },
    methods:{
        async  getDish(){

            let params = new URLSearchParams({
                name: this.message
            })
            let response = await fetch('http://127.0.0.1:8000/api/dish/?'+ params)
            this.dishList  = await response.json()
        }
    }
})



