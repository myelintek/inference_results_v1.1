from code.common import system_list

systems = system_list.KnownSystems()

for system in systems.get_all_system_classes():
    if not system.pci_ids:
        system.pci_ids = ""
    print(system.aliases, "+", system.pci_ids, "+", system.arch, "+", system.supported_counts)



