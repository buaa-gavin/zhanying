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
  {
    path: "/history/:id",
    name: "patient",
    component: () => import("../views/Patient.vue"),
  },
  {
    path: "/result",
    name: "result",
    component: () => import("../views/Result.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
