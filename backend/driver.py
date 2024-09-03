from triton.backends.compiler import BaseBackend, GPUTarget


class AccBackend(BaseBackend):
    @staticmethod
    def supports_target(target: GPUTarget):
        return target.backend == "acc"

    def __init__(self, target: GPUTarget) -> None:
        super().__init__(target)
