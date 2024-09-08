#ifndef TRITON_ACC_CONVERSION_PASSES
#define TRITON_ACC_CONVERSION_PASSES

include "mlir/Pass/PassBase.td"

def ConvertTritonToTritonAcc: Pass<"convert-triton-to-tritonacc", "ModuleOp"> {
    let summary = "Convert Triton to TritonAcc";
    let description = [{
      ...
    }];
    let constructor = "mlir::triton_acc::createConvertTritonToTritonAccPass()";

    let dependentDialects = ["func::FuncDialect"];
}

#endif // TRITON_ACC_CONVERSION_PASSES
