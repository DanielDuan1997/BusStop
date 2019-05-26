<template>
  <mu-container class="center">
    <mylogo></mylogo>
    <myselector :from.sync="from" :to.sync="to" :start-date.sync="startDate" :submit="submit"></myselector>
    <mu-list v-if="!this.err">
    </mu-list>
    <div v-else class="error-text">
      无法连接到服务器
    </div>
  </mu-container>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      from: '张江',
      to: '邯郸',
      startDate: '',
      err: false,
    }
  },
  methods: {
    submit () {
      if (this.startDate === '') {
        let curDate = new Date()
        this.startDate = curDate.getFullYear() + '-' + (curDate.getMonth() + 1) + '-' + curDate.getDate()
      }
      let formData = new FormData()
      formData.append('from', this.from[0])
      formData.append('to', this.to[0])
      formData.append('date', this.startDate)
      let opts = {
        head: {'content-type' : 'application/x-www-form-urlencoded'},
        method: 'POST',
        body: formData
      }
      fetch('http://0.0.0.0:5001/', opts)
        .then(response => this.callback(response.text()))
        .catch(response => {this.err = true})
    },
    callback(response) {
      console.log(response)
    }
  }
};
</script>

<style>
.center {
  text-align: center;
  padding: 10px;
}
.error-text {
  margin-top: 10px;
}
</style>
