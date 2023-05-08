import module.Choose_file
import read_record_csv
import Harness_to_Internal

# harnesess = module.Choose_file.choose_harnesses_in_folder('C://1_disk_D//python//LEPS//Test_harnesses')
# virt = module.Choose_file.choose_Virt('C://1_disk_D//python//LEPS//Virt_X254.csv')
# intern = module.Choose_file.choose_Intern('C://1_disk_D//python//LEPS//Int_X254.csv')
# internal_in_harn = Harness_to_Internal.Harness_to_Internal(harnesess, virt, intern)
# Wires_in_prod_modules = module.Choose_file.choose_Wires_in_prod_modules('C://1_disk_D//python//LEPS//Wires_in_prod_modules.csv')
# Wirelist = module.Choose_file.choose_Wirelist('C://1_disk_D//python//LEPS//Wirelist.csv')

def Check_modularization(internal_in_harn, Wires_in_prod_modules, harnesess, Wirelist):
    #Спочатку дії з harnesess та Wirelist, роблю список вязка - проводи до вязки
    harnesess_wires_by_Wirelist_by_index = []
    # harnesess_wires_by_Wirelist_by_variant = []
    harnesess_wires_by_internal = []
    #визначення списку унікальних вязок
    uniq_har = []
    for i in harnesess:
        if i[0] not in uniq_har:
            uniq_har.append(i[0])
    # Проходжу циклом по унікальних вязках для harnesess_wires_by_index
    for i in uniq_har:
        #Проходжу циклом для відбору окремої вязки в масив
        one_separ_harn = []
        for k in harnesess:
            if i == k[0]:
                one_separ_harn.append(k)
        #Проходжу по вязці перевіряючи кожний індекс
        for k in one_separ_harn:
            #Проходжу циклом по Wirelist
            for j in Wirelist:
                # print(Wirelist)
                if k[4] == j[1]:
                    part_harnesess_wires_by_index = []
                    part_harnesess_wires_by_index.append(i)
                    part_harnesess_wires_by_index.append(j[0])
                    harnesess_wires_by_Wirelist_by_index.append(part_harnesess_wires_by_index)
    # module.read_record_csv.record(harnesess_wires_by_Wirelist_by_index, 'C://1_disk_D//python//LEPS//harnesess_wires_by_Wirelist_by_index.csv')

    # # Проходжу циклом по унікальних вязках для harnesess_wires_by_variant
    # for i in uniq_har:
    #     #Проходжу циклом для відбору окремої вязки в масив
    #     one_separ_harn = []
    #     for k in harnesess:
    #         if i == k[0]:
    #             one_separ_harn.append(k)
    #     #Проходжу по вязці перевіряючи кожний індекс
    #     for k in one_separ_harn:
    #         #Проходжу циклом по Wirelist
    #         for j in Wirelist:
    #             if k[5] == j[3]:
    #                 part_harnesess_wires_by_variant = []
    #                 part_harnesess_wires_by_variant.append(i)
    #                 part_harnesess_wires_by_variant.append(j[0])
    #                 harnesess_wires_by_Wirelist_by_variant.append(part_harnesess_wires_by_variant)
    # # print(harnesess_wires_by_Wirelist_by_variant)

    # Проходжу циклом по унікальних вязках для harnesess_wires_by_internal
    for i in uniq_har:
        #Проходжу циклом для відбору окремої вязки в масив
        one_separ_harn = []
        for k in internal_in_harn:
            if i == k[0]:
                one_separ_harn.append(k)
        #Проходжу по вязці перевіряючи кожний інтернал
        for k in one_separ_harn:
            #Проходжу циклом по Wires_in_prod_modules
            for j in Wires_in_prod_modules:
                if k[1] == j[1]:
                    part_harnesess_wires_by_internal = []
                    part_harnesess_wires_by_internal.append(i)
                    part_harnesess_wires_by_internal.append(j[0])
                    harnesess_wires_by_internal.append(part_harnesess_wires_by_internal)
    # print(harnesess_wires_by_internal)
    # module.read_record_csv.record(harnesess_wires_by_internal, 'C://1_disk_D//python//LEPS//harnesess_wires_by_internal.csv')

    Is_in_wirelist_but_absend_in_internal = [['Is in wirelist but absent in internal:']]
    Is_in_internal_but_absend_in_wirelist = [['Is in internal but absent in wirelist:']]
    #Проходжу циклом по harnesess_wires_by_Wirelist_by_index, якщо не знаходжу значення в harnesess_wires_by_internal то записую в Is_in_wirelist_but_absend_in_internal

    for i in harnesess_wires_by_Wirelist_by_index:
        if i not in harnesess_wires_by_internal:
            Is_in_wirelist_but_absend_in_internal.append(i)
    # print(Is_in_wirelist_but_absend_in_internal)

    for i in harnesess_wires_by_internal:
        if i not in harnesess_wires_by_Wirelist_by_index:
            Is_in_internal_but_absend_in_wirelist.append(i)
    # print(Is_in_internal_but_absend_in_wirelist)

# Check_modularization(internal_in_harn, Wires_in_prod_modules, harnesess, Wirelist)