<template>
  <div>
    <Nav></Nav>
    <div class="result">
      <div class="resultTitle">
        <span>检测结果</span>
      </div>
      <div class="resultImage">
        <img class="originImage" :src="$store.state.originImage" />
        <img class="predictImage" :src="$store.state.segImage" />
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
      loading: true,
    };
  },
  methods: {
    backDiagnose() {
      this.$router.push("/diagnose");
    },
    backHistory() {
      this.$router.push("/history");
    },
  },
};
</script>

<style>
.result {
  margin-top: 5px;
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
  margin-left: 20px;
  margin-right: 20px;
  display: flex;
  justify-content: space-between;
}
.originImage {
  width: 32vw;
  margin-left: 4vw;
}
.predictImage {
  width: 32vw;
  margin-right: 4vw;
}
.predictClass {
  margin-top: 5vh;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
}
.resultButton {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
}
.leftButton {
  text-align: center;
  align-items: center;
  margin-left: 25vw;
}
.rightButton {
  text-align: center;
  align-items: center;
  margin-right: 25vw;
  margin-bottom: 5vh;
}
.loadingWord {
  padding-top: 20vh;
  text-align: center;
  font-size: 40px;
  font-weight: bold;
  align-items: center;
}
</style>
