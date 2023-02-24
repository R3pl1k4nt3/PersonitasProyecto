<template>
    <div>
      <h2>Editar GC JAES</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="empleo">Empleo:</label>
          <input type="text" id="empleo" v-model="empleado.empleo">
        </div>
        <div>
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" v-model="empleado.nombre">
        </div>
        <div>
          <label for="apellidos">Apellidos:</label>
          <input type="text" id="apellidos" v-model="empleado.apellidos">
        </div>
        <div>
          <label for="telefono">Teléfono:</label>
          <input type="text" id="telefono" v-model="empleado.telefono">
        </div>
        <div>
          <label for="fecha_incorporacion">Fecha de Incorporación:</label>
          <input type="date" id="fecha_incorporacion" v-model="empleado.fecha_incorporacion">
        </div>
        <div>
        <label for="fotografia">Fotografía:</label>
        <input type="file" ref="fotografiaInput" id="fotografia" v-on:change="onFileChange" />
      </div>
        <div>
          <label for="unidad">Unidad:</label>
          <input type="text" id="unidad" v-model="empleado.unidad.nombre">
        </div>
        <div>
          <label for="departamento">Departamento:</label>
          <input type="text" id="departamento" v-model="empleado.departamento.nombre">
        </div>
        <button type="submit">Actualizar</button>
      </form>
    </div>
  </template>

<script>
    import axios from 'axios';
        export default {
            data() {
                return {
                empleado: {
                    empleo: "",
                    nombre: "",
                    apellidos: "",
                    telefono: "",
                    fecha_incorporacion: "",
                    fotografia: null,
                    unidad: null,
                    departamento: null,
                },
                unidades: [],
                departamentos: [],
                };
            },
            created() {
                this.getUnidades();
                this.getDepartamentos();
                this.getEmpleado();
            },
            methods: {
                getUnidades() {
                axios.get("http://localhost:8000/api/unidades/").then((response) => {
                    this.unidades = response.data;
                });
                },
                getDepartamentos() {
                axios.get("http://localhost:8000/api/departamentos/").then((response) => {
                    this.departamentos = response.data;
                });
                },
                getEmpleado() {
                const idEmpleado = this.$route.params.id;
                axios.get(`http://localhost:8000/api/empleados/${idEmpleado}/`).then((response) => {
                    this.empleado = response.data;
                });
                },
                actualizarEmpleado() {
                const idEmpleado = this.$route.params.id;
                const formData = new FormData();
                formData.append("empleo", this.empleado.empleo);
                formData.append("nombre", this.empleado.nombre);
                formData.append("apellidos", this.empleado.apellidos);
                formData.append("telefono", this.empleado.telefono);
                formData.append("fecha_incorporacion", this.empleado.fecha_incorporacion);
                formData.append("unidad", this.empleado.unidad);
                formData.append("departamento", this.empleado.departamento);
                formData.append("fotografia", this.empleado.fotografia);
                axios
                    .patch(`http://localhost:8000/api/empleados/${idEmpleado}/`, formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                    })
                    .then(() => {
                    this.$router.push({ name: "Empleado", params: { id: idEmpleado } });
                    });
                },
            },
        };
</script>