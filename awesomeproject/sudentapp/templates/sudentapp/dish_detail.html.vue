{% extends "base.html"%}

{%block some_name%}
<div class="row">
    <div class="col-md-12">
    <div class="card   dish_photo">
        <img src="{{object.get_photo_url}}" class="card-img" alt="...">
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
                    {%for item in ingredients%}
                    <li>{{item.food.name}} -- {{item.quantity}} {{item.get_unit_display}} | {{item.energy }}</li> 
                    {%endfor%}
                </ol>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title"> БЖУ</h5>
                <ol>
                    <li> Белки-- {{pfc.protein}} </li> 
                    <li> Жиры- {{pfc.fat}}</li> 
                    <li> Углеводы-- {{pfc.carbohydrate}} </li> 
                    <li> Калории--  {{pfc.energy}}</li> 
                </ol>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title"> БЖУ aggr</h5>
                <ol>

                    <li> Белки-- {{pfc_aggr.p}} </li> 
                    <li> Жиры- {{pfc_aggr.f}}</li> 
                    <li> Углеводы-- {{pfc_aggr.c}} </li> 
                    <li> Калории--  {{pfc_aggr.e}}</li> 
                </ol>
            </div>
        </div>
    </div>
</div>
</div>

<div class="row">
    <div class="col-md-12">
        <h2>Рецепт</h2>
<div>{{object.recipe|linebreaks}}</div>
</div>
</div>
{%endblock%}
