# 智扫通机器人智能客服系统

## 项目简介

智扫通机器人智能客服系统是一个基于 LangChain 和 LangGraph 构建的智能问答系统，集成了 RAG（检索增强生成）能力，能够为用户提供扫地机器人相关的产品咨询、使用指导和使用报告生成等服务。

## 技术栈

- Python 3.10+

- LangChain / LangGraph - Agent 框架

- Streamlit - Web 界面

- Chroma - 向量数据库

- DashScope (通义千问) - 大语言模型和嵌入模型

- PyPDF / TextLoader - 文档加载

## 项目结构

```text
├── agent/
│   ├── react_agent.py          # ReAct Agent 主逻辑
│   └── tools/
│       ├── agent_tools.py      # Agent 工具定义
│       └── middleware.py       # Agent 中间件（日志、提示词切换）
├── config/
│   ├── agent.yml               # Agent 配置
│   ├── chroma.yml              # 向量数据库配置
│   ├── prompts.yml             # 提示词路径配置
│   └── rag.yml                 # RAG 模型配置
├── data/                       # 知识库原始文件目录
├── logs/                       # 日志文件目录
├── model/
│   └── factory.py              # 模型工厂（Chat/Embedding）
├── rag/
│   ├── rag_service.py          # RAG 总结服务
│   └── vector_store.py         # 向量存储服务
├── utils/
│   ├── config_handler.py       # 配置加载
│   ├── file_handler.py         # 文件处理（MD5、加载器）
│   ├── logger_handler.py       # 日志处理
│   ├── path_tool.py            # 路径工具
│   └── prompt_loader.py        # 提示词加载
├── app.py                      # Streamlit 入口
└── README.md
```

## 功能特性

### 1. 智能问答

- 基于 RAG 的知识检索，从知识库中获取相关参考资料

- 支持多轮对话，上下文理解

### 2. Agent 工具集

|工具名称|描述|
|---|---|
|rag_summarize|从向量存储中检索参考资料并生成回答|
|get_weather|获取指定城市天气|
|get_user_location|获取用户所在城市|
|get_user_id|获取用户 ID|
|get_current_month|获取当前月份|
|fetch_external_data|获取用户使用记录数据|
|fill_context_for_report|为报告生成场景注入上下文|
### 3. 报告生成

- 支持动态提示词切换，当用户请求生成报告时，自动切换为报告生成提示词

- 从外部数据源获取用户使用记录，生成个性化使用报告

### 4. 中间件支持

- 工具调用监控：记录工具调用情况和参数

- 模型调用日志：记录模型调用前的状态

- 动态提示词切换：根据场景切换系统提示词

## 快速开始

### 环境准备

克隆项目

```bash
git clone <repository-url>
cd <project-directory>
```

安装依赖

```bash
pip install -r requirements.txt
```

配置 API Key

在 config/rag.yml 中配置 DashScope API Key：

```yaml
dashscope_api_key: "your-api-key"
chat_model_name: "qwen-plus"
embedding_model_name: "text-embedding-v3"
```

## 配置说明

### config/rag.yml - RAG 模型配置

```yaml
dashscope_api_key: ""           # 通义千问 API Key
chat_model_name: "qwen-plus"    # 对话模型名称
embedding_model_name: "text-embedding-v3"  # 嵌入模型名称
```

### config/chroma.yml - 向量数据库配置

```yaml
collection_name: "knowledge_base"           # 集合名称
persist_directory: "chroma_db"              # 持久化目录
data_path: "data"                           # 知识库文件目录
chunk_size: 500                             # 分块大小
chunk_overlap: 50                           # 分块重叠
k: 5                                        # 检索返回数量
md5_hex_store: "md5_records.txt"            # MD5 记录文件
allow_knowledge_file_type: ["txt", "pdf"]   # 允许的文件类型
separators: ["\n\n", "\n", "。", "！", "？", "；", "，", "、", " "]  # 分块分隔符
```

### config/agent.yml - Agent 配置

```yaml
external_data_path: "data/external_data.csv"  # 外部数据文件路径
```

### config/prompts.yml - 提示词路径配置

```yaml
main_prompt_path: "prompts/system_prompt.txt"        # 主系统提示词
rag_summarize_prompt_path: "prompts/rag_prompt.txt"  # RAG 提示词
report_prompt_path: "prompts/report_prompt.txt"      # 报告生成提示词
```

## 初始化知识库

在运行应用前，需要先将知识库文件加载到向量数据库中：

```bash
python -m rag.vector_store
```

知识库文件应放置在 data/ 目录下，支持 .txt 和 .pdf 格式。

## 启动应用

```bash
streamlit run app.py
```

访问 http://localhost:8501 即可使用智能客服系统。

## 外部数据格式

external_data.csv 文件格式示例：

```csv
user_id,特征,效率,耗材,对比,时间
"1001","高频使用","85%","滤网需更换","提升20%","2025-01"
"1001","中频使用","90%","正常","提升15%","2025-02"
```

## 提示词模板

- 主系统提示词 (prompts/system_prompt.txt)：定义 Agent 的基础行为和能力。

- RAG 提示词 (prompts/rag_prompt.txt)：定义检索增强生成的提示词模板。

- 报告提示词 (prompts/report_prompt.txt)：定义报告生成场景的提示词模板。

## 日志系统

日志文件存储在 logs/ 目录下，按日期命名：

- 控制台输出级别：INFO

- 文件输出级别：DEBUG
> （注：文档部分内容可能由 AI 生成）
