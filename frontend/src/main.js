// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'
import theme from 'muse-ui/lib/theme'

theme.add('teal', {
  primary: '#009688',
  secondary: '#ff4081',
  success: '#4caf50',
  warning: '#ffeb3b',
}, 'light');
theme.use('teal')

Vue.config.productionTip = false
Vue.use(MuseUI)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
