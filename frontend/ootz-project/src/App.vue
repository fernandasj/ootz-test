<template>
  <div id="app">
     <section class="hero is-primary is-bold is-fullheight">
      <!-- Hero head: will stick at the top -->
      <div class="hero-head">
        <nav class="navbar">
          <div class="container">
            <div class="navbar-brand">
              <a class="navbar-item">
                OOTZ Project 1.0
              </a>
            </div>
          </div>
        </nav>
      </div>

      <div class="hero-body">
          <div class="container has-text-centered">
              <div class="row">
                  <div class="columns">
                      <div class="column is-half is-offset-one-quarter">
                          <router-view></router-view>
                      </div>
                  </div>
              </div>
          </div>
      </div>

      <!-- Hero footer: will stick at the bottom -->
      <div class="hero-foot">
        <div class="container">
          <div class="content has-text-centered">
            <p>
              <strong>OOTZ Project</strong> by <a href="http://github.com/fernandasj">Fernanda Vieira</a>.
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'app',
  // data () {
  //   return {
  //     // msg: 'Hello, World!'
  //   }
  // }
}
</script>

<style>
</style>
