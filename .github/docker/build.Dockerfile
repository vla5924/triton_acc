# This image shall be used for building Triton packages in CI environment
# Canonical URL: ghcr.io/ML-acc/triton_acc/build:latest

FROM quay.io/pypa/manylinux_2_28_x86_64

RUN dnf update \
    && dnf install -y clang lld \
    && dnf clean all

RUN mkdir /root/ccache \
    && cd /root/ccache \
    && curl -Lo cc.tar.xz https://github.com/ccache/ccache/releases/download/v4.10.2/ccache-4.10.2-linux-x86_64.tar.xz \
    && tar xf cc.tar.xz \
    && cd ccache* \
    && make install \
    && rm -r /root/ccache
