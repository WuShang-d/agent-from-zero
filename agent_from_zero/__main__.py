"""Run a deterministic demonstration of the loop."""

import argparse

from .loop import Agent, Continue, Finish, Step


class DemoDecider:
    def decide(self, task: str, history: tuple[Step, ...]) -> Continue | Finish:
        if not history:
            return Continue(f"已记录演示任务：{task}")
        return Finish("循环演示结束；任务未被实际执行。")


def main() -> None:
    parser = argparse.ArgumentParser(description="运行不执行任务的最小 Agent 循环演示")
    parser.add_argument("task", help="仅用于演示记录的任务文本")
    args = parser.parse_args()

    result = Agent(DemoDecider()).run(args.task)
    for step in result.steps:
        decision = step.decision
        kind = "continue" if isinstance(decision, Continue) else "finish"
        message = decision.message if isinstance(decision, Continue) else decision.answer
        print(f"{step.number}. {kind}: {message}")
    print(f"status: {result.status}")


if __name__ == "__main__":
    main()
