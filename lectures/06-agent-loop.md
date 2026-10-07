# 第 6 课：模型、动作、观察，组成真正的循环

**上一版的失败。** 第 5 课能执行单次工具调用，但程序执行完就停止。模型既看不到结果，也不能据结果决定下一步。第 1 课已有 `Agent.run()`，现在要把它从“演示决策器的循环”改造成“模型请求与工具观察的循环”。

![ReAct 示意：行动结果回到下一轮工作上下文](figures/article-03.png)

*图源：[腾讯程序员原文](https://mp.weixin.qq.com/s/kZZac-VBgnQIZeookE9Y8g)。图中的 Thought 是概念标签；实现不要求展示或保存模型私有推理。*

## 状态转移

每一轮先由 `ContextBuilder` 生成请求，模型返回 `final` 或一个/多个结构化 `tool_call`。收到调用时，运行时验证、执行、把 `ToolResult` 作为观察加入本轮上下文，再开始下一轮。收到 `final` 才返回答案。`max_steps` 限制**模型决策轮数**，`max_time` 限制整个运行时间；两个上限都要返回明确停止原因。

```text
user task → build context → model
                         ├─ final ─────────────→ finished
                         └─ tool call → validate → execute → observation ┐
                                      ↑────────────────────────────────────┘
```

## 动手实验

1. 用 `FakeModel` 排定两次响应：第一次调用 `read_file`，第二次回答文件中的第一行。检查第二次收到的请求确实包含与调用 ID 对应的工具结果。
2. 再让假模型永远请求工具；确认步数上限停止，并且停止后不再执行新工具。一次响应有多个工具时，第一版顺序执行并记录顺序。
3. 对照现有 `Continue/Finish`：决定是扩展这个决策类型，还是用新的 `ModelResponse` 替换它。修改测试，明确旧演示入口是否仍仅作教学演示。

**验收。** 一份真实轨迹中能数出两次模型调用、一次工具执行、一次观察和一次最终回答。最终回答引用工具结果不等于事实正确，但证明了数据通路已闭合。

**阅读。** [ReAct](https://arxiv.org/abs/2210.03629) 与 [Anthropic《Building effective agents》](https://www.anthropic.com/engineering/building-effective-agents)。
