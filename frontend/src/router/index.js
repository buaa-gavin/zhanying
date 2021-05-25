import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: () => import("../views/Index.vue"),
  },
  {
    path: "/diagnose",
    component: () => import("../views/Diagnose.vue"),
  },
  {
    path: "/history",
    component: () => import("../views/History.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
