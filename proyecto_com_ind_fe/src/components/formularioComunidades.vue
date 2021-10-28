<template>
    <div class="registroComunidades">
        <div class="imagen">
             <img src="https://valleyadventours.com/wp-content/uploads/2017/10/tour-compras-cali.jpg" >
        </div>
        <div class="containerRegistroComunidades">
            <p>Con esta plataforma usted podra ingresar su comunidad</p>
            
            <form v-on:submit.prevent= "processRegistroComunidades">
                <select id="region" name="region" v-model="registroComunidades.region">  
                 <option value= "1">Caribe</option>
                 <option value="2">Andina</option>
                 <option value="3">Pacifico</option>
                 <option value="4">Orinoquia</option>
                 <option value="5">Amazonia</option>
                 <option value="6">Insular</option>
                </select>
                <br/>
                <input type="text" placeholder="Comunidad" v-model="registroComunidades.nombreComunidad">
                <br/>
                <button type="submit">guarda tu Comunidad!!</button>
            </form>
        </div>
    </div>    
</template>

<script>
    import axios from 'axios';

    export default{
        name: 'formularioComunidades',

        data: function(){
            return{
                registroComunidades :{
                    nombreComunidad : "",
                    region  : [
                        {code : 1, name: "caribe"},
                        {code : 2, name: "Andina"},
                        {code : 3, name: "Pacifico"},
                        {code : 4, name: "Orinoquia"},
                        {code : 5, name: "Amazonia"},
                        {code : 6, name: "Insular"}
                    ]
                }
            }
        },

        methods:{
            processRegistroComunidades: function(){
                axios.post(
                   'http://localhost:8000/comunidades/',
                   this.registroComunidades, 
                   {headers:{ 'Content-Type': 'application/json'}}
                )
                .then((result) => {
                    console.log("funciono")
                    alert("comunidad creada!");
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
 .registroComunidades{
        margin  : 90px 10px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        /*espaciado*/

 }
    .registroComunidades .imagen{
         height: 90%;
    }
    .registroComunidades .containerRegistroComunidades {
        border: 3px solid #0F362D;
        border-radius: 10px;
        width: 70%;
        height: 45%;
        padding: 5%;
        margin: 15px;
    }
    .registroComunidades .containerRegistroComunidades p{
       color:#0F362D;
       display: flex;
       text-align: center;
       font-size: 17px;
       padding: 5px;    
       margin: 0px;
    }
    .registroComunidades .containerRegistroComunidades form{
        width: 80%;
        padding: 25px;
        display: flex;
        flex-direction: column; 
    }

    .registroComunidades .containerRegistroComunidades option{
        font-size: 12px;
        font-family: 'Verdana', sans-serif;
        color: #444;
       
    }

    .registroComunidades .containerRegistroComunidades input{
        height: 25px;
        width: 90%;
        box-sizing: border-box;
        padding: 5px 10px;
        margin: 5px;
        border: 1px solid #0F362D;
    }
    .registroComunidades .containerRegistroComunidades button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #0F362D;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        margin: 10px 0 20px 0;
    }
    .registroComunidades .containerRegistroComunidades button:hover{
        color: #000;
        background: #FF9F1C;
        border: 1px solid #0F362D;
    }
</style>
