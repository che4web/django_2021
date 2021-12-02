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
search();
async function searchFood(){
    let response = await fetch('http://127.0.0.1:8000/dish/food/json/')
    let data  = await response.json()

    let  ar = document.getElementById('food_aread')
    ar.innerHTML=''

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
searchFood()

function borsch(){
    let  inp = document.getElementById('searchInput')
    inp.value="Борсч"
    search()
    
}

inp = document.getElementById('borsch')
inp.onclick= borsch

