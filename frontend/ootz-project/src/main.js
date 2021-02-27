import Vue from 'vue'
import App from './App.vue'
import axios from "axios";
import VueRouter from "vue-router";

import Vuex from "vuex";

import { router } from "./routes";

Vue.prototype.$axios = axios;

Vue.use(VueRouter);
Vue.use(Vuex)

new Vue({
  el: '#app',
  render: h => h(App),
  router
}).$mount("#app");
