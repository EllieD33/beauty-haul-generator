import multiprocessing
import time


class Spinner:
    def __init__(self, message="", speed=0.1):
        self.message = message
        self.speed = speed

        self.process = multiprocessing.Process(
            target=self.spin,
            args=(),
            name="Spinner"
        )

    def spin(self):
        spinner = ["✦", "✧", "✩", "✪", "✫", "✬", "✭", "✮", "✯", "✰"]
        n = 0
        while True:
            print(f"\r{spinner[n]} {self.message} ", end="")
            n += 1
            if n >= len(spinner):
                n = 0
            time.sleep(self.speed)

    def start(self):
        self.process.start()

    def stop(self):
        if not self.process.is_alive():
            return
        else:
            self.process.terminate()



if __name__ == "__main__":
    my_spinner  = Spinner("Loading", 0.3)
    my_spinner.start()
    time.sleep(10)
    my_spinner.stop()