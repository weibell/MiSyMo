import time
import psutil

from modules.monitoring_module import MonitoringModule
from util import adaptive_precision

to_MBps = 1000*1000


class Disk(MonitoringModule):
    def __init__(self):
        disk_data = psutil.disk_io_counters()
        self.old_time = time.perf_counter()
        self.old_read_bytes = disk_data.read_bytes
        self.old_write_bytes = disk_data.write_bytes

        self.throughput_read = None
        self.throughput_write = None

    def tick(self):
        disk_data = psutil.disk_io_counters()
        current_time = time.perf_counter()
        current_read_bytes = disk_data.read_bytes
        current_write_bytes = disk_data.write_bytes

        elapsed_seconds = current_time - self.old_time
        self.throughput_read = (current_read_bytes - self.old_read_bytes) / elapsed_seconds
        self.throughput_write = (current_write_bytes - self.old_write_bytes) / elapsed_seconds

        self.old_time = current_time
        self.old_read_bytes = current_read_bytes
        self.old_write_bytes = current_write_bytes

    @property
    def as_string(self):
        read = adaptive_precision(self.throughput_read/to_MBps, target_width=3, max_decimal_places=1)
        write = adaptive_precision(self.throughput_write/to_MBps, target_width=3, max_decimal_places=1)
        return f"Disk [MB/s]: {read} r/w {write}"
