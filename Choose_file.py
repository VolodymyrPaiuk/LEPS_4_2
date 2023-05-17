import os
import module.read_record_csv
# path_harn = 'C://1_disk_D//python//LEPS//Test_harnesses'
# path_Virt = 'C://1_disk_D//python//LEPS//Virt_X254.csv'
# path_Intern = 'C://1_disk_D//python//LEPS//Int_X254.csv'
# path_Wirelist = 'C://1_disk_D//python//LEPS//Wirelist.csv'
# path_Wires_in_prod_modules = 'C://1_disk_D//python//LEPS//Wires_in_prod_modules.csv'

def choose_harnesses_in_folder (path_harn):
    harnesses = []
    folder_content = os.listdir(path_harn)
    # print(folder_content)

    for i in folder_content:
        one_file = []
        one_file = module.read_record_csv.read(path_harn + '//' + i)
        # print(one_file)
        while_i = 1
        while while_i < len(one_file):
            harnesses.append(one_file[while_i])
            while_i+=1

    # module.read_record_csv.record(harnesses, 'C://1_disk_D//python//LEPS//Test_harnesses//111.csv')
    return harnesses

def choose_Virt (path_Virt):
    Virt = module.read_record_csv.read(path_Virt)
    # print(Virt)
    return Virt

def choose_Intern(path_Intern):
    Intern = module.read_record_csv.read(path_Intern)
    # print(Intern)
    return Intern
def choose_Wirelist(path_Wirelist):
    Wirelist = module.read_record_csv.read(path_Wirelist)
    # print(Wirelist)
    return Wirelist
def choose_Wires_in_prod_modules(path_Wires_in_prod_modules):
    Wires_in_prod_modules = module.read_record_csv.read(path_Wires_in_prod_modules)
    # print(Wires_in_prod_modules)
    return Wires_in_prod_modules


# choose_Wires_in_prod_modules(path_Wires_in_prod_modules)
# choose_Wirelist(path_Wirelist)
# choose_harnesses_in_folder(path_harn)
# choose_Virt(path_Virt)
# choose_Intern(path_Intern)