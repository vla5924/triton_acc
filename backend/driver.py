from triton.backends.driver import DriverBase
from triton.backends.compiler import GPUTarget


class AccUtils(object):

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AccUtils, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_device_properties(device):
        return {
            "max_shared_mem": 192 * 1024, "multiprocessor_count": None, "sm_clock_rate": None, "mem_clock_rate": None,
            "mem_bus_width": None
        }

    @staticmethod
    def load_binary(name, kernel_asm, shared, device):
        return (None,  # module
                kernel_asm,  # function
                None,  # n_regs
                None  # n_spills
                )


class AccLauncher(object):

    def __init__(self, src, metadata):
        pass

    def __call__(self, *args, **kwargs):
        self.launch(*args, **kwargs)


class AccDriver(DriverBase):

    def __init__(self):
        super().__init__()
        self.utils = AccUtils()
        self.launcher_cls = AccLauncher
        self.binary_ext = "acccode"

    # Acc driver won't be automatically chosen unless explicitly set through
    # triton.runtime.driver.set_active(AccDriver())
    @staticmethod
    def is_active():
        return False

    def get_device_capability(self):
        return ("acc", 0)

    def get_current_stream(self, device):
        return None

    def get_current_device(self):
        # Acc doesn't have a device to return. Return something.
        return "acc"

    def set_current_device(self, device):
        # Acc doesn't have a device to set
        assert device == "acc"
        return

    def get_current_target(self):
        return GPUTarget("acc", 0, 0)
