import argparse
import signal
import time

from modules.cpu import CPU
from modules.disk import Disk
from modules.network import Network
from modules.ram import RAM
from util import print_line

DELIMITER = "      "
CONTINUOUS_OUTPUT = None
UPDATE_INTERVAL = None


class MinimalisticSystemMonitor:
    def __init__(self, modules):
        self.modules = modules

    def tick(self):
        for module in self.modules:
            module.tick()

    def current_values(self):
        line = DELIMITER.join(module.as_string for module in self.modules)
        return line


def parse_arguments():
    class Range(object):
        def __init__(self, start, end):
            self.start = start
            self.end = end

        def __eq__(self, other):
            return self.start <= other <= self.end

        def __str__(self):  # for --help
            return '[{0},{1}]'.format(self.start, self.end)

    global CONTINUOUS_OUTPUT
    global UPDATE_INTERVAL
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--continuous", action="store_true",
                        help="do not re-use the same line as output (default: disabled)")
    parser.add_argument("-i", "--interval", type=float, choices=[Range(0.1, 30)], default=1.0,
                        help="update interval in seconds, between 0.1 and 30 (default: 1.0)")
    args = parser.parse_args()
    CONTINUOUS_OUTPUT = args.continuous
    UPDATE_INTERVAL = args.interval


def main():
    signal.signal(signal.SIGINT, lambda *_: exit(1))
    parse_arguments()

    modules = [
        CPU(),
        RAM(),
        Network(),
        Disk(),
    ]
    monitor = MinimalisticSystemMonitor(modules)
    while True:
        monitor.tick()
        print_line(monitor.current_values(), continuous=CONTINUOUS_OUTPUT)
        time.sleep(UPDATE_INTERVAL)


if __name__ == "__main__":
    main()
