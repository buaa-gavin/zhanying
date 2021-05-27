<template>
  <div>
    <Nav></Nav>
    <div class="result" v-if="$store.state.isDone" v-loading="loading">
      <h1 class="loadingWord">检测中</h1>
    </div>
    <div class="result" v-else>
      <div class="resultTitle">
        <span>检测结果</span>
      </div>
      <div class="resultImage">
        <div class="originImage">
          <img :src="$store.state.originImage" />
        </div>
        <div class="predictImage">
          <img :src="$store.state.segImage" />
        </div>
      </div>
      <div class="predictClass">
        <span> 诊断结果： </span>
        <span>{{ $store.state.classResult }}</span>
      </div>
      <div class="resultButton">
        <div class="leftButton">
          <el-button type="primary" @click="backDiagnose">继续检测</el-button>
        </div>
        <div class="rightButton">
          <el-button type="success" @click="backHistory">查看病历记录</el-button>
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
  components: {
    Nav,
    Footer,
  },
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    backDiagnose() {
      this.$router.push("/diagnose");
      this.$store.commit("editIsDone");
    },
    backHistory() {
      this.$router.push("/history");
    },
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
.loadingWord {
  padding-top: 20vh;
  text-align: center;
  font-size: 40px;
  font-weight: bold;
  align-items: center;
}
</style>
