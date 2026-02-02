import time


def show_time():
    return time.strftime("%d-%m-%Y %H:%M:%S")


def countdown(seconds):
    while seconds > 0:
        print(f"Time Left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Done!")


def sleep_now(seconds):
    time.sleep(seconds)


def execution_time(func):
    start = time.time()
    func()
    end = time.time()
    print("Time Taken:", round(end - start, 4), "seconds")


# ✅ Main Runner Function
def run():
    print("⏱️ MyTimePkg Started\n")

    print("Current Time:")
    print(show_time())

    print("\nCountdown:")
    countdown(5)

    print("\nSleeping for 2 seconds...")
    sleep_now(2)

    print("\nChecking Execution Time...")

    def demo():
        for i in range(1000000):
            pass

    execution_time(demo)

    print("\n✅ MyTimePkg Finished")
