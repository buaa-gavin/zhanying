import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
//注册element-ui
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

import Axios from 'axios'

Vue.use(ElementUI);

Vue.config.productionTip = false

Axios.defaults.baseURL = 'http://localhost:8888/'
Axios.defaults.withCredentials = true
Vue.prototype.$axios = Axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
