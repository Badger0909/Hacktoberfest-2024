import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False
        self.laps = []

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            print("Stopwatch started.")

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            print(f"Stopwatch stopped. Elapsed time: {self.format_time(self.elapsed_time)}")

    def lap(self):
        if self.running:
            lap_time = time.time() - self.start_time
            self.laps.append(lap_time)
            print(f"Lap {len(self.laps)}: {self.format_time(lap_time)}")

    def restart(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.laps = []
        self.running = False
        print("Stopwatch restarted.")

    def get_elapsed_time(self):
        if self.running:
            return time.time() - self.start_time
        return self.elapsed_time

    @staticmethod
    def format_time(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:06.3f}"

# Example usage
if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.start()
    time.sleep(1)  # Simulate time passing
    stopwatch.lap()
    time.sleep(2)  # Simulate time passing
    stopwatch.lap()
    stopwatch.stop()
    stopwatch.restart()
