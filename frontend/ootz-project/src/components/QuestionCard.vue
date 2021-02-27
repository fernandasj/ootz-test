<template>
    <div class="field">
        <p class="control field is-expanded has-text-left">
          <label class="label has-text-left">Cabeçalho da Questão:</label>
          <textarea
              class="textarea is-primary"
              rows="3"
              placeholder="Cabeçalho da questão"
              v-model="headQuestion"
              @change="onChange"
          ></textarea>
        </p>
        <p class="control field is-expanded has-text-left">
            <label class="label">Alternativa 1</label>
            <input
                v-model="choice1"
                class="input is-primary"
                placeholder="Alternativa 1"
                @change="onChange"
            />
        </p>
        <p class="control field is-expanded has-text-left">
            <label class="label">Score 1</label>
            <input
                v-model="score1"
                type="number"
                class="input is-primary"
                placeholder="Score 1"
                @change="onChange"
            />
        </p>
        <hr>
        <p class="control field is-expanded has-text-left">
            <label class="label">Alternativa 2</label>
            <input
                v-model="choice2"
                class="input is-primary"
                placeholder="Alternativa 2"
                @change="onChange"
            />
        </p>
        <p class="control field is-expanded has-text-left">
            <label class="label">Score 2</label>
            <input
                v-model="score2"
                type="number"
                class="input is-primary"
                placeholder="Score 2"
                @change="onChange"
            />
        </p>
        <hr>
        <p class="control field is-expanded has-text-left">
            <label class="label">Alternativa 3</label>
            <input
                v-model="choice3"
                class="input is-primary"
                placeholder="Alternativa 3"
                @change="onChange"
            />
        </p>
        <p class="control field is-expanded has-text-left">
            <label class="label">Score 3</label>
            <input
                v-model="score3"
                type="number"
                class="input is-primary"
                placeholder="Score 3"
                @change="onChange"
            />
        </p>
    </div>
</template>
<script>

const API_BASE_URL = "http://127.0.0.1:8000/api";

export default {
    name: "question-card",
    data() {
        return {
            headQuestion: "",
            choice1: null,
            score1: null,
            choice2: null,
            score2: null,
            choice3: null,
            score3: null,
            alternatives: [],
        };
    },
    // props:{
    //   textChoice: "",
    //   score: 0,
    //   headQuestion: ""
    // },
    methods: {
        onChange() {
            var choices1 = {textChoice: this.choice1, score: this.score1}
            var choices2 = {textChoice: this.choice2, score: this.score2}
            var choices3 = {textChoice: this.choice3, score: this.score3}
            var alternatives = this.alternatives.push(
              choices1,
              choices2,
              choices3
            );

            window.localStorage.setItem("headQuestion", headQuestion)
            window.localStorage.setItem("choice1", this.choice1)
            window.localStorage.setItem("choice2", this.choice2)
            window.localStorage.setItem("choice3", this.choice3)
            window.localStorage.setItem("score1", this.score1)
            window.localStorage.setItem("score2", this.score2)
            window.localStorage.setItem("score3", this.score3)

            window.localStorage.setItem("alternatives", alternatives)
            console.log("altenatives: ", alternatives);
            console.log("alternative ...", ...alternatives);
            var headQuestion = this.headQuestion;
            this.$store.dispatch("questionDataAction", {
                alternatives,
                headQuestion
            });

        },
    }
};
</script>
<style>
</style>
