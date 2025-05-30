from functools import wraps


class Monitor:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message: str) -> None:
        self.logs.append(message)


monitor = Monitor()


def monitor_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        monitor.log(f"call:{func.__name__}")
        return func(*args, **kwargs)

    return wrapper
