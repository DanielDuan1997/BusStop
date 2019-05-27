<template>
  <mu-container class="center">
    <mylogo></mylogo>
    <myselector :from.sync="from" :to.sync="to" :start-date.sync="startDate" :submit="submit"></myselector>
    <div v-if="!err" class="main-area">
      <div class="bus-title">{{data.notice}}</div>
      <div v-if="data.schedule.length">
        <div v-for="(bus, index) in data.schedule" :class="getStyle(data.style[index])">
          <span class="bus-text">{{bus}}: &nbsp; {{ori_from}} &nbsp; -> &nbsp; {{ori_to}}</span>
        </div>
      </div>
      <div v-else>
        当日无校车
      </div>
    </div>
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
      ori_from: '张江',
      ori_to: '邯郸',
      startDate: '',
      err: false,
      data: {'notice': undefined, 'schedule': []}
    }
  },
  created: function () {
    this.submit()
  },
  methods: {
    submit () {
      if (this.startDate === '') {
        let curDate = new Date()
        this.startDate = curDate.getFullYear() + '-' + (curDate.getMonth() + 1) + '-' + curDate.getDate()
      }
      let formData = new FormData()
      formData.append('from', this.from)
      formData.append('to', this.to)
      formData.append('date', this.startDate)
      let opts = {
        head: {'content-type' : 'application/x-www-form-urlencoded'},
        method: 'POST',
        body: formData
      }
      fetch('http://0.0.0.0:5001/', opts)
        .then(response => response.text())
        .then(text => this.callback(text))
        .catch(response => {this.err = true})
    },
    sameDate (date_1, date_2) {
      return date_1.getFullYear() == date_2.getFullYear()
          && date_1.getMonth() == date_2.getMonth()
          && date_1.getDate() == date_2.getDate()
    },
    callback (text) {
      this.ori_from = this.from
      this.ori_to = this.to
      this.data = JSON.parse(text)
      let length = this.data.schedule.length
      this.data.style = new Array(length)
      let curTime = new Date()
      let busDate = this.startDate.split('-')
      let curBusTime = new Date()
      curBusTime.setFullYear(Number(busDate[0]), Number(busDate[1]) - 1, Number(busDate[2]))
      let sameDate = this.sameDate(curTime, curBusTime)
      for (let i=0; i<length; i++) {
        let busTime = this.data.schedule[i].split(':')
        curBusTime.setHours(Number(busTime[0]), Number(busTime[1]))
        if (curBusTime < curTime)
          this.data.style[i] = 0
        else if (sameDate && (i == 0 || this.data.style[i - 1] == 0))
          this.data.style[i] = 1
        else
          this.data.style[i] = 2
      }
    },
    getStyle (tp) {
      if (tp == 0)
        return "bulletin0"
      else if (tp == 1)
        return "bulletin1"
      else
        return "bulletin2"
    }
  }
};
</script>

<style>
.center {
  text-align: center;
  padding: 10px;
}
.main-area {
  margin-top: 10px;
  z-index: -1;
}
.bulletin0 {
  background: rgba(255, 255, 255, 0.4);
  height: 50px;
  width: 45%;
  margin: 10px 2%;
  border: 2px dashed rgba(128, 203, 196, 0.4);
  border-radius: 10px;
  text-align: center;
  float: left;
  color: rgba(128, 203, 196, 0.4);
}
.bulletin1 {
  background: #ffffff;
  height: 50px;
  width: 45%;
  margin: 10px 2%;
  border: 2px dashed red;
  border-radius: 10px;
  text-align: center;
  float: left;
  font-weight: bold;
}
.bulletin2 {
  background: #ffffff;
  height: 50px;
  width: 45%;
  margin: 10px 2%;
  border: 2px dashed #80cbc4;
  border-radius: 10px;
  text-align: center;
  float: left;
}
.bus-title {
  font-size: 15px;
  font-weight: bold;
}
.bus-text {
  line-height: 50px;
  font-size: 13px;
}
.error-text {
  margin-top: 10px;
}
</style>
