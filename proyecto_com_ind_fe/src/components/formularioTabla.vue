<template>
    <div class="obtenerTablaComProd">
       
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>comunidad</th>
                    <th>Producto</th>
                    <th>Cantidad</th>
                    <th>Caracteristicas</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in listaG" :key="item">
                    <td>{{item.comunidad.nombreComunidad}}</td>
                    <td>{{item.producto.nombreProducto}}</td>
                    <td>{{item.producto.cantidad}}</td>
                    <td>{{item.producto.caracteristica}}</td>
                   
                </tr>
            </tbody>
        </table>
    </div>    
</template>

<script>
    import axios from 'axios';

    export default{
        name: 'formularioTabla',
        
        data: function(){
            const listaG = localStorage.getItem("listaG")  
            
            if(listaG){
                this.listaG = JSON.parse(listaG);
            }
            return{
                comunidadesYproductosList: []
            }
        },

        mounted(){
            this.fetch()
        },

        methods: {
           fetch(){
             

            axios.get("http://127.0.0.1:8000/comunidadesYproductosList/")
            .then((res) => {
                
                 let lista = res.data.sort(this.compare)
                 
                 localStorage.setItem('listaG', JSON.stringify(lista));

             })
            .catch((err) => {
                 console.log(err)
             });
             
           },

            compare: function(a, b) {
            if (a.comunidad.id < b.comunidad.id) {
             return -1;
            }
            if (a.comunidad.id > b.comunidad.id) {
                return 1;
            }
            // a debe ser igual b
            return 0;
            }
        }

    }
</script>

<style >

.obtenerTablaComProd{
    margin: 40px auto;
    width: 600px;
}

table{
    background-color: white;
    text-align: left;
    border-collapse: collapse;
    width: 100%;
}

th, td{
    padding: 10px;
}

thead{
    background-color: #246355;
    border-bottom: solid 5px #0F362D;
    color: white;
}

tr:nth-child(even){
 background-color: #ddd;   
}

tr:hover td{
    background-color: #369681;
    color: white;
}

</style>