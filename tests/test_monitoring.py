from agentic_genai.monitoring import Monitor, monitor


def test_monitor_decorator():
    events = Monitor().events
    events.clear()

    @monitor
    def hello():
        return "hi"

    assert hello() == "hi"
    assert events == ["start:hello", "end:hello"]
