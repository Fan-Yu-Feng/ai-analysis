<template>
  <Dialog :title="dialogTitle" v-model="dialogVisible">
    <el-form
      ref="formRef"
      :model="formData"
      :rules="formRules"
      label-width="100px"
      v-loading="formLoading"
    >
      <el-form-item label="评论配置表 id" prop="promptConfigId">
        <el-input v-model="formData.promptConfigId" placeholder="请输入评论配置表 id" />
      </el-form-item>
      <el-form-item label="任务状态：待处理、处理中、已完成、失败" prop="status">
        <el-radio-group v-model="formData.status">
          <el-radio label="1">请选择字典生成</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="任务优先级，数值越大优先级越高" prop="priority">
        <el-input v-model="formData.priority" placeholder="请输入任务优先级，数值越大优先级越高" />
      </el-form-item>
      <el-form-item label="配置明细" prop="configDetail">
        <el-input v-model="formData.configDetail" placeholder="请输入配置明细" />
      </el-form-item>
      <el-form-item label="错误信息，如果任务失败则记录错误信息" prop="errorMessage">
        <el-input
          v-model="formData.errorMessage"
          placeholder="请输入错误信息，如果任务失败则记录错误信息"
        />
      </el-form-item>
      <el-form-item label="创建者" prop="createBy">
        <el-input v-model="formData.createBy" placeholder="请输入创建者" />
      </el-form-item>
      <el-form-item label="修改者" prop="updateBy">
        <el-input v-model="formData.updateBy" placeholder="请输入修改者" />
      </el-form-item>
      <el-form-item label="任务类型：评论分析、舆情分析，等等" prop="taskType">
        <el-select
          v-model="formData.taskType"
          placeholder="请选择任务类型：评论分析、舆情分析，等等"
        >
          <el-option label="请选择字典生成" value="" />
        </el-select>
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="submitForm" type="primary" :disabled="formLoading">确 定</el-button>
      <el-button @click="dialogVisible = false">取 消</el-button>
    </template>
  </Dialog>
</template>
<script setup lang="ts">
import { TaskConfigApi, ConfigVO } from '@/api/taskConfig'

/** 任务配置 表单 */
defineOptions({ name: 'ConfigForm' })

const { t } = useI18n() // 国际化
const message = useMessage() // 消息弹窗

const dialogVisible = ref(false) // 弹窗的是否展示
const dialogTitle = ref('') // 弹窗的标题
const formLoading = ref(false) // 表单的加载中：1）修改时的数据加载；2）提交的按钮禁用
const formType = ref('') // 表单的类型：create - 新增；update - 修改
const formData = ref({
  id: undefined,
  promptConfigId: undefined,
  status: undefined,
  priority: undefined,
  configDetail: undefined,
  errorMessage: undefined,
  createBy: undefined,
  updateBy: undefined,
  taskType: undefined,
})
const formRules = reactive({
  promptConfigId: [{ required: true, message: '评论配置表 id不能为空', trigger: 'blur' }],
  status: [
    { required: true, message: '任务状态：待处理、处理中、已完成、失败不能为空', trigger: 'blur' },
  ],
  taskType: [
    { required: true, message: '任务类型：评论分析、舆情分析，等等不能为空', trigger: 'change' },
  ],
})
const formRef = ref() // 表单 Ref

/** 打开弹窗 */
const open = async (type: string, id?: number) => {
  dialogVisible.value = true
  dialogTitle.value = t('action.' + type)
  formType.value = type
  resetForm()
  // 修改时，设置数据
  if (id) {
    formLoading.value = true
    try {
      formData.value = await TaskConfigApi.getById(id)
    } finally {
      formLoading.value = false
    }
  }
}
defineExpose({ open }) // 提供 open 方法，用于打开弹窗

/** 提交表单 */
const emit = defineEmits(['success']) // 定义 success 事件，用于操作成功后的回调
const submitForm = async () => {
  // 校验表单
  await formRef.value.validate()
  // 提交请求
  formLoading.value = true
  try {
    const data = formData.value as unknown as ConfigVO
    if (formType.value === 'create') {
      await TaskConfigApi.add(data)
      message.success(t('common.createSuccess'))
    } else {
      await TaskConfigApi.updateById(data)
      message.success(t('common.updateSuccess'))
    }
    dialogVisible.value = false
    // 发送操作成功的事件
    emit('success')
  } finally {
    formLoading.value = false
  }
}

/** 重置表单 */
const resetForm = () => {
  formData.value = {
    id: undefined,
    promptConfigId: undefined,
    status: undefined,
    priority: undefined,
    configDetail: undefined,
    errorMessage: undefined,
    createBy: undefined,
    updateBy: undefined,
    taskType: undefined,
  }
  formRef.value?.resetFields()
}
</script>
