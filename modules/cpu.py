import psutil

from modules.monitoring_module import MonitoringModule
from util import adaptive_precision


class CPU(MonitoringModule):
    def __init__(self):
        self.cpu_usage = None

    def tick(self):
        self.cpu_usage = psutil.cpu_percent()

    @property
    def as_string(self):
        cpu_usage = adaptive_precision(self.cpu_usage, target_width=4, max_decimal_places=1)
        return f"CPU: {cpu_usage}%"
