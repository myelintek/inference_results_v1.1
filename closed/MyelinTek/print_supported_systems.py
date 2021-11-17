from code.common import system_list

systems = system_list.KnownSystems()

for system in systems.get_all_system_classes():
    print(system.aliases, system.pci_ids, system.arch, system.supported_counts)



