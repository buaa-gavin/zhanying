<template>
  <div class="index">
    <Nav></Nav>
    <div class="content">
      <div class="indexTitle">
        <span class="words">
          <h2>欢迎使用湛影系统</h2>
        </span>
        <br />
        <span class="words">
          <h2>点击按钮开始检测或者查看病历记录</h2>
        </span>
      </div>

      <div class="buttons">
        <div class="ubutton">
          <el-button type="primary" @click="diagnose">检测</el-button>
        </div>
        <div class="checkbutton">
          <el-button type="success" @click="history">病历记录</el-button>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
export default {
  components: {
    Nav,
    Footer,
  },
  methods: {
    diagnose() {
      this.$router.push("/diagnose");
    },
    history() {
      this.$router.push("/history");
    },
  },
};
</script>

<style>
.index {
  height: 100vh;
}
.indexTitle {
  margin-top: 5vh;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  margin-left: 25vw;
  margin-right: 25vw;
  padding: 5px;
}
.content {
  height: 65vh;
}
.words {
  width: 100vw;
  height: 20px;
  font-size: 20px;
  text-align: center;
}
.buttons {
  margin-top: 10vh;
  width: 100vw;
  display: flex;
  justify-content: space-between;
}
.ubutton {
  text-align: center;
  align-items: center;
  margin-left: 40vw;
}
.checkbutton {
  text-align: center;
  align-items: center;
  margin-right: 40vw;
}
</style>
