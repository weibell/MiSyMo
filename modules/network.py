import time
import psutil

from modules.monitoring_module import MonitoringModule
from util import adaptive_precision

to_Mbps = 1000*1000//8


class Network(MonitoringModule):
    def __init__(self):
        network_data = psutil.net_io_counters()
        self.old_time = time.perf_counter()
        self.old_bytes_sent = network_data.bytes_sent
        self.old_bytes_recv = network_data.bytes_recv

        self.throughput_sent = None
        self.throughput_recv = None

    def tick(self):
        network_data = psutil.net_io_counters()
        current_time = time.perf_counter()
        current_bytes_sent = network_data.bytes_sent
        current_bytes_recv = network_data.bytes_recv

        elapsed_seconds = current_time - self.old_time
        self.throughput_sent = (current_bytes_sent - self.old_bytes_sent) / elapsed_seconds
        self.throughput_recv = (current_bytes_recv - self.old_bytes_recv) / elapsed_seconds

        self.old_time = current_time
        self.old_bytes_sent = current_bytes_sent
        self.old_bytes_recv = current_bytes_recv

    @property
    def as_string(self):
        up = adaptive_precision(self.throughput_sent/to_Mbps, target_width=3, max_decimal_places=1)
        down = adaptive_precision(self.throughput_recv/to_Mbps, target_width=3, max_decimal_places=1)
        return f"Net [MBit/s]: {up} ↑/↓ {down}"
