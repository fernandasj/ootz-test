<template>
    <div class="card">
        <header class="card-header">
            <p class="control is-expanded card-header-title has-text-centered">Questionários</p>
            <p class="control">
                <router-link to="/questionary" class="button is-small is-black add-button"
                style="margin:15px; border-radius: 50%;">
                  <span class="icon is-small">
                      <i class="fa fa-plus"></i>
                  </span>
                </router-link>
            </p>
        </header>

        <!-- Questionnaries -->
        <div class="card-content">
            <div class="content">
                <div class="row">
                  <div class="columns">
                    <div class="column is-half">
                      <div class="field is-grouped">
                        <p class="control is-expanded has-text-primary-dark has-background-primary-light">Nome do Questionário</p>
                      </div>
                    </div>
                    <div class="column is-one-quarter">
                      <div class="field is-grouped">
                        <p class="control is-expanded has-text-primary-dark has-background-primary-light">Questões</p>
                      </div>
                    </div>
                    <div class="column is-one-quarter">
                      <div class="field is-grouped">
                        <p class="control is-expanded has-text-primary-dark has-background-primary-light">Ações</p>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="row">
                    <div class="columns">
                        <div class="column">
                          <div class="field is-grouped" v-for="questionary in questionnaries">
                                <p class="control">
                                    <a class="button is-dark is-small">
                                        <span class="icon is-small">
                                            <i class="fa fa-info"></i>
                                        </span>
                                    </a>
                                </p>
                                <p class="controls">{{ questionary.name }}</p>
                                <p class="control is-expanded">{{ questionary.questions.length }}</p>

                                <p class="control">
                                    <a
                                        class="button is-info is-small"
                                        style=" border-radius: 50%;"
                                        @click="editQuestionary(questionary.idQuestionary)"
                                    >
                                        <span class="icon is-small">
                                            <i class="fa fa-reply"></i>
                                        </span>
                                    </a>
                                </p>
                                <p class="control">
                                    <a
                                        class="button is-danger is-small"
                                        style=" border-radius: 50%;"
                                        @click="deleteQuestionary(questionary.idQuestionary)"
                                    >
                                        <span class="icon is-small">
                                            <i class="fa fa-trash"></i>
                                        </span>
                                    </a>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Questionnaries end -->
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
            questionnaries: null,
            questionaryEdit: null,
        };
    },
    mounted() {
        this.getQuestionnaries();
    },
    methods: {
        getQuestionnaries() {
            this.$axios
                .get(`${API_BASE_URL}/questionnaries/`)
                .then(response => {
                    console.log(response);
                    this.questionnaries = response.data.results;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        deleteQuestionary(id) {
            this.$axios
                .delete(`${API_BASE_URL}/questionnaries/${id}`)
                .then(response => {
                    this.questionnaries.splice(id, 1);
                })
                .catch(error => {
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
