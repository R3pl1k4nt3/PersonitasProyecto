import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListaPersonas from '@/components/Personas/ListaPersonas'
import EditarPersona from '@/components/Personas/EditarPersona'
import EditPersona from '@/components/Personas/EditPersona'
import NewPersona from '@/components/Personas/NewPersona'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/personas',
      name: 'ListaPersonas',
      component: ListaPersonas
    },
    {
      path: '/personas/:personaId/editar',
      name: 'EditarPersona',
      component: EditarPersona
    },
    {
      path: '/personas/:personaId/edit',
      name: 'EditPersona',
      component: EditPersona
    },
    {
      path: '/personas/newPersona',
      name: 'NewPersona',
      component: NewPersona
    },
  ],
  mode: 'history'
})
