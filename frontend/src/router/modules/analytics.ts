const TaskConfig = () => import('@/views/analytics/TaskConfig/index.vue')

export default {
  path: '/analytics',
  name: 'Analytics',
  // component: Layout,
  redirect: '/analytics/task-config',
  meta: {
    // icon: 'ep:home-filled',
    title: '分析',
    rank: 0,
  },
  children: [
    {
      path: '/task-config',
      name: 'TaskConfig',
      component: TaskConfig,
      meta: {
        title: '任务配置',
      },
    },
    {
      // 分析结果
      path: '/result',
      name: 'Result',
      component: () => import('@/views/analytics/Result/index.vue'),
      meta: {
        title: '分析结果',
        showLink: true,
      },
    },
  ],
} satisfies RouteConfigsTable
