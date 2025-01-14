<template>
  <ContentWrap>
    <!-- 搜索工作栏 -->
    <el-form
      ref="queryFormRef"
      class="-mb-15px"
      :model="queryParams"
      :inline="true"
      label-width="70px"
    >
      <el-form-item label="prompt配置" prop="promptConfigId">
        <el-input
          v-model="queryParams.promptConfigId"
          placeholder="请输入评论配置表 ID"
          clearable
          class="!w-250px"
          @keyup.enter="handleQuery"
        />
      </el-form-item>
      <el-form-item label="任务状态" prop="status">
        <el-select
          v-model="queryParams.status"
          placeholder="请选择任务状态：待处理、处理中、已完成、失败"
          clearable
          class="!w-240px"
        >
          <el-option
            v-for="item in taskStatusList"
            :key="item.code"
            :label="item.msg"
            :value="item.code"
          />
        </el-select>
      </el-form-item>

      <el-form-item label="任务类型" prop="taskType">
        <el-select
          v-model="queryParams.taskType"
          placeholder="请选择任务类型：评论分析、舆情分析，等等"
          clearable
          class="!w-240px"
        >
          <el-option
            v-for="item in taskTypeList"
            :key="item.code"
            :label="item.msg"
            :value="item.code"
          />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button @click="handleQuery"><Icon icon="ep:search" class="mr-5px" /> 搜索</el-button>
        <el-button @click="resetQuery"><Icon icon="ep:refresh" class="mr-5px" /> 重置</el-button>
        <el-button type="primary" plain @click="openForm('create')">
          <Icon icon="ep:plus" class="mr-5px" /> 新增
        </el-button>
      </el-form-item>
    </el-form>
  </ContentWrap>

  <!-- 列表 -->
  <ContentWrap>
    <el-table v-loading="loading" :data="list" :stripe="true" :show-overflow-tooltip="true">
      <el-table-column label="ID" align="center" prop="promptConfigId" />
      <el-table-column label="任务状态" align="center" prop="status" />
      <el-table-column label="优先级" align="center" prop="priority" />
      <el-table-column label="配置明细" align="center" prop="configDetail" />
      <el-table-column label="错误信息" align="center" prop="errorMessage" />
      <el-table-column label="创建者" align="center" prop="createBy" />
      <el-table-column label="修改者" align="center" prop="updateBy" />
      <el-table-column
        label="创建时间"
        align="center"
        prop="createTime"
        :formatter="dateFormatter"
        width="180px"
      />
      <el-table-column label="任务类型" align="center" prop="taskType" />
      <el-table-column label="操作" align="center">
        <template #default="scope">
          <el-button link type="primary" @click="openForm('update', scope.row.id)">
            编辑
          </el-button>
          <el-button link type="danger" @click="handleDelete(scope.row.id)"> 删除 </el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 分页 -->
    <Pagination
      v-model:page="queryParams.pageNo"
      v-model:limit="queryParams.pageSize"
      :total="total"
      @pagination="getList"
    />
  </ContentWrap>

  <!-- 表单弹窗：添加/修改 -->
  <ConfigForm ref="formRef" @success="getList" />
</template>

<script setup lang="ts">
import { dateFormatter } from '@/utils/formatTime'
import { TaskConfigVO, TaskConfigApi, TaskConfigReqParams } from '@/api/taskConfig'
import ConfigForm from './ConfigForm.vue'
import { EnumItem, EnumName, EnumsApi } from '@/api/enums'

/** 任务配置 列表 */
defineOptions({ name: 'Config' })

const message = useMessage() // 消息弹窗
const { t } = useI18n() // 国际化

const loading = ref(true) // 列表的加载中
const list = ref<TaskConfigVO[]>([]) // 列表的数据
const total = ref(0) // 列表的总页数
const queryParams = reactive<TaskConfigReqParams>({
  pageNo: 1,
  pageSize: 10,
  promptConfigId: undefined,
  status: undefined,
  priority: undefined,
  configDetail: undefined,
  errorMessage: undefined,
  createBy: undefined, // 创建者
  updateBy: undefined, // 修改者
  taskType: undefined,
})
const queryFormRef = ref() // 搜索的表单
const taskStatusList = ref<EnumItem[]>([])
const taskTypeList = ref<EnumItem[]>([])
/** 查询列表 */
const getList = async () => {
  loading.value = true
  try {
    debugger
    const data = await TaskConfigApi.getTypeTaskPage(queryParams)
    // TODO 分页接口还没写，后面在补充
    taskStatusList.value = await EnumsApi.getTaskStatusEnum()
    taskTypeList.value = await EnumsApi.getTaskTypeEnum()
    console.log('taskStatusList', taskStatusList.value)
    list.value = data.data
    // list.value = data.list
    // total.value = data.total
  } finally {
    loading.value = false
  }
}

/** 搜索按钮操作 */
const handleQuery = () => {
  queryParams.pageNo = 1
  getList()
}

/** 重置按钮操作 */
const resetQuery = () => {
  queryFormRef.value.resetFields()
  handleQuery()
}

/** 添加/修改操作 */
const formRef = ref()
const openForm = (type: string, id?: number) => {
  formRef.value.open(type, id)
}

/** 删除按钮操作 */
const handleDelete = async (id: number) => {
  try {
    // 删除的二次确认
    await message.delConfirm()
    // 发起删除
    await TaskConfigApi.delete(id)
    message.success(t('common.delSuccess'))
    // 刷新列表
    await getList()
  } catch {}
}

/** 初始化 **/
onMounted(() => {
  getList()
})
</script>
