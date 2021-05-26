<template>
  <div>
    <div class="main">
      <div class="icon">
        <img class="image" src="../assets/logo.png" />
        <div class="wd">湛影--乳腺癌辅助诊断系统</div>
      </div>
      <div class="rout">
        <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" router>
          <el-menu-item index="/">首页</el-menu-item>
          <el-menu-item index="/diagnose">检测</el-menu-item>
          <el-menu-item index="/history">病历记录</el-menu-item>
        </el-menu>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Nav",
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style>
.main {
  height: 80px;
  width: 100vw;
  display: flex;
  background-color: #545c64;
  justify-content: space-between;
  align-items: flex-end;
}
.icon {
  display: flex;
  width: 400px;
  text-align: center;
}
.image {
  height: 77px;
  margin-left: 20px;
}
.rout {
  margin-right: 40px;
}
.wd {
  color: white;
  font-size: 20px;
  align-items: center;
  margin-left: 20px;
  margin-top: 25px;
}
.el-menu.el-menu--horizontal {
  border-bottom: 0;
}
.el-menu-item {
  border: 0;
}
</style>
