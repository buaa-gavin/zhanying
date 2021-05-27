<template>
  <div>
    <Nav></Nav>
    <div class="content">
      <div class="upimg">
        <input
               v-on:change="uploadImage"
               type="file"
               id="file"
        >
        <!--        <el-upload-->
<!--            type="file"-->
<!--            id="file"-->
<!--            action="' '"-->
<!--            :class="uploadDisabled"-->
<!--            list-type="picture-card"-->
<!--            :limit="1"-->
<!--            show-file-list-->
<!--            :auto-upload="true"-->
<!--            :on-change="change"-->
<!--            :on-remove="recover"-->
<!--            multiple-->
<!--            :http-request="uploadImage"-->
<!--        >-->
          <i class="el-icon-plus" style="height:300px,width:300px"></i>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <img class="imgPre" width="100%" :src="dialogImageUrl" alt="" />
        </el-dialog>
      </div>
      <div class="upid">
        <span></span>
        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="病人ID" prop="pid">
            <el-input type="text" v-model="ruleForm.pid" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <span class="spanright"></span>
      </div>
      <div class="upbutton">
        <el-button type="primary" @click="uploadID">检测</el-button>
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
  mounted() {
    this.$store.commit("editIsDone");
  },
  data() {
    var validateID = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入ID"));
      } else {
        callback();
      }
    };
    return {
      dataList: "",
      dialogImageUrl: "",
      uploadDisabled: "", //是否隐藏
      imageID: "",
      ruleForm: {
        pid: "",
      },
      rules: {
        pid: [{ validator: validateID, trigger: "blur" }],
      },
    };
  },
  methods: {
    //单独发送图片
    uploadImage(e) {
      //   console.log(this.ruleForm.pid);
      // 发送 POST 请求
      let config = {
        headers: {
          "Content-Type": "multipart/form-data", //设置headers
        },
      };
      const file = e.target.files[0];
      let formData = new FormData();
      formData.append("content",file)

      var that = this;
      // 首先判断是否上传了图片，如果上传了图片，将图片存入到formData中
      // console.log(this.dataList);
      // if (this.dataList) {
      //   that.dataList.forEach((item, index) => {
      //     // console.log(item)
      //     formData.append(index, item);
      //   });
      // }
      // console.log(formData.get(0));
      axios
        .post(
          "/api/diagnose/", //请求后端的url
          formData,
          config
        )
        .then((res) => {
          console.log(res.data);
          this.$store.commit("editOrigin", res.data.content);
          this.$store.commit("editImage", res.data.semantic);
          this.$store.commit("editResult", res.data.status);
          this.$store.commit("editIsDone");
          this.imageID = res.data.id;
          console.log(res.data);
        })
        .catch((error) => {
          console.log("请求失败");
        });
      //用户可以在上传完成之后将数组给清空，这里直接跳转到首页了，没有做清空的操作
    },
    change(file, fileList) {
      //将每次图片数组变化的时候，实时的进行监听，更改数组里面的图片数据
      var arr = [];
      fileList.forEach((item) => {
        arr.push(item.raw);
      });
      this.dataList = arr;
      console.log(arr);
      // 隐藏组件
      this.uploadDisabled = "disabled";
    },
    recover() {
      this.uploadDisabled = "";
    },
    uploadID() {
      //提交文件ID+病人ID
      console.log(this.imageID, this.ruleForm.pid);
      axios({
        method: "patch", //请求方法
        data: { person: this.ruleForm.pid },
        url: "/api/diagnose/" + this.imageID + "/",
      }).then((res) => {
        this.$router.push({ name: "result" });
      });
    },
  },
};
</script>

<style>
.content {
  margin-top: 10vh;
  /*height: 60vh;*/
}

.upimg {
  align-items: center;
  width: 100vw;
  margin-top: 20px;
  text-align: center;
}
.upid {
  width: 100vw;
  text-align: center;
  align-items: center;
  margin-top: 40px;
  display: flex;
  justify-content: space-between;
}
/* 居中用 */
.spanright {
  margin-right: 7vw;
}
.upbutton {
  align-items: center;
  width: 100vw;
  margin-top: 30px;
  text-align: center;
}
.disabled .el-upload--picture-card {
  display: none;
}
</style>
