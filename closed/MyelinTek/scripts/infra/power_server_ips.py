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

__doc__ = """Script used to store, retrieve, and check connectivity to the IP addresses of Power Meter servers."""

import argparse
import os
import subprocess
import sys

POWER_SERVER_IP_MAP = {
    "computelab-ro-prod-01": "10.33.74.149",  # Resource: 2f9be888-4945-40d7-b72f-caf06a4b993d
    "altra-g242-p31-01": "10.33.74.149",  # Resource: 2f9be888-4945-40d7-b72f-caf06a4b993d
    "ipp1-1469": "10.33.73.223",  # Resource: 3df91161-65dd-47cb-9867-fcbe71c249d3
    "sjc1-luna-02": "10.33.74.154",  # Resource: aeb9c187-8a01-48db-a347-42ca7b0e807b
    "computelab-310": "10.33.74.156",  # Resource: c5d3bb68-4f0b-4bfb-ac95-bf37b54eb6d6
    "computelab-501": "10.117.6.91",  # Resource: 91b00cba-f082-4ee1-a74e-4bc9a541674a
    "computelab-502": "10.33.74.181",  # Resource: 34e58317-4e50-42ff-bb8d-724c6cd7f012
}


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sut_hostname",
        help="Hostname of the SUT that power is measured for"
    )
    parser.add_argument(
        "--check_connectivity",
        help="Check connectivity status and SSH login validity, instead of printing the IP address.",
        action="store_true"
    )
    return parser.parse_args()


def check_connectivity(ip_addr):
    ssh_command = f"ping -c 1 {ip_addr}"
    return subprocess.call(ssh_command, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, shell=True)


if __name__ == "__main__":
    args = get_args()
    if args.sut_hostname not in POWER_SERVER_IP_MAP:
        sys.exit(1)

    ip_addr = POWER_SERVER_IP_MAP[args.sut_hostname]
    if args.check_connectivity:
        sys.exit(check_connectivity(ip_addr))
    else:
        print(ip_addr)
