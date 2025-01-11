<script setup lang="ts">
import { onMounted } from 'vue'
import { TaskConfigApi } from '@/api/taskConfig'

defineOptions({
  name: 'TaskConfig',
})
onMounted(() => {
  console.log('mounted')
  TaskConfigApi.getTypeTaskList({}).then((res) => {
    console.log(res)
  })
})
</script>

<template>
  <div>test</div>
</template>

<style lang="scss" scoped></style>
