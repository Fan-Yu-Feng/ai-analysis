<template>
  <ContentWrap>
    <!-- 搜索工作栏 -->
    <el-form
      ref="queryFormRef"
      class="-mb-15px"
      :model="queryParams"
      :inline="true"
      label-width="68px"
    >
      <el-form-item label="id" prop="promptConfigId">
        <el-input
          v-model="queryParams.promptConfigId"
          placeholder="请输入评论配置表 id"
          clearable
          class="!w-240px"
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
          <el-option label="请选择字典生成" value="" />
        </el-select>
      </el-form-item>
      <el-form-item label="配置明细" prop="configDetail">
        <el-input
          v-model="queryParams.configDetail"
          placeholder="请输入配置明细"
          clearable
          class="!w-240px"
          @keyup.enter="handleQuery"
        />
      </el-form-item>
      <el-form-item label="任务类型" prop="taskType">
        <el-select
          v-model="queryParams.taskType"
          placeholder="请选择任务类型：评论分析、舆情分析，等等"
          clearable
          class="!w-240px"
        >
          <el-option label="请选择字典生成" value="" />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button @click="handleQuery"><Icon icon="ep:search" class="mr-5px" /> 搜索</el-button>
        <el-button @click="resetQuery"><Icon icon="ep:refresh" class="mr-5px" /> 重置</el-button>
        <el-button
          v-hasPermi="['task:config:create']"
          type="primary"
          plain
          @click="openForm('create')"
        >
          <Icon icon="ep:plus" class="mr-5px" /> 新增
        </el-button>
      </el-form-item>
    </el-form>
  </ContentWrap>

  <!-- 列表 -->
  <ContentWrap>
    <el-table v-loading="loading" :data="list" :stripe="true" :show-overflow-tooltip="true">
      <el-table-column label="id" align="center" prop="promptConfigId" />
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
          <el-button
            v-hasPermi="['task:config:update']"
            link
            type="primary"
            @click="openForm('update', scope.row.id)"
          >
            编辑
          </el-button>
          <el-button
            v-hasPermi="['task:config:delete']"
            link
            type="danger"
            @click="handleDelete(scope.row.id)"
          >
            删除
          </el-button>
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
import download from '@/utils/download'
import { ConfigVO, TaskConfigApi } from '@/api/taskConfig'
import ConfigForm from './ConfigForm.vue'

/** 任务配置 列表 */
defineOptions({ name: 'Config' })

const message = useMessage() // 消息弹窗
const { t } = useI18n() // 国际化

const loading = ref(true) // 列表的加载中
const list = ref<ConfigVO[]>([]) // 列表的数据
const total = ref(0) // 列表的总页数
const queryParams = reactive({
  pageNo: 1,
  pageSize: 10,
  promptConfigId: undefined,
  status: undefined,
  priority: undefined,
  configDetail: undefined,
  errorMessage: undefined,
  createBy: undefined,
  updateBy: undefined,
  createTime: [],
  taskType: undefined,
})
const queryFormRef = ref() // 搜索的表单
const exportLoading = ref(false) // 导出的加载中

/** 查询列表 */
const getList = async () => {
  loading.value = true
  try {
    const data = await TaskConfigApi.getTypeTaskPage({})
    list.value = data.list
    total.value = data.total
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
