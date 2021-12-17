#!/bin/bash

FAST=$1
BENCHMARKS="${@:2}"

if $FAST == 1
    then make run RUN_ARGS="--benchmarks=$BENCHMARKS --scenarios=offline --fast";
    else make run RUN_ARGS="--benchmarks=$BENCHMARKS --scenarios=offline";
fi

