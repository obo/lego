# How to Cross-Compile for EV3DEV Running Stretch?

More details: https://www.acmesystems.it/arm9_toolchain

Get the tools:

```bash
sudo apt-get install libc6-armel-cross libc6-dev-armel-cross
sudo apt-get install binutils-arm-linux-gnueabi binutils-arm-linux-gnueabi
sudo apt-get install libncurses5-dev
sudo apt-get install gcc-arm-linux-gnueabi g++-arm-linux-gnueabi
```

Compile hello-world:

```bash
arm-linux-gnueabi-gcc hello.c -o hello
```

Copy to robot and run. This hello world app worked!
