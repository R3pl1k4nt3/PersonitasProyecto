import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListaPersonas from '@/components/Personas/ListaPersonas'
import EditPersona from '@/components/Personas/EditPersona'

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
      path: '/personas/:personaId/edit',
      name: 'EditPersona',
      component: EditPersona
    },
  ],
  mode: 'history'
})
