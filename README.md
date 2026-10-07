> 课程主线参考腾讯程序员文章[《从一次 LLM 调用到完整 Harness，Agent 到底经历了什么？》](https://mp.weixin.qq.com/s/kZZac-VBgnQIZeookE9Y8g)（ivanxxie、davoszhang）。课程文字与练习为本仓库重新编写；所用原文配图逐张标注来源。

# agent-from-zero

亲手从零写一个 Agent 的学习仓库。前一阶段在 [llm-from-zero](https://github.com/WuShang-d/llm-from-zero) 中完成了从分词、预训练到对话 SFT 的实验；结果与限制见其 [README](https://github.com/WuShang-d/llm-from-zero#readme) 和 [RESULTS.md](https://github.com/WuShang-d/llm-from-zero/blob/main/RESULTS.md)。其中手搓模型的回答能力不足，**不作为本项目的实际推理后端**。

学习路径：单轮对话 → 多轮对话循环 → 状态与上下文 → 本地工具 → 模型工具调用 → Agent 运行循环 → 错误、权限、记忆、MCP 与评测。长期目标是探索类似 Claude Code 的编码 Agent。

从 [lectures 课程目录](lectures/README.md)进入。讲义给出问题、动手步骤和验收方法；Agent 的实现由学习者逐课亲手写入仓库，不预置完整实现。图示及后续课程目标**不代表仓库当前已有这些功能**。

## 当前状态：从空白开始

仓库当前没有 Agent 运行代码。第 1 课将从空文件写出连接本地模型的单轮终端对话；第 2 课再加入多轮对话循环。模型可通过本机 Ollama 提供，具体标签可替换，课程不依赖付费 API。

开始前需要 Python 3.10+、正在运行的 Ollama 和一个已下载的本地对话模型。先在自己的终端确认：

```bash
python3 --version
ollama list
```

然后阅读[第 1 课](lectures/01-first-chat.md)，按步骤创建自己的第一个 Python 文件。Ollama 的 [Chat API](https://docs.ollama.com/api/chat) 在本机提供消息接口；模型标签由你在练习时选择。

## 目录

```text
lectures/          # 分课讲义、原文配图与后期练习项目
README.md
```
