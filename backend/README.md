# 后端文档
## 项目初始化

- 后端项目初始化参考：[项目初始化搭建](https://pyloong.github.io/pythonic-project-guidelines/practices/web/#2)
## 项目结构


## 项目启动

安装环境后执行以下命令既可：
```shell
pip install -e .
ai_analytics
```
出现以下提示既可, 打开网站：http://127.0.0.1:8000/docs
```text
INFO:     Started server process [56941]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

```

## 数据迁移
    
创建空白数据库迁移版本：
```shell
ai_analytics migrate -- revision -m "init"
```

执行迁移：
```shell
ai_analytics migrate -- upgrade head

```
创建第一个数据库迁移版本：
```shell
ai_analytics migrate -- revision --autogenerate -m "init_table"
```
执行迁移：
```shell
ai_analytics migrate -- upgrade head
```
