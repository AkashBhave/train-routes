import Vue from 'vue';
import App from './App.vue';
// Axios
import axios from 'axios';
import vueAxios from 'vue-axios';

Vue.config.productionTip = false;

new Vue({
    render: function(h) {
        return h(App);
    }
}).$mount('#app');

Vue.use(vueAxios, axios);
