# triton_acc

## Installation

```bash
export TRITON_PLUGIN_DIRS=$(pwd)/triton_acc
git clone --recurse-submodules https://github.com/ML-acc/triton_acc.git triton_acc
cd triton_acc/triton/python

# Install prerequisites
python3 -m pip install --upgrade pip
python3 -m pip install cmake ninja wheel pybind11
sudo apt-get update -y
sudo apt-get install -y ccache clang lld

TRITON_BUILD_WITH_CLANG_LLD=true TRITON_BUILD_WITH_CCACHE=true python3 -m pip install --no-build-isolation -vvv '.[tests]'
# or
python3 -m pip install -e .
```
