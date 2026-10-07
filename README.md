> 课程主线参考腾讯程序员文章[《从一次 LLM 调用到完整 Harness，Agent 到底经历了什么？》](https://mp.weixin.qq.com/s/kZZac-VBgnQIZeookE9Y8g)（ivanxxie、davoszhang）。课程文字与练习为本仓库重新编写；所用原文配图逐张标注来源。

# agent-from-zero

从最小 Agent 循环开始学习编码 Agent 的独立项目。前一阶段在 [llm-from-zero](https://github.com/WuShang-d/llm-from-zero) 中完成了从分词、预训练到对话 SFT 的实验；结果与限制见其 [README](https://github.com/WuShang-d/llm-from-zero#readme) 和 [RESULTS.md](https://github.com/WuShang-d/llm-from-zero/blob/main/RESULTS.md)。其中手搓模型的回答能力不足，**不作为本项目的实际推理后端**。

学习路径：Agent 循环 → 工具调用 → 状态与上下文管理 → 错误处理 → 权限控制 → 任务评测；长期探索类似 Claude Code 的编码 Agent。每一步以可运行代码和可验证行为推进。

完整学习材料见 [lectures 课程目录](lectures/README.md)。课程文档描述后续要亲手完成的实验，**不代表对应功能已在代码中实现**。

## 当前里程碑：最小循环

现有代码只有决策、记录、结束三个环节，以及最大步数限制。`DemoDecider` 是确定性的演示决策器，用来验证循环控制流程；它不使用模型，不调用工具，也不执行输入任务。后续接入实际推理后端时可替换 `Decider`，但需要单独实现和验证。

需要 Python 3.10+，无第三方依赖。在仓库根目录运行：

```bash
python3 -m agent_from_zero "查看项目结构"
python3 -m unittest discover -s tests -v
```

第一个命令展示两次决策及最终状态 `finished`。传入的任务只用于演示记录，不会访问文件或执行命令。

## 目录

```text
agent_from_zero/   # 最小循环、决策接口和演示入口
tests/             # 循环结束与步数上限的测试
lectures/          # 15 课讲义与原文配图
README.md
```
