##
# @file build.py
#
# @brief Builds the Hello World program.


# --------------------------------------------------------------------------------------------------
#  Imports
# --------------------------------------------------------------------------------------------------


import os
import subprocess


# --------------------------------------------------------------------------------------------------
# Global Constants
# --------------------------------------------------------------------------------------------------


ASM_FILES = ["startup"]
C_FILES = ["helloWorld"]
LINKER_FILE = "linker.ld"

TOOLCHAIN_DIR = "C:\\SysGCC\\arm-eabi\\arm-none-eabi\\bin\\" # https://gnutoolchains.com/download/
COMPILER_DIR = "C:\\SysGCC\\arm-eabi\\bin\\"

BIN_NAME = "helloWorld"


# --------------------------------------------------------------------------------------------------
# Class/Functions
# --------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------
# Script
# --------------------------------------------------------------------------------------------------

asmInFiles = " ".join([str + ".s" for str in ASM_FILES])
asmOutFiles = " ".join([str + ".o" for str in ASM_FILES])
cInFiles = " ".join([str + ".c" for str in C_FILES])
cOutFiles = " ".join([str + ".o" for str in C_FILES])

linkerInFiles = asmOutFiles + " " + cOutFiles
linkerOutFile = BIN_NAME + ".elf"

binFile = BIN_NAME + ".bin"

subprocess.check_output(f"{TOOLCHAIN_DIR}as.exe -mcpu=arm926ej-s -g {asmInFiles} -o {asmOutFiles}", shell=True)
subprocess.check_output(f"{COMPILER_DIR}arm-none-eabi-gcc.exe -c -mcpu=arm926ej-s -g {cInFiles} -o {cOutFiles}", shell=True)
subprocess.check_output(f"{TOOLCHAIN_DIR}ld.exe -T {LINKER_FILE} {linkerInFiles} -o {linkerOutFile}", shell=True)
subprocess.check_output(f"{TOOLCHAIN_DIR}objcopy.exe -O binary {linkerOutFile} {binFile}", shell=True)

subprocess.check_output("del *.o *.elf", shell=True)

subprocess.run(f"\"C:\\Program Files\\qemu\\qemu-system-arm.exe\" -M versatilepb -m 128M -nographic -kernel {BIN_NAME}.bin", shell=True)
