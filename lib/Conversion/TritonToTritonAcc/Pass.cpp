#include "triton_acc/Conversion/Passes.h"

#include "mlir/Dialect/Func/IR/FuncOps.h"
#include "mlir/IR/BuiltinOps.h"

using namespace mlir;
using namespace mlir::triton_acc;

namespace {

#define GEN_PASS_DEF_CONVERTTRITONTOTRITONACC
#include "triton_acc/Conversion/Passes.h.inc"

class ConvertTritonToTritonAcc
    : public impl::ConvertTritonToTritonAccBase<ConvertTritonToTritonAcc> {
public:
  ConvertTritonToTritonAcc() = default;

  void runOnOperation() override{}
};

} // namespace

std::unique_ptr<Pass> mlir::triton_acc::createConvertTritonToTritonAccPass() {
  return std::make_unique<ConvertTritonToTritonAcc>();
}
