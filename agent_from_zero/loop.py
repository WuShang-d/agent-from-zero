"""The first milestone: a bounded decision loop without tools or model calls."""

from dataclasses import dataclass
from typing import Literal, Protocol, Union


@dataclass(frozen=True)
class Continue:
    message: str


@dataclass(frozen=True)
class Finish:
    answer: str


Decision = Union[Continue, Finish]


@dataclass(frozen=True)
class Step:
    number: int
    decision: Decision


class Decider(Protocol):
    def decide(self, task: str, history: tuple[Step, ...]) -> Decision:
        """Choose whether the loop continues or ends."""


@dataclass(frozen=True)
class RunResult:
    status: Literal["finished", "step_limit"]
    steps: tuple[Step, ...]
    answer: str | None


class Agent:
    def __init__(self, decider: Decider, max_steps: int = 5) -> None:
        if max_steps < 1:
            raise ValueError("max_steps must be at least 1")
        self.decider = decider
        self.max_steps = max_steps

    def run(self, task: str) -> RunResult:
        if not task.strip():
            raise ValueError("task must not be empty")

        steps: list[Step] = []
        for number in range(1, self.max_steps + 1):
            decision = self.decider.decide(task, tuple(steps))
            if not isinstance(decision, (Continue, Finish)):
                raise TypeError("decider must return Continue or Finish")
            steps.append(Step(number, decision))
            if isinstance(decision, Finish):
                return RunResult("finished", tuple(steps), decision.answer)

        return RunResult("step_limit", tuple(steps), None)
