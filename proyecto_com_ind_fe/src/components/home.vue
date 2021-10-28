<template>
    <div class="home">
        
         <div class="contenido">
         <h1>Bienvenidas comunidades!! </h1>
         <h2>su registro le premitira dar a conocer los diferentes productos de su comunidad, así como conocer los productos fabricados por otras comunidades del pais</h2>
         <h2> para registrar sus productos debera seguir estos pasos: </h2>
        
         <ol>
            <li>
                ingrese a la pestaña de formulario de comunidad y diligencie sus datos
            </li>
            <li>
                ingrese a la pestaña de formulario de producto y diligencie sus datos
            </li>
            <li>
                ingrese a la pestaña de formulario de producto por comunidad y diligencie donde asociara su producto a su comunidad
            </li>
            <li>
                en la pestaña final podra visualizar los productos ingresados por comunidad
            </li>
         </ol> 
         </div>  
         <div class="imagen">
             <img src="https://i.pinimg.com/736x/0c/95/1d/0c951db207fc0a57a9f90a0f270ca65b--http-header-chihuahua.jpg" >
         </div>
    </div>
</template>


<script>
    
</script>


<style>

    .home {
        margin         : 5%;
        padding        : 2%;
        height         : 10px;
        width          : 100%;
        /*justify-content: center;
        align-items    : center;*/
        display: grid;
        grid-template-columns: 1fr 1fr;
        /*espaciado*/
        gap:35px;
        margin:auto;
      
    }
    .home .contenido {
        /*margin : 50px;
        height : 30%;
        color    : #283747; */
        border: 3px solid #0F362D;
        border-radius: 10px;
        width: 90%;
        height: 70%;
        padding: 5%;
        margin: 15px;
        background-color:#0F362D;
    }

    .home .contenido h1{
        margin : 20px;
        font-size: 30px;
        color    : #fff; 
        display: flex;
        align-items    : center;
        justify-content: center;
        line-height: 1;
        font-family: sans-serif;
    }
    .home .contenido h2{
        margin : 20px;
        font-size: 15px;
        color    : #fff; 
        display: flex;
        align-items    : center;
        justify-content: center;
        font-family: sans-serif;
        line-height: 1.5;
    }
    .home .contenido ol{
        margin : 20px;
        font-size: 13px;
        color    : #fff; 
        text-align: left;
        font-family: sans-serif;
        line-height: 1.5;
        font-weight: lighter;
    
    }

    .imagen img{
        height: 70%;
    
        
    }

    /*.home h2 {
        font-size: 20px;
        color    : #000000;
        justify-content: center;
        align-items: center;
    }

    .home .imagen{
        
    }*/


</style>