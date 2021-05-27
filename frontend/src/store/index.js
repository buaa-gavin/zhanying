import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isDone: false,
    originImage: null,
    segImage: null,
    classResult: null,
  },
  mutations: {
    editOrigin(state, data) {
      state.originImage = data;
      console.log(data);
    },
    editImage(state, data) {
      state.segImage = data;
      console.log(data);
    },
    editResult(state, data) {
      state.classResult = data;
      console.log(data);
    },
    editIsDone(state) {
      state.isDone = !state.isDone;
    },
  },
  actions: {},
  modules: {},
});
