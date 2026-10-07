# 第 5 课：工具调用是一份协议

**上一版的失败。** 模型可以写“我会读取 README”，但文件不会被读。直接对自由文本做正则匹配后执行命令，会让解释文字、坏参数甚至恶意内容混成动作。

![工具路由器把结构化调用送给具体实现，再返回结果消息](figures/article-04.png)

*图源：[腾讯程序员原文](https://mp.weixin.qq.com/s/kZZac-VBgnQIZeookE9Y8g)。图列出许多可能的工具；本课只实现无写入的两个。*

## 最小协议

定义 `ToolCall(id, name, arguments)` 与 `ToolResult(id, status, content)`。注册表保存可用工具的名称、参数模式与实现。每次调用先验证名称、字段类型和必填项，再路由到实现；结果按调用 ID 返回。模型输出中的自然语言说明不能直接当作可执行命令。

一次示例轨迹：`ToolCall(id="c1", name="read_file", arguments={"path": "stats.py"})` → 路由器验证目录边界 → 读取成功 → `ToolResult(id="c1", status="ok", content="...")`。若模型又给出 `id="c2", name="read_file", arguments={"path": 42}`，结果应是参数错误，不能自动把数字转成路径或猜测模型意图。

## 动手实验

1. 做一个纯函数 `calculator`（仅允许明确的数字与四则运算参数，不用 `eval`）和一个限定练习目录的只读 `read_file`。这一阶段不给任何写入或 shell 能力。
2. 写三个固定 `ToolCall`：正常读取、未知工具、参数缺失。逐个运行路由器，检查对应的 `ToolResult.id` 与状态。
3. 再给一个 `../../` 路径和一个指向练习目录外部的符号链接；确认读取边界以解析后的路径判断。若做不到可靠限制，就暂时只保留 `calculator`。

**验收。** 错误调用返回结构化错误，进程不执行猜测出的“相近工具”；只读工具无法访问练习目录之外的文件。第 6 课再把结果作为观察送回模型。

**阅读。** [ReAct 论文](https://arxiv.org/abs/2210.03629)展示行动与观察交错；[OpenAI 2023 年 Function Calling 公告](https://openai.com/index/function-calling-and-other-api-updates/)说明结构化工具调用进入 API 的背景。两者是设计线索，不意味着本仓库采用其专有格式。
