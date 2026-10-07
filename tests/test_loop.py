import unittest

from agent_from_zero import Agent, Continue, Finish


class SequenceDecider:
    def __init__(self, decisions):
        self.decisions = iter(decisions)
        self.histories = []

    def decide(self, task, history):
        self.histories.append(history)
        return next(self.decisions)


class AgentTests(unittest.TestCase):
    def test_finish_preserves_history_and_answer(self):
        decider = SequenceDecider([Continue("first"), Finish("done")])
        result = Agent(decider).run("example")
        self.assertEqual(result.status, "finished")
        self.assertEqual(result.answer, "done")
        self.assertEqual([step.number for step in result.steps], [1, 2])
        self.assertEqual(len(decider.histories[0]), 0)
        self.assertEqual(decider.histories[1], result.steps[:1])

    def test_step_limit_stops_continuing_decider(self):
        decider = SequenceDecider([Continue("one"), Continue("two")])
        result = Agent(decider, max_steps=2).run("example")
        self.assertEqual(result.status, "step_limit")
        self.assertIsNone(result.answer)
        self.assertEqual(len(result.steps), 2)

    def test_rejects_invalid_inputs(self):
        with self.assertRaises(ValueError):
            Agent(SequenceDecider([]), max_steps=0)
        with self.assertRaises(ValueError):
            Agent(SequenceDecider([])).run("  ")


if __name__ == "__main__":
    unittest.main()
