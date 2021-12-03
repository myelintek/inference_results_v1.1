from configs.configuration import ConfigRegistry
import subprocess
from code.common import get_system
from code.common.constants import (
        Benchmark, 
        Scenario,
        HarnessType,
        AccuracyTarget,
        PowerSetting,
        WorkloadSetting,
        G_DEFAULT_HARNESS_TYPES,
        )
from typing import List

#systems = system_list.KnownSystems()
#print(get_system())
system = get_system()
print(system)
supported_benchmarks = ["ssd-mobilenet", "bert", "ssd-resnet34", "resnet50"]
supported_scenarios = ["offline"]
#supported_benchmarks = List[Benchmark]
#supported_scenarios = List[Scenario]
benchmarks = []
for benchmark_name in supported_benchmarks:
    benchmark = Benchmark.get_match(benchmark_name)
    if benchmark is None:
        raise RuntimeError(f"'{benchmark_name}' is not a valid benchmark name.")
    benchmarks.append(benchmark)

scenarios = []
for scenario_name in supported_scenarios:
    scenario = Scenario.get_match(scenario_name)
    if scenario is None:
        raise RuntimeError(f"'{scenario_name}' is not  valid scenario name.")
    scenarios.append(scenario)

#main_args = parse_main_args()

for benchmark in benchmarks:
    for scenario in scenarios:
        ConfigRegistry.load_configs(benchmark, scenario)
        workload_settings = ConfigRegistry.available_workload_settings(benchmark, scenario)
        #print(workload_settings)
        if workload_settings is None:
            continue
        # Build the workload_setting.
        #harness_type_str = main_args["harness_type"]

        #if harness_type_str == "auto":
        harness_type = G_DEFAULT_HARNESS_TYPES[benchmark]
        #else:
        #    harness_type = HarnessType.get_match(harness_type_str)
        
        default_workload = WorkloadSetting(
            harness_type=harness_type,
            accuracy_target=AccuracyTarget.k_99,
            power_setting=PowerSetting.MaxP)
        workload_settings = [default_workload]
        
       # print(workload_settings)
        #workload_settings = ConfigRegistry.available_workload_settings(benchmark, scenario)
        for workload_setting in workload_settings:
            #print(benchmark, scenario, system, workload_setting)
            #print(workload_setting)
            config = ConfigRegistry.get(benchmark, scenario, system, **workload_setting.as_dict())
            if config is None:
                print(f"No registered config for {benchmark.value.name}.{scenario.value.name}.{system} "
                        f"for WorkloadSetting({workload_setting})")
                continue
            config_dict = config.as_dict()
            config_dict['benchmark'] = config_dict['benchmark'].name
            config_dict['system'] = str(config_dict['system'])
            config_dict['scenario']=config_dict['scenario'].name
            config_string = ""
            for key, value in config_dict.items():
                config_string = config_string + f"{key} : {value}\n"
            print(f"{config_string};")
            
        
    





