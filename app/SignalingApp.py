import signal
import time


# Our signal handler
def signal_handler(signum, frame):
    print("Signal Number:", signum, " Frame: ", frame)


# call signal handler every 2 seconds with a SIGALRM signal
signal.signal(signal.SIGINT, signal_handler)

# While Loop
while 1:
    signal.raise_signal(2)
    time.sleep(3)