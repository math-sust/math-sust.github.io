import Vue from "vue";
import App from "./App.vue";
import router from "./router";
/* Imports from vue-material */
import { MdButton, MdContent, MdTabs } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import VueMaterial from 'vue-material'
/* Import master CSS */
import '@/style/style.css';
// import 'vue-material/dist/theme/default.css'
// import "vue-material/dist/vue-material.min.css";
// import "vue-material/dist/theme/black-green-light.css";

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");


Vue.use(MdButton)
Vue.use(MdContent)
Vue.use(MdTabs)
Vue.use(VueMaterial)

