<template>
  <div>
    <Nav></Nav>
    <div class="content">
      <div class="his_head">
        <h3>病历检测记录</h3>
      </div>
      <div class="patient_list">
        <el-table :data="info" style="width: 100%">
          <el-table-column label="检测时间" width="300">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 10px">{{ scope.row.date }}</span>
            </template>
          </el-table-column>

          <el-table-column label="病人ID" width="100">
            <template slot-scope="scope">
              <i class="el-icon-circle-check"></i>
              <span style="margin-left: 10px">{{ scope.row.id }}</span>
            </template>
          </el-table-column>

          <el-table-column label="病人姓名" width="100">
            <template slot-scope="scope">
              <i class="el-icon-user"></i>
              <span style="margin-left: 10px">{{ scope.row.name }}</span>
            </template>
          </el-table-column>

          <el-table-column label="查看" style="margin-left: 20px">
            <template slot-scope="scope">
              <el-button size="mini" @click="skip(scope.row.id)" type="primary">详情</el-button>
            </template>
          </el-table-column>
        </el-table>
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
  created() {
    window.it = this;
  },
  components: {
    Nav,
    Footer,
  },
  data() {
    return {
      info: null,
    };
  },
  mounted() {
    axios.get("/api/InfoList/").then((response) => (this.info = response.data));
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    skip(id) {
      this.$router.push({ name: "patient", params: { id: id } });
    },
  },
};
</script>

<style>
.content {
  height: 70vh;
}
.his_head {
  height: 10vh;
  width: 100vw;
  text-align: left;
  margin-left: 11vw;
  font-size: 25px;
}
.patient_list {
  margin-left: 10vw;
}
</style>
