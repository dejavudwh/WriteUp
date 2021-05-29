#!/bin/sh

#   close canary                      stack layout randomization
gcc -fno-stack-protector -z execstack -no-pie -g -o ret2stack ret2stack.c
