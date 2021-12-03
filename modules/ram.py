import psutil

from modules.monitoring_module import MonitoringModule
from util import adaptive_precision


to_GiB = 1024*1024*1024


class RAM(MonitoringModule):
    def __init__(self):
        self.ram_data = None

    def tick(self):
        self.ram_data = psutil.virtual_memory()

    @property
    def as_string(self):
        current = adaptive_precision(self.ram_data.used/to_GiB, target_width=4, max_decimal_places=2)
        total = adaptive_precision(self.ram_data.total/to_GiB, target_width=2, max_decimal_places=1)
        percentage = f"{self.ram_data.percent:4.1f}%"
        return f"RAM [GiB]: {current}/{total} ({percentage})"
