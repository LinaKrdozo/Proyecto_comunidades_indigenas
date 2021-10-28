<template>
    <div class="obtenerComProd">
        <div class="imagen">
             <img src="https://artesaniasdecolombia.com.co/Documentos/Catalogo/3708_werregue-mediano-g.png" >
        </div>
        <div class="containerObtenerComProd">
            <p>Con esta plataforma usted podra asociar su comunidad a su producto</p>
            <form v-on:submit.prevent= "processObtenerComProd">
                <select name = "" id= "" class="form-control" v-model="registroComProd.comunidad">
                    <option v-for= "comunidad in comunidades "  :value="comunidad.id" v-bind:key="comunidad">
                        {{comunidad.nombreComunidad}}
                    </option>
                </select>
                <br/>
                <select name = "" id= "" class="form-control" v-model="registroComProd.producto">
                    <option  v-for= "producto in productos "  :value="producto.id" v-bind:key="producto">
                        {{producto.nombreProducto}}
                    </option>
                </select>
                <button type="submit">asociar!!</button>
            </form>
        </div>
    </div>    
</template>

<script>
    import axios from 'axios';

    export default{
        name: 'formularioComProd',

        data: function(){
            return {
                comunidades: {},
                productos: {},
                registroComProd :{
                    comunidad : this.comunidades,
                    producto  : this.productos 
                }

            }
        },

        mounted(){
            this.getComunidades(),
            this.getProductos()
        },


        methods:{
            getComunidades(){
                const comunidades = localStorage.getItem("comunidades")
                console.log("comunidades: ",comunidades)
                
                axios.get(
                   'http://127.0.0.1:8000/comunidadesList/'
                )
                .then(response => {
                    this.comunidades = response.data;
                    localStorage.setItem('comunidades', JSON.stringify(response.data));
                    console.log(response);
                });
                
            },  
            
            getProductos(){
                const productos = localStorage.getItem("productos")
                console.log("productos: ",productos)
                
                
                axios.get(
                   'http://127.0.0.1:8000/productList/'
                )
                .then(response => {
                    this.productos = response.data;
                    localStorage.setItem('productos', JSON.stringify(response.data));
                    console.log(response);
                });
                
            },

             processObtenerComProd: function(){
                console.log("registroComProd: ", JSON.stringify(this.registroComProd) )
                
                axios.post(
                   'http://127.0.0.1:8000/comunidadesYproductos/',
                   this.registroComProd 
                )
                .then((result) => {
                    console.log("funciono")
                    alert("comunidad y producto asociados!")
                   
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
 .obtenerComProd {
        margin  : 50px 100px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        /*espaciado*/
    }
    .obtenerComProd .imagen{
         height: 100%;
    }
    .obtenerComProd .containerObtenerComProd{
        border: 3px solid #0F362D;
        border-radius: 10px;
        width: 70%;
        height: 25%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 5%;
    }
    .obtenerComProd .containerObtenerComProd p{
       color:#0F362D;
       text-align: center;
       font-size: 17px;
    }
    .obtenerComProd .containerObtenerComProd form{
        width: 70%;
        padding: 5px;
        display: flex;
        flex-direction: column;
    }

    .obtenerComProd .containerObtenerComProd option{
        font-size: 12px;
        font-family: 'Verdana', sans-serif;
        color: #444;
       
    }

    .obtenerComProd .containerObtenerComProd input{
        height: 25px;
        width: 90%;
        box-sizing: border-box;
        padding: 5px 10px;
        margin: 5px;
        border: 1px solid #0F362D;
    }
    .obtenerComProd .containerObtenerComProd button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #0F362D;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        margin: 10px 0 20px 0;
    }
    .obtenerComProd .containerObtenerComProd button:hover{
        color: #000;
        background: #FF9F1C;
        border: 1px solid #0F362D;
    }
</style>
