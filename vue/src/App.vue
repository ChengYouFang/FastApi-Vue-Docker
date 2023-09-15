<template>
  <div>
    <input type="text" v-model="msg"><br>
    <button @click="sendMessage">發送</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  methods: {
    //取得執行結果
    getResult() {
      axios.get(`http://localhost:7666/get_task_result/${this.taskID}`, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(res => {
        const result = res.data
        if (result.status === 1) {
          alert(result.result.name)
          this.taskID = null
        } else if (result.status === 3) {
          alert('Some issue')
          this.taskID = null
        } else {
          setTimeout(this.getResult, 1000)
        }
      })
    },
    sendMessage() {
      if (this.msg && !this.taskID) {
        axios.post('http://localhost:7666/create_task', {name: this.msg}, {
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(res => {
          console.log()
          this.msg = null
          this.taskID = res.data.id
          setTimeout(this.getResult, 1000)
        })
      }
    }
  },
  data() {
    return {
      msg: null,
      taskID: null
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
