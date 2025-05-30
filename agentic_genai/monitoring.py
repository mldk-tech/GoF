class Monitor:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.events = []
        return cls._instance

    def log(self, message: str) -> None:
        self.events.append(message)


def monitor(fn):
    def wrapper(*args, **kwargs):
        monitor_instance = Monitor()
        monitor_instance.log(f"start:{fn.__name__}")
        result = fn(*args, **kwargs)
        monitor_instance.log(f"end:{fn.__name__}")
        return result
    return wrapper
