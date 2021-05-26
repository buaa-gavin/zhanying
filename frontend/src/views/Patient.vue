<template>
  <div>
    <Nav></Nav>
    <div class="content">
      <div class="infoPart">
        <div class="iconHead">
          <i class="el-icon-user-solid"></i>
        </div>
        <div class="basicInfo">
          <div class="nameTitle">
            <span>姓名： {{ patientInfo.name }}</span>
          </div>
          <div class="generalWord">
            <span class="titleWord">ID： </span><span class="vueWord">{{ patientInfo.id }}</span> <span class="titleWord">初诊日期： </span><span class="vueWord">{{ patientInfo.date }}</span>
          </div>
          <div class="generalWord">
            <span class="titleWord">性别： </span><span class="vueWord">{{ patientInfo.sex }}</span> <span class="titleWord">出生日期： </span><span class="vueWord">{{ patientInfo.birthday }}</span>
          </div>
        </div>
      </div>
      <div class="splitLine"></div>
      <div class="result">---</div>
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
  //   mounted() {
  //     axios.get("/api/InfoList/" + this.$route.params.id).then((response) => (this.info = response.data));
  //   },
  data: function() {
    return {
      patientInfo: {
        id: "1",
        name: "a",
        sex: "男",
        birthday: "2000-05-26",
        date: "2021-05-26",
      },
    };
  },
};
</script>

<style>
.content {
  height: 70vh;
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
  margin-right: 20px;
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
  margin-top: 30px;
}
</style>
