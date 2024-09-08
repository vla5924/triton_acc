#ifndef TRITON_ACC_CONVERSION_PASSES_H
#define TRITON_ACC_CONVERSION_PASSES_H

#include "mlir/Pass/Pass.h"

namespace mlir {
namespace triton_acc {

std::unique_ptr<Pass> createConvertTritonToTritonAccPass();

#define GEN_PASS_REGISTRATION
#include "triton_acc/Conversion/Passes.h.inc"

} // namespace triton_acc
} // namespace mlir

#endif
