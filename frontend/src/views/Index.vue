<template>
  <div class="index">
    <Nav></Nav>
    <div class="content">
      <span class="words">
        <h2>欢迎使用湛影系统</h2>
      </span>
      <br />
      <span class="words">
        <h2>点击进行检测或者查看历史记录</h2>
      </span>
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
};
</script>

<style>
.index {
  height: 100vh;
}
.content {
  height: 80vh;
}
.words {
  width: 100vw;
  height: 20px;
  font-size: 20px;
  text-align: center;
}
</style>
