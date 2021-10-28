<template>
    <div class="registroProductos">
        <div class="containerRegistroProductos">
            <p>Con esta plataforma usted podra ingresar su producto</p>
            <form v-on:submit.prevent= "processRegistroProductos">
                <input type="text" placeholder="Producto" v-model="registroProductos.nombreProducto">
                <br/>
                <input type="text" placeholder="caracteristicas" v-model="registroProductos.caracteristica">
                <br/>
                <input type="number" placeholder="0" v-model="registroProductos.cantidad">
                <br/>
                 <select id="tipo_producto" name="tipo_producto" v-model="registroProductos.tipo_producto">
                 <option value="1">Tejido</option>
                 <option value="2">Ceramica</option>
                 <option value="3">Joyeria</option>
                 <option value="4">Orfebreria</option>
                 <option value="5">Tallado</option>
                </select>
                <br/>
                <button type="submit">guarda tu Producto!!</button>
            </form>
        </div>
         <div class="imagen">
             <img src="https://media.istockphoto.com/photos/wayuu-backpack-picture-id534624660?k=20&m=534624660&s=612x612&w=0&h=y9rBq69JuKcbYFwECxoQkKxMSP1UTax9-JknjqudKto=" >
        </div>
    </div>    
</template>

<script>
    import axios from 'axios';

    export default{
        name: 'formularioProductos',

        data: function(){
            return{
                registroProductos :{
                    nombreProducto : "",
                    caracteristica: "",
                    cantidad : 0,
                    tipo_producto  : [
                        {code : 1, name: "tejido"},
                        {code : 2, name: "ceramica"},
                        {code : 3, name: "joyeria"},
                        {code : 4, name: "Orfebreria"},
                        {code : 5, name: "tallado"}
                    ]

                }
            }
        },

        methods:{
            processRegistroProductos: function(){
                axios.post(
                   'http://localhost:8000/productGet/',
                   this.registroProductos, 
                   {headers:{ 'Content-Type': 'application/json'}}
                    
               )
                .then((result) => {
                    console.log("funciono")
                    alert("producto creado!");
                   /* let dataComunidades ={
                        registroComunidades: this.comunidades.registroComunidades
                    }   
                    
                    this.$emit('completedIngresoFormularioComunidades', dataComunidades)*/
                })
                .catch((error) => {
                   console.log(error); 
                   alert("Error. fallo el registro");
                });
            }   
        }
    }

</script>

<style >
 .registroProductos{
        margin  : 40px 120px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        /*espaciado*/
        gap:5px;
    }

    .registroProductos .imagen{
         height: 110%;
    }

    .registroProductos .containerRegistroProductos{
        border: 3px solid #0F362D;
        border-radius: 10px;
        width: 90%;
        height: 60%;
        padding: 5%;
        margin: 15px;
    }
    .registroProductos .containerRegistroProductos p{
       color:#0F362D;
       display: flex;
       text-align: center;
       font-size: 17px;
       padding: 5px;
       margin: 0px;
       
    }
   
    .registroProductos .containerRegistroProductos form{
        width: 90%;
        padding: 10px;
        display: flex;
        flex-direction: column;
    }
    .registroProductos .containerRegistroProductos option{
        font-size: 12px;
        font-family: 'Verdana', sans-serif;
        color: #444;
        
       
    }
    .registroProductos .containerRegistroProductos input{
        height: 25px;
        width: 100%;
        box-sizing: border-box;
        padding: 5px 10px;
        margin: 5px 0;
        border: 1px solid #0F362D;
    }
    .registroProductos .containerRegistroProductos button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #0F362D;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        margin: 10px 0 20px 0;
    }
    .registroProductos .containerRegistroProductos button:hover{
        color: #000;
        background: #FF9F1C;
        border: 1px solid #0F362D;
    }
</style>
