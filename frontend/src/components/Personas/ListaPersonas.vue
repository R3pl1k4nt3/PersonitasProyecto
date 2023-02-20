<template lang="html">
    <div class ="container">
        <div clas ="row">
            <div class ="col text-left">
                <h2>Listado de personas</h2>
                <div class ="col-md-12">
                    <b-table striped hover :items="personas" :fields="fields">
                        
                        <template slot=cell(action) slot-scope="data" >
                            <b-button size="sm" variant="primary">
                                EDITAR
                            </b-button>
                            <b-button size="sm" variant="danger">
                                ELIMINAR
                            </b-button>
                        </template>                     
                    </b-table>
                </div>
              
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data () {
            return{
                fields: [
                    {key:'nombre', label: 'Nombre '},
                    {key:'apellidos', label: 'Apellidos' },
                    {key:'empleo', label: 'Empleo' },
                    {key:'action', label: 'ACCION' },

                    //{key:'unidad', label: 'Unidad' },
                    //{key:'departamento', label: 'Departamento' }
                ],
                personas: []
            }
        },
        methods:{
            getPersonas() {
                const urlPersonas = 'http://127.0.0.1:8000/api/personas/'
                axios.get(urlPersonas).then((response) =>{
                    this.personas = response.data;
                    console.log(response.data);
                })
                
                .catch((error) =>{
                    console.log(error)
                })
            }
            },

        created(){
            this.getPersonas()
            console.log(this.personas)
        }
    }
    
</script>
<style lang="css" scoped>
</style>
