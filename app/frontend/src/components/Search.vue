<template>
    <div>
      <input 
        type="text" 
        v-model="searchTerm" 
        placeholder="Buscar operadoras" 
        @input="search"
      >
      <ul v-if="operadoras.length > 0">
        <li v-for="operadora in operadoras" :key="operadora.id">
          {{ operadora.nome_fantasia || operadora.razao_social }}
        </li>
      </ul>
      <p v-else-if="operadoras.length === 0 && searchTerm.length > 0">
        Nenhum resultado para "{{ searchTerm }}"
      </p>
      <p v-else-if="operadoras.length === 0">
        Nenhuma operadora cadastrada.
      </p>
    </div>
  </template>
  <script>
  import api from "@/services/api.js";
  
  export default {
    data() {
      return {
        searchTerm: "",
        operadoras: [],
      };
    },
    methods: {
      async fetchOperadoras(query = null) {
        try {
          const response = await api.get("/operadoras/search/", {
            params: {
              query: query,
              skip: 0,
              limit: 10,
            },
          });
          this.operadoras = response.data.results;
        } catch (error) {
          if (error.response?.status === 404) {
            this.operadoras = [];
          } else {
            console.error("Erro ao buscar operadoras", error);
          }
        }
      },
      async search() {
        if (this.searchTerm.length === 0) {
          await this.fetchOperadoras();
        } else if (this.searchTerm.length > 2) {
          await this.fetchOperadoras(this.searchTerm);
        }
      },
    },
    mounted() {
      this.fetchOperadoras();
    },
  };
  </script>