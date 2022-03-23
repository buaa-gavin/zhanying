<template>
  <div>
    <Nav></Nav>
    <div class="patientContent">
      <div class="infoPart">
        <div class="iconHead">
          <i class="el-icon-user-solid"></i>
        </div>
        <div class="basicInfo">
          <div class="nameTitle">
            <span>姓名： {{ patientInfo.name }}</span>
          </div>
          <div class="generalWord">
            <span class="titleWord">ID： </span><span class="vueWord">{{ patientInfo.id }}</span> <span class="titleWord">上次就诊日期： </span><span class="vueWord">{{ patientInfo.updated }}</span>
          </div>
          <div class="generalWord">
            <span class="titleWord">性别： </span><span class="vueWord">{{ patientInfo.sex }}</span> <span class="titleWord">出生日期： </span><span class="vueWord">{{ patientInfo.birth }}</span>
          </div>
        </div>
      </div>
      <div class="splitLine"></div>

      <div class="result">
        <div class="resultBlock" v-for="item in patientInfo.diagnose_set" :key="item">
          <div class="diagnoseTime">
            <i class="el-icon-time" style="margin-right:5px"></i>
            <span>检测时间： </span>
            <span>{{ formatted_time(item.updated) }}</span>
          </div>
          <div class="patientImage">
            <img class="patientOrigin" :src="item.content" />
            <img class="patientPredict" :src="item.semantic" />
          </div>
          <div class="patientResult">
            <i class="el-icon-warning-outline" style="margin-right:5px"></i>
            <span>检测结果： </span>
            <span>{{ item.status }}</span>
          </div>
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
  data: function() {
    return {
      patientInfo: null,
    };
  },
  mounted() {
    //this.patientInfo = response.data
    axios.get("/api/InfoList/" + this.$route.params.id).then((response) => {
      console.log(response);
      console.log(response.data);
      this.patientInfo = response.data;
      console.log(this.patientInfo.updated.substring(0, 10));
      this.patientInfo.updated = this.patientInfo.updated.substring(0, 10);
      if (this.patientInfo.sex === "f") {
        this.patientInfo.sex = "女";
      } else if (this.patientInfo.sex === "m") {
        this.patientInfo.sex = "男";
      } else {
        this.patientInfo.sex = "未知";
      }
    });
  },
  methods: {
    formatted_time: function(iso_date_string) {
      const date = new Date(iso_date_string);

      return date.toLocaleDateString();
    },
  },
};
</script>

<style>
.patientContent {
  margin-bottom: 5px;
}
.infoPart {
  margin-left: 10vw;
  height: 20vh;
  margin-top: 5vh;
  margin-bottom: 5vh;
  display: flex;
}
.iconHead {
  height: 20vh;
  font-size: 15vh;
}
.basicInfo {
  margin-left: 5vh;
  text-align: left;
}
.nameTitle {
  margin-top: 30px;
  font-size: 20px;
  font-weight: bold;
}
.titleWord {
  font-weight: bold;
}
.vueWord {
  margin-right: 40px;
}
.generalWord {
  margin-top: 20px;
  font-size: 13px;
}
.splitLine {
  position: relative;
  margin: 0 auto;
  width: 600px;
  height: 1px;
  background-color: #d4d4d4;
  text-align: center;
  font-size: 16px;
  color: rgba(101, 101, 101, 1);
}
.result {
  margin-left: 10vw;
  margin-right: 10vw;
  margin-top: 10vh;
}
.resultBlock {
  padding: 10px;
  margin-bottom: 10vh;
  border-radius: 2px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.diagnoseTime {
  text-align: center;
  margin: 10px;
  font-size: 20px;
  font-weight: 500;
  align-items: center;
}
.patientResult {
  text-align: center;
  margin: 10px;
  font-size: 20px;
  font-weight: 500;
  align-items: center;
}
.patientImage {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 20px;
  margin-right: 20px;
  display: flex;
  justify-content: space-between;
}
.patientOrigin {
  width: 32vw;
  margin-left: 4vw;
}
.patientPredict {
  width: 32vw;
  margin-right: 4vw;
}
</style>
