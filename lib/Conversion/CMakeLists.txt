add_triton_library(TritonAccConversion
    TritonToTritonAcc/Pass.cpp

    DEPENDS
    TritonAccConversionPassIncGen

    LINK_LIBS PUBLIC
    MLIRIR
    MLIRPass
    MLIRTransforms
    TritonIR
)
