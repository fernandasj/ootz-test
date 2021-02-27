import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

import QuestionaryList from "../components/QuestionaryList";
import QuestionaryCard from "../components/QuestionaryCard";

export const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: QuestionaryList
    },
    {
      path: "/questionary",
      component: QuestionaryCard
    }

  ]
});
