<template>
  <div>
    <Nav></Nav>
    <div class="result">
      <div class="resultTitle">
        <span>检测结果</span>
      </div>
      <div class="resultImage">
        <div class="originImage">
          <img :src="originImage" />
        </div>
        <div class="predictImage">
          <img :src="predictImage" />
        </div>
      </div>
      <div class="predictClass">
        <span> 诊断结果： </span>
        <span>{{ classResult }}</span>
      </div>
      <div class="resultButton">
        <div class="leftButton">
          <el-button type="primary" @click="diagnose">继续检测</el-button>
        </div>
        <div class="rightButton">
          <el-button type="success" @click="history">查看病历记录</el-button>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import axios from "axios";
export default {
  mounted() {},
  components: {
    Nav,
    Footer,
  },
  data() {
    return {
      originImage: "../assets/logo.png",
      predictImage: "../assets/logo.png",
      classResult: "正常",
    };
  },
};
</script>

<style>
.result {
  height: 75vh;
}
.resultTitle {
  margin-top: 5vh;
  text-align: center;
  font-size: 25px;
  font-weight: bold;
  align-items: center;
}
.resultImage {
  margin-top: 5vh;
  display: flex;
  justify-content: space-between;
}
.originImage {
  margin-left: 10vw;
}
.predictImage {
  margin-right: 10vw;
}
.predictClass {
  margin-top: 5vh;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
}
.resultButton {
  margin-top: 20px;
  width: 100vw;
  display: flex;
  justify-content: space-between;
}
.leftButton {
  text-align: center;
  align-items: center;
  margin-left: 30vw;
}
.rightButton {
  text-align: center;
  align-items: center;
  margin-right: 30vw;
}
</style>
