from dataclasses import dataclass
from typing import Dict
from types import ModuleType
import functools

from triton.backends.compiler import BaseBackend, GPUTarget


@dataclass(frozen=True)
class AccOptions:

    def __post_init__(self):
        pass


class AccBackend(BaseBackend):

    @staticmethod
    def supports_target(target: GPUTarget):
        return target.backend == "acc"

    def __init__(self, target: GPUTarget) -> None:
        super().__init__(target)

    @functools.lru_cache()
    def hash(self) -> str:
        """Returns a unique identifier for this backend"""
        return self.target

    def parse_options(self, options: dict) -> object:
        """
        Converts an `options` dictionary into an arbitrary object and returns it.
        This function may contain target-specific heuristics and check the legality of the provided options
        """
        return AccOptions()

    def get_codegen_implementation(self):
        codegen_fns = {"min_dot_size": lambda lhsType, rhsType: (1, 1, 1)}
        return codegen_fns

    def pack_metadata(self, metadata):
        # Note: We actually don't need any of these except for the name which is
        # used in the launch function in driver.py. Putting these in so we're
        # consistent with other backends
        return (metadata.num_warps, metadata.num_ctas, metadata.shared, metadata.cluster_dims[0],
                metadata.cluster_dims[1], metadata.cluster_dims[2], metadata.name)

    def add_stages(self, stages: dict, options: object) -> None:
        """
        Populates `stages` dictionary with entries of the form:
        ir_name [str] => Function[(src: str, metadata: dict) -> str|bytes]
        The value of each entry may populate a `metadata` dictionary.
        Stages will be run sequentially (in inseriton order) and can communicate using `metadata`.
        All stages are expected to return a `str` object, except for the last stage which returns
        a `bytes` object for execution by the launcher.
        """
        pass

    def load_dialects(self, context):
        """
        Load additional MLIR dialects into the provided `context`
        """
        pass

    def get_module_map(self) -> Dict[str, ModuleType]:
        """
        Return a map of interface modules to their device-specific implementations.
        """
        return dict()
