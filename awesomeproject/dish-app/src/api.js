export const dishUrl = "/api/dish/"
export const ingredientUrl = "/api/ingredient/"
import axios from 'axios'

export async function _getList(url,filter){
    console.log(filter)
    return (await axios.get(url,{params:filter})).data

}

export async function _get(url,id){
    return (await axios.get(url+id+'/')).data
}
export async function _save(url,obj){
    if (obj.id){
    return (await axios.patch(url+obj.id+'/',obj)).data
        
    }else{
        return (await axios.post(url,obj)).data
    }
}
function apiConstructor(apiUrl){
    return {
        async save(obj){
            return _save(apiUrl,obj)
        },
        async get(id){
            return _get(apiUrl,id)
        },
        async filter(filter){
            return _getList(apiUrl,filter)
        },
    }
}
export let Ingredient = apiConstructor(ingredientUrl)
export let Dish = apiConstructor(dishUrl)


