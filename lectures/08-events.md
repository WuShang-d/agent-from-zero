# 第 8 课：终端文字不足以恢复任务

**上一版的失败。** 终端能看到工具执行过程，但退出后没有可靠的结构化状态。即便保存整段屏幕文字，也无法稳定回答“哪个调用已经完成、结果属于哪一个 ID”。

![OpenCode 概念图：多客户端、Agent Profile 与结构化事件](figures/article-09.png)

*图源：[腾讯程序员原文](https://mp.weixin.qq.com/s/kZZac-VBgnQIZeookE9Y8g)。这里只借图说明事件轨迹与界面显示分离；具体实现以阅读时的源码版本为准。*

## 从事件重建状态

给一次运行分配 `session_id`，每次用户输入分配 `turn_id`。定义至少五种事件：`user_submitted`、`model_responded`、`tool_started`、`tool_completed`、`turn_stopped`。每条事件有 schema 版本、单调序号、时间、父 ID 和数据。JSONL 追加文件是合适的第一版；状态由事件投影出来，而不是从 CLI 输出反向猜测。

例如一次读取至少留下 `tool_started(call_id=c1, seq=3)` 与 `tool_completed(call_id=c1, seq=4, status=ok)`。重放器检查 `seq` 连续、ID 对应，才可展示“已完成”。日志末尾若只有 `started`，正确结论是“开始过但结果未知”，不是“读取失败”或“读取成功”。

## 动手实验

1. 跑第 6 课的读文件任务，保存事件；编写 `replay(session_id)`，在不调用模型和工具的前提下重建显示轨迹。
2. 人为截断 JSONL 最后一行；重放器应明确报告尾部损坏，并保留此前完整事件。不要默默把损坏行当作任务成功。
3. 故意交换 `tool_started` 与 `tool_completed` 的序号，确认投影器拒绝非法顺序。UI 可以换样式，但事件语义不能跟着变化。

**验收。** 可以从事件回答“工具是否开始、是否完成、哪条结果对应哪次调用”。本课只做**重放展示**，不声称已经能安全地继续未完成的副作用；第 12 课再处理恢复执行。

**源码阅读。** [OpenCode 仓库](https://github.com/anomalyco/opencode)：选定一个提交或版本，寻找 Session、Message/Part 与事件流怎样关联。记录所见版本，不把原文示意图当作实时架构文档。
