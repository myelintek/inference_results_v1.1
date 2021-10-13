# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
sys.path.insert(0, os.getcwd())

from code.common.constants import Benchmark
from configs.configuration import BenchmarkConfiguration


class GPUBaseConfig(BenchmarkConfiguration):
    benchmark = Benchmark.UNET3D

    map_path = "data_maps/brats/val_map.txt"
    tensor_path = "${PREPROCESSED_DATA_DIR}/brats/brats_npy/int8_cdhw32"
    precision = "int8"
    input_dtype = "int8"
    input_format = "cdhw32"
    use_graphs = False


class CPUBaseConfig(BenchmarkConfiguration):
    benchmark = Benchmark.UNET3D

    map_path = "data_maps/brats/val_map.txt"
    tensor_path = "${PREPROCESSED_DATA_DIR}/brats/brats_npy/fp32"
    precision = "fp32"
    input_dtype = "fp32"
    use_triton = True
