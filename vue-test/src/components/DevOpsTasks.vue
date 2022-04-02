<template>
  <div id="app">
  <b-navbar toggleable="lg" fixed="top" type="dark" variant="dark">
    <b-navbar-brand><img src="img/logo_full.png" id="logo"/></b-navbar-brand>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#" title="Work In Progress..." disabled>Stats</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="logout">Logout</b-nav-item>
        <!-- <b-nav-item>{{username}}</b-nav-item> TODO -->
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>

  <b-container fluid>
    <b-form method="post">
      <b-row>
        <b-col>
            {% csrf_token %}
            <b-input-group>
              <b-form-input type="text" name="user" maxlength="100" required id="id_user" v-model="user" placeholder="User..." :state="taskState"></b-form-input>
              <b-form-input type="text" name="task" maxlength="100" required id="id_task" v-model="task" placeholder="Task.." :state="taskState"></b-form-input>
              <b-button type="submit" variant="info">Save</b-button>
              <b-button @click="task = '', user = ''" variant="info">Clear</b-button>
            </b-input-group>
        </b-col>
      </b-row>
      <b-row>
       <b-col>
        {% for tag in tags %}
          <label :for="tag.id_for_label"><p></p>
            <b-form-checkbox-group name="tags" switches>
              <b-form-checkbox name="tags" :id="id_for_label" :value="tag.tag">{{tag.tag}}</b-form-checkbox>
            </b-form-checkbox-group>
          </label>
        {% endfor %}
        </b-col>
      </b-row>

  </b-form>
 </b-container>


<p></p>


        <b-container fluid>
          <b-row>
            <b-col>
                <b-input-group>
                  <b-form-input
                    id="filter-input"
                    v-model="filter"
                    type="search"
                    placeholder="Search: User / Time / Task / Tag"
                  ></b-form-input>

                  <b-input-group-append>
                    <b-button :disabled="!filter" @click="filter = ''" variant="dark">Clear</b-button>
                  </b-input-group-append>
                </b-input-group>
            </b-col>
          </b-row>
  
          <!-- Main table element -->
          <b-table
            id="datatable"
            :items="ena"
            :fields="fields"
            :current-page="currentPage"
            :filter="filter"
            :filter-included-fields="filterOn"
            show-empty="false"
            responsive="true"
            hover
            dark
            fixed="true"
            head-variant="dark"
            sticky-header="1700vh"
            @filtered="onFiltered"
            :sort-compare-options="{ numeric: true, sensitivity: 'base' }"
          ></b-table>
        </b-container>
  </div>
</template>

<script>

export default {
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