# 第 1 课：从空文件写出一次对话

这一课不读现成的 Agent 代码，也不写 `Agent` 类。你只要在仓库根目录**自己创建** `main.py`，让它做一件事：收一条用户输入，发给本地模型，打印回答，然后退出。它是后面所有版本的最小基线。

如果把“Agent”宽泛地理解为接收输入、作出响应的代理，这就是 **V0 对话 Agent**。它还没有自主行动、会话记忆或工具；这些不是第一天必须具备的。我们先把一条真实数据流跑通，再由实际缺口决定下一步加什么。

![问题送入模型，返回一条回答](figures/article-01.png)

*图源：[腾讯程序员原文](https://mp.weixin.qq.com/s/kZZac-VBgnQIZeookE9Y8g)。今天只实现图中的一次请求。*

## 先理解这一次发生了什么

终端里的 `input()` 负责收文字；你写的 Python 程序负责组织请求并调用 Ollama；模型只负责根据收到的消息生成回复；程序再把回复显示出来。**模型不知道你的磁盘上有哪些文件，也不会自动记住下一次运行。** 这个版本还没有连续对话、工具或任务循环。

Ollama 的本地 Chat API 是 `POST http://localhost:11434/api/chat`。本课请求只需要模型名、一个 `user` 消息和 `stream: false`；响应的文字在 `message.content`。`stream: false` 让服务返回一份完整 JSON，便于第一次理解数据流。[接口字段见官方文档](https://docs.ollama.com/api/chat)。

下面是**请求形状**，把 `你的模型标签` 换成 `ollama list` 中的一项；这还不是让你复制的完整 Python 程序：

```json
{
  "model": "你的模型标签",
  "messages": [{"role": "user", "content": "你好"}],
  "stream": false
}
```

响应还会带耗时、用量等字段；本课只取 `message.content`。你可以先在纸上标出：“你好”从哪个字段出去，回答从哪个字段回来。

例如响应中的相关部分可能是 `{"message": {"role": "assistant", "content": "你好！"}, "done": true}`。这是为了说明字段位置，实际响应还有其他字段；不要靠模型回答的具体措辞判断程序是否写对。

```text
你输入一句话
    ↓
main.py 构造 messages=[{role: user, content: 你的话}]
    ↓
Ollama → 本地模型 → 一份 JSON 响应
    ↓
main.py 取出 message.content 并打印
```

## 开始前

在终端运行 `python3 --version` 和 `ollama list`。从列表选一个已下载的模型标签，先用 `ollama run 模型标签` 手动聊一句，确认模型本身能回答，再退出 Ollama 对话。讲义不会强制使用 Qwen、Gemma 或其他特定模型。Ollama 应用需要正在运行。若列表为空，先按[官方模型页](https://ollama.com/search)下载你选定的本地模型。这里调用的是本机服务，不需要付费 API key。

## 亲手写 `main.py`

1. 先只写 `question = input("你：")` 并把它打印出来，确认终端输入没问题。
2. 用 Python 标准库的 `json` 和 `urllib.request` 构造一次 POST：地址是上面的本地接口；请求体包含 `model`、`messages`、`stream`，并设置 `Content-Type: application/json`。可以先把请求体打印出来，确认 `messages` 只有当前这一句。
3. 读取 HTTP 响应并解析 JSON；打印 `message.content`。不要把整份 JSON 当作回答展示。
4. 把问题改成“请用一句话介绍你自己”，重新运行程序。再运行一次问“我刚才问了什么？”——预测它为什么答不出来或只能猜。

卡住时按数据流逐段检查：终端收到了什么？发出的 JSON 是什么？HTTP 是否连上？返回 JSON 里是否有 `message` 和 `content`？不用先设计复杂框架。

## 完成标准

- 运行 `python3 main.py`，输入一条问题，可以看到本地模型的文字回答。
- 每次运行只发送一条 `user` 消息。第二次启动程序时不会带着第一次的历史。
- 能指出哪一行发起模型调用、哪一行提取回答；能解释为什么此时“模型说要查文件”不会真的读取文件。

**留给下一课的缺口：** 想接着说第二句话，就得重新启动程序。第 2 课先解决“连续聊天”，再研究“聊天为什么记得过去”。
