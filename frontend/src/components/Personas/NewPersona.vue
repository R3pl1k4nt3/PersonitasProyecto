<template>
    <div>
      <h1>Nuevo Empleado</h1>
      <form @submit.prevent="crearEmpleado">
        <div>
            <label for="empleo">Empleo:</label>                
                                    <!-- <input type="select" placeholder="Empleo" name="title" class="form-control" v-model="form.empleo"> -->
                <select id="empleo" v-model="empleado.empleo">
                    <option v-for="empleo in empleos" :value="empleo">{{ empleo }}</option>
                </select>              
        </div>
        <div>
          <label for="nombre">Nombre:</label>
          <input type="text" v-model="empleado.nombre" id="nombre" />
        </div>
        <div>
          <label for="apellidos">Apellidos:</label>
          <input type="text" v-model="empleado.apellidos" id="apellidos" />
        </div>
        <div>
          <label for="telefono">Teléfono:</label>
          <input type="text" v-model="empleado.telefono" id="telefono"  />
        </div>
        <div>
          <label for="fecha_incorporacion">Fecha de Incorporación:</label>
          <input type="date" v-model="empleado.fecha_incorporacion" id="fecha_incorporacion" />
        </div>
        <!-- <div>
          <label for="fotografia">Fotografía:</label>
          <input type="file" v-on:change="onFileChange" />
        </div> -->
        <div>
          <label for="unidad">Unidad:</label>
          <select id="unidad" v-model="empleado.unidad" required>
            <option value="" disabled>Selecciona una unidad</option>
            <option v-for="unidad in unidades" :key="unidad.id" :value="unidad.url">{{ unidad.unidad }}</option>
          </select>
        </div>
        <div>
          <label for="departamento">Departamento:</label>
          <select id="departamento" v-model="empleado.departamento" required>
            <option value="" disabled>Selecciona un departamento</option>
            <option v-for="departamento in departamentos" :key="departamento.id" :value="departamento.url">{{ departamento.departamento }}</option>
          </select>
        </div>
        <button type="submit">Crear Empleado</button>
      </form>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  name: 'CrearEmpleado',
  data() {
    return {
      empleado: {
        empleo: null,
        nombre: 'aaa',
        apellidos: 'aaa',
        telefono: 'aaa',
        fecha_incorporacion: null,
        fotografia: null,
        unidad: null,
        departamento: null,
      },
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
        opcionEmpleo: '',        
        unidades: [],
        departamentos: [],
        
     
        };
    },
    created() {
 
    axios.get('http://localhost:8000/api/unidades/')
    .then((response) =>{
      console.log(response.data)
      this.unidades = response.data;
      })

      axios.get('http://localhost:8000/api/departamentos/')
      .then((response) =>{
         console.log(response.data)
         this.departamentos = response.data;
         
      })
    },
    methods:{

    crearEmpleado(){    
      // const unidadResponse =  axios.get(this.empleado.unidad);
      // const departamentoResponse =  axios.get(this.empleado.departamento);

      // const empleado = {unidad: unidadResponse.data.url,
      //   departamento: departamentoResponse.data.url
      //   empleo: this.empleado.empleo,
      //   nombre: this.empleado.nombre,
      //   apellidos: this.empleado.apellidos,
      //   fecha_incorporacion : this.empleado.fecha_incorporacion,
      //   fotografia: null,
      //   telefono: this.empleado.telefono,
      //   unidad: unidadResponse.data.url,
      //   departamento: departamentoResponse.data.url
      // };
      console.log(this.empleado)
      axios.post('http://localhost:8000/api/personas/', this.empleado)
      .then((response) =>{
         console.log(response.data)
      })
    }
  }
};
   
  


</script>