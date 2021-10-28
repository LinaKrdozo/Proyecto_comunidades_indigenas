<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Inventarios productos <br /> comunidades indigenas</h1>
      <nav>
      <button v-if="!isAuth" v-on:click="loadHome">Home</button>
      <button v-if="!isAuth" v-on:click="loadIngresoFormularioComunidades">Comunidad</button>
      <button v-if="!isAuth" v-on:click="loadIngresoFormularioProductos">Producto</button> 
      <button v-if="!isAuth" v-on:click="loadIngresoFormularioComunidadesProductos">Producto por comunidad</button> 
      <button v-if="!isAuth" v-on:click="loadTablaComunidadesProductos">Tabla Producto por comunidad</button> 
  
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedHome = "completedHome"
        v-on:completedIngresoFormularioComunidades = "completedIngresoFormularioComunidades"
        v-on:completedIngresoFormularioProductos = "completedIngresoFormularioProductos"
        v-on:completedIngresoFormularioComunidadesProductos = "completedIngresoFormularioComunidadesProductos"
        v-on:completedTablaComunidadesProductos = "completedTablaComunidadesProductos"
        >
      </router-view>
    </div>
  
    <div class="footer">
      <hr>
      <h2>MisionTic 2022-p8 Course</h2>
    </div>
  </div>
</template>

<script>
  export default{
    name: 'App',
  
  data: function(){
      return {
        isAuth: false
      }
    },

    Components: {
    },

    methods:{

      verifyAuth: function(){
        this.isAuth = localStorage.getItem("isAuth") || false;
        if(this.isAuth == false){
          this.$router.push({name: "home"})
        }
        else{
          this.$router.push({name: "home"});
        }
      },

      loadHome: function(){
        this.$router.push({name: "home"});
      },

      loadIngresoFormularioComunidades: function(){
        this.$router.push({name: "formularioComunidades"})
      },

       loadIngresoFormularioProductos: function(){
        this.$router.push({name: "formularioProductos"})
      },

      loadIngresoFormularioComunidadesProductos: function(){
        this.$router.push({name: "formularioComProd"})
      },

      loadTablaComunidadesProductos : function(){
        this.$router.push({name: "formularioTabla"})
      },

      completedcompletedHome: function(data){
        this.completedcompletedHome(data);
      },  

      completedIngresoFormularioComunidades: function(data){
        alert("Registro exitoso");
        localStorage.setItem("comunidad", data.comunidad);
        this.completedIngresoFormularioComunidades(data);
      },

      completedIngresoFormularioProductos: function(data){
        alert("Registro exitoso");
        this.completedIngresoFormularioProductos(data);
        
      }, 
      completedIngresoFormularioComunidadesProductos:function(data){
        alert("Registro exitoso");
        this.completedIngresoFormularioComunidadesProductos(data);
      },

      completedTablaComunidadesProductos:function(data){
        alert("Registro exitoso");
        this.completedIngresoFormularioComunidadesProductos(data);
      }

    },
    
     created: function(){
      this.verifyAuth();
    }
    
  }

</script>


<style>
   *{
      margin:0;
      padding: 0;
      box-sizing: border-box;
    }
  .header{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    background-color:#FF9F1C;
    color:#0F362D ;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header h1{
    width: 30%;
    text-align: center;
    font-size: 150%;
  }

  .header nav {
    height: 150%;
    width: 65%;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
  .header nav button{
    color: #000;
    background: #FF9F1C;
    border: 1px solid #FF9F1C;
    border-radius: 50px;
    padding: 10px;
    text-transform: uppercase;
    text-decoration: none;
    /*margin:px;*/
    font-size: 12px;
    
  }
  .header nav button:hover{
    color: #0F362D;
    background: #E5E7E9;
    border: 1px solid #E5E7E9;
  }
  .main-component{
    height: 75vh;
    margin: 0%;
    padding: 0%;
    background: #FFF;
    align-content: center;
  }
  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 1px;
    background-color: #FFF;
    color: #373737;
    line-height: 1.5;
  }
  .footer h2{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
  }

  .footer hr{
    height: 2px;
    background-color: #0F362D;
    justify-content: center;
    align-items: center;
    
  }
</style>
