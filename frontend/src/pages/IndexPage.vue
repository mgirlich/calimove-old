<template>
  <q-page class="row items-center justify-evenly">
    <example-component title="Example component" active :todos="todos" :meta="meta"></example-component>
  </q-page>
</template>

<script setup lang="ts">
import axios from 'axios';

import { ref } from 'vue';
import { Todo, Meta } from 'components/models';
import ExampleComponent from 'components/ExampleComponent.vue';

const todos = ref<Todo[]>();

axios.get('https://ps1tsi9sp4.execute-api.eu-west-1.amazonaws.com/calimove/api/todos')
  .then((resp) => {
    todos.value = resp.data;
  })
  .catch((err) => {
    console.log(err);
  })

defineOptions({
  name: 'IndexPage'
});


// const todos = ref<Todo[]>([
//   {
//     id: 1,
//     content: 'ct1'
//   },
//   {
//     id: 2,
//     content: 'ct2'
//   },
//   {
//     id: 3,
//     content: 'ct3'
//   },
//   {
//     id: 4,
//     content: 'ct4'
//   },
//   {
//     id: 5,
//     content: 'ct5'
//   }
// ]);

const meta = ref<Meta>({
  totalCount: 1200
});
</script>
