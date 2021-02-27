<template>
    <div class="card">
        <header class="card-header">
            <p class="card-header-title">Novo Questionário</p>
        </header>

        <!-- Questionnaries -->
        <div class="card-content">
            <div class="content">
              <div class="columns">
                  <div class="column">
                      <div class="field">
                        <label class="label has-text-left">Nome do Questionário:</label>
                        <input
                            class="input is-primary"
                            placeholder="Nome do questionário"
                            v-model="name"
                        >
                      </div>
                    <!-- <question-card></question-card> -->
                    <hr>
                    <question-card></question-card>
                  </div>
                </div>
            </div>
        </div>
        <footer class="card-footer">
          <button type="submit" class="card-footer-item button is-black" @click="formSubmitQuestion">Savar</button>
          <router-link to="/" class="card-footer-item button is-dark">
            <button class="card-footer-item button is-dark">Cancelar</button>
          </router-link>
        </footer>
        <!-- Questionary end -->
    </div>
    <!-- CARD LIST end -->
</template>

<script>
import QuestionCard from "./QuestionCard";

const API_BASE_URL = "http://127.0.0.1:8000/api";

export default {
    name: "questionay-view-card",
    components: {
        QuestionCard
    },
    data() {
        return {
          name: "",
          questions: []
        };
    },
    methods: {
      formSubmitQuestion(e) {
      e.preventDefault();
      let currentObj = this;
      console.log(currentObj);

      for (let index = 0; index < this.$children.length; index++) {
        const element = this.$children[index];
        let headQuestion = element.headQuestion;
        let choices = element.alternatives;
        this.questions.push({
          headQuestion,
          choices
        })
        console.log("Data questions: ",this.questions)
      }
      var choices1 = {
        textChoice: window.localStorage.getItem("choice1"),
        score: window.localStorage.getItem("score1")
      }
      var choices2 = {
        textChoice: window.localStorage.getItem("choice2"),
        score: window.localStorage.getItem("score2")
      }
      var choices3 = {
        textChoice: window.localStorage.getItem("choice3"),
        score: window.localStorage.getItem("score3")
      }
      var headQuestion = window.localStorage.getItem("headQuestion")

      var alternatives = this.questions.push(
        choices1,
        choices2,
        choices3
      );

      window.localStorage.setItem("name", this.name)
      this.$axios
        .post(`${API_BASE_URL}/questionnaries/`, {
            name: this.name,
            questions: [{headQuestion, choices: alternatives}],
        })
        .then(response => {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  }
};
</script>

<style>
.card-header-title {
    color: #636368;
}
</style>
