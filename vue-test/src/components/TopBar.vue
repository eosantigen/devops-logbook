<template>

<div id="navbar"  fluid style="overflow: hidden;">
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
</div>

</template>