import time

def wait(ms):
    start = int(round(time.time() * 1000))
    now = int(round(time.time() * 1000))
    while now <= start + ms:
        now = int(round(time.time() * 1000))
    print(f"Waited: {abs(start-now)} Target: {ms}ms ")
    return (now - start)
    