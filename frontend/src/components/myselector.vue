<template>
  <div>
    <mu-paper :z-depth="1" class="paper">
      <mu-list style="text-align: left; padding: 0">
        <mu-list-item>
          <mu-container class="place" @click="showPlace=true">
            <mu-row>
              <mu-col span="5" class="text-center">
                <span class="bold">出发地</span><br>
                {{myFrom}}
              </mu-col>
              <mu-col span="2" class="arrow">
                <mu-icon value=":iconfont icon-right-arrow" size="20"></mu-icon>
              </mu-col>
              <mu-col span="5" class="text-center">
                <span class="bold">目的地</span><br>
                {{myTo}}
              </mu-col>
            </mu-row>
          </mu-container>
        </mu-list-item>
        <mu-divider></mu-divider>
        <mu-list-item>
          <mu-row @click="showDate=true" class="full">
            <mu-col span="5" class="title">
              出发日期
            </mu-col>
            <mu-col span="7" class="text">
              {{myDate}}
            </mu-col>
          </mu-row>
        </mu-list-item>
      </mu-list>
    </mu-paper>
    <div style="margin-top: 2%">
      <mu-button color="primary" style="width: 80%; font-weight: bold; font-size: 17px" @click="submit">
        查询
      </mu-button>
    </div>

    <div v-if="showPlace" class="picker" v-on:click="clickPlace">
      <mu-slide-picker :slots="placeSlots" :visible-item-count="5" @change="placeChange" :values="myPlace" class="picker-content-1"></mu-slide-picker>
    </div>
    <div v-if="showDate" class="picker" v-on:click="clickDate">
      <mu-date-picker color="primary" :date.sync="myStartDate" class="picker-content-2"></mu-date-picker>
    </div>
  </div>
</template>

<script>
const place = {
  '张江': ['邯郸', '枫林', '上科大'],
  '邯郸': ['张江', '江湾', '枫林'],
  '枫林': ['张江', '邯郸'],
  '江湾': ['邯郸'],
  '上科大': ['张江']
}
export default {
  name: 'myselector',
  props: {
    from: String,
    to: String,
    startDate: String,
    submit: Function
  },
  data () {
    return {
      placeSlots: [
        {
          width: '100%',
          textAlign: 'center',
          values: Object.keys(place)
        }, {
          width: '100%',
          textAlign: 'center',
          values: ['邯郸', '枫林', '上科大']
        }
      ],
      myPlace: ['张江', '邯郸'],
      myFrom: this.from,
      myTo: this.to,
      myStartDate: undefined,
      showPlace: false,
      showDate: false
    }
  },
  computed: {
    myDate: function() {
      if (this.myStartDate !== undefined) {
        let year = this.myStartDate.getFullYear()
        let month = this.myStartDate.getMonth() + 1
        let date = this.myStartDate.getDate()
        return year + '-' + month + '-' + date
      } else {
        let curDate = new Date()
        return curDate.getFullYear() + '-' + (curDate.getMonth() + 1) + '-' + curDate.getDate()
      }
    }
  },
  watch: {
    myFrom (val) {
      this.$emit('update:from', val)
    },
    myTo (val) {
      this.$emit('update:to', val)
    },
    myDate (val) {
      this.$emit('update:startDate', val)
    }
  },
  methods: {
    placeChange (value, index) {
      switch (index) {
        case 0:
          this.myFrom = value
          const arr = place[value]
          this.placeSlots[1].values = arr
          this.myTo = arr[0]
          break
        case 1:
          this.myTo = value
          break
      }
      this.myPlace = [this.myFrom, this.myTo]
    },
    clickPlace (event) {
      if (event.target.className.toLowerCase() === "picker")
        this.showPlace = false
    },
    clickDate () {
      if (event.target.className.toLowerCase() === "picker")
        this.showDate = false
    }
  }
};
</script>

<style scoped>
.paper {
  margin-top: 10px;
  margin-left: 10%;
  width: 80%;
  max-width: 256px;
  max-width: 460px;
  background: rgba(255, 255, 255, 1);
}
.title {
  text-align: center;
  font-weight: bold;
  font-size: 17px;
}
.text {
  text-align: center;
  font-size: 17px;
}
.arrow {
  text-align: center;
  top: 10px;
}
.full {
  width: 100%;
}
.place {
  padding: 8px;
}
.text-center {
  text-align: center;
  font-size: 17px;
}
.bold {
  font-weight: bold;
}
.picker {
  background: rgba(157, 157, 157, 0.5);
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
}
.picker-content-1 {
  position: absolute;
  bottom: 0;
  width: 100%;
}
.picker-content-2 {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
</style>