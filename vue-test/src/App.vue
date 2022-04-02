<template>
  <div id="app">
    <DevOpsTasks msg="Welcome to Your Vue.js App"/>
    <TopBar msg="Navigation Bar"/>
  </div>
</template>

<script>
import DevOpsTasks from './components/DevOpsTasks.vue'
import TopBar from './components/TopBar.vue'


export default {
  name: 'App',
  components: {
    DevOpsTasks,
    TopBar,
  },
        data() {
        return {
          ena: '',
          dyo: '',
          tag: '',
          items: '', 
          id_for_label: '',
              task: '',
              user: '',
              fields: ['user', {key: 'time', sortable: true}, 'task', 'tags'],
              totalRows: 1,
              currentPage: 1,
              filter: null,
              filterOn: ['user', 'time', 'task', 'tags'],
        }
      },
      computed: {
        taskState() {
          return this.task.length <= 10 > 1 ? false : null
      }
    },
    mounted() {
      this.ena = JSON.parse(document.getElementById('entries').textContent)
      this.dyo = JSON.parse(document.getElementById('tags').textContent)
    },
      methods: {
      onFiltered(filteredItems) {
        this.totalRows = filteredItems
        this.currentPage = true
      }
  }

}
  
</script>