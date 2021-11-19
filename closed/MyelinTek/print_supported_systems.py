from code.common import system_list

systems = system_list.KnownSystems()

for system in systems.get_all_system_classes():
    print(str(system.aliases)+';', str(system.pci_ids)+';', '['+str(system.arch)+'];', str(system.supported_counts))



