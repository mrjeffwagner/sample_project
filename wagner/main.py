from datetime import datetime


def report(msg: str):
    _time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-6]
    print(f"{_time}: {msg}")
