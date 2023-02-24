<template lang="html">
    <div class ="container">
        <div clas ="row">
            <div class ="col text-left">
                <h2>EDITAR PERSONA</h2>
            </div>
        </div>
        <div clas = "row">
            <div class = "col">
                <div class = "card">
                    <div class = "card-body">
                        <form @submit="onSubmit">
                            <div class ="form-group row">
                                <label for="nombre" class="col-sm-2 col-form-label"></label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Nombre" name="title" class="form-control" v-model.trim="form.nombre">
                                </div>
                            </div>

                            <div class ="form-group row">
                                <label for="apellidos" class="col-sm-2 col-form-label"></label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Apellidos" name="title" class="form-control" v-model.trim="form.apellidos">
                                </div>
                            </div>
                            <div class ="form-group row">
                                <label for="telefono" class="col-sm-2 col-form-label"></label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Extension" name="title" class="form-control" v-model.trim="form.telefono">
                                </div>
                            </div>

                            <div class ="form-group row">
                                <label for="fechaIncorporacion" class="col-sm-2 col-form-label"></label>
                                <div class="col-sm-6">
                                    <input type="date" placeholder="Fecha de Destino" name="title" class="form-control" v-model.trim="form.fechaIncorporacion">
                                </div>
                            </div>

                            <!-- <div class ="form-group row">
                                <label for="empleo" class="col-sm-2 col-form-label"></label>
                                <div class="col-sm-6">
                                    <input type="select" placeholder="Empleo" name="title" class="form-control" v-model.trim="form.empleo">
                                    <select id="empleo" v-model="opcionEmpleo">
                                        <option v-for="empleo in empleos" :value="empleo">{{ empleo }}</option>
                                </select>
                                    </div>
                               
                               
                            </div> -->
                            <div class ="form-group row">
                                <label for="empleo" class="col-sm-2 col-form-label"></label>
                                <div class="col-sm-6">
                                    <!-- <input type="select" placeholder="Empleo" name="title" class="form-control" v-model.trim="form.empleo"> -->
                                    <select id="empleo" v-model="opcionEmpleo" class="form-control" v-model.trim="form.empleo">
                                        <option v-for="empleo in empleos" :value="empleo">{{ empleo }}</option>
                                </select>
                                    </div>                           
                               
                            </div>
                            <div class ="form-group row">
                                <label for="unidad" class="col-sm-2 col-form-label"></label>
                                <div class="col-sm-6">
                                    <!-- <input type="select" placeholder="Empleo" name="title" class="form-control" v-model.trim="form.empleo"> -->
                                    <select id="unidad" v-model="opcionUnidad" class="form-control" v-model.trim="form.empleo">
                                        <option v-for="empleo in empleos" :value="empleo">{{ empleo }}</option>
                                </select>
                                    </div>
                               
                               
                            </div>
                            

                            <div class ="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Editar</b-button>
                                    <b-button type="submit" class="btn-large-space" variant="danger" :to="{name:'ListaPersonas'}">Cancelar</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
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
                empleos : [
                    "General",
                    "Coronel",
                    "Teniente Coronel",        
                    "Comandante",
                    "Capitán",
                    "Teniente",
                    "Subteniente",
                    "Brigada",
                    "Sargento 1º",
                    "Sargento",
                    "Cabo Mayor",
                    "Cabo 1º",
                    "Cabo",
                    "Guardia Civil"
                ],
                departamento:[],
                unidad:['JAES','ICAE','SEPROSE','PFNA'],
                opcionEmpleo: '',
                personaId: this.$route.params.personaId,
                form: {
                    nombre:'',
                    apellidos:'',
                    empleo:'',
                    fechaIncorporacion:'',
                    telefono:'',
                    unidad:'',
                    departamento:''
                }
            }
        },
        methods:{
            onSubmit(event){
                event.preventDefault()
                const urlPersona = `http://127.0.0.1:8000/api/personas/${this.personaId}/`
                axios.patch(urlPersona).then((response) =>{
                    this.form.nombre = response.data.nombre
                    this.form.apellidos = response.data.apellidos
                    this.form.empleo = response.data.empleo
                    this.form.fechaIncorporacion = response.data.fecha_incorporacion
                    this.form.telefono = response.data.telefono
                    this.form.unidad = response.data.unidad
                    this.form.departamento = response.data.departamento
                    alert("Persona actualizada correctamente")
                }).catch((error)=>{
                    console.log(error)
                })
            
            },

            getPersona (){
                const urlPersona = `http://127.0.0.1:8000/api/personas/${this.personaId}/`
                axios.get(urlPersona).then((response) =>{
                    this.form.nombre = response.data.nombre
                    this.form.apellidos = response.data.apellidos
                    this.form.empleo = response.data.empleo
                    this.form.fechaIncorporacion = response.data.fecha_incorporacion
                    this.form.telefono = response.data.telefono
                    this.form.unidad = response.data.unidad
                    this.form.departamento = response.data.departamento
                    this.opcionEmpleo = response.data.empleo
                    
                }).catch((error)=>{
                    console.log(error)
                })
            },
            getUnidades() {
                axios.get("http://localhost:8000/api/unidades/").then((response) => {
                    this.unidades = response.data;
                });
                },
            getDepartamentos() {
                axios.get("http://localhost:8000/api/departamentos/").then((response) => {
                    this.departamentos = response.data;
                });
            
            }
        },

        created(){
            this.getPersona(),
            this.getDepartamentos();
            this.getEmpleado();
            
           
        }
    }
    
</script>
<style lang="css" scoped>
</style>
