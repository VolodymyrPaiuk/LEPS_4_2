def Check_modular(i, one_separ_harn_intern, wires_in_prod_mod, one_separ_harn_index, Wirelist):
    #Створюю масив для помилок
    Rez_mis = []

    #Визначаю проводи під вязку по one_separ_harn_intern та wires_in_prod_mod
    #Створюю масив з проводами
    wires_in_har_prod = []
    for k in wires_in_prod_mod:
        if k[1] in one_separ_harn_intern:
            wires_in_har_prod.append(k[0])
    #Добавляю перевірку якщо заказались два однакові проводи
    for k in wires_in_har_prod:
        if wires_in_har_prod.count(k) > 1:
            Rez_mis.append(['Duplicate_of_wires_in_internal: ' + str(i) + ' ' + str(k) + ' ' + str(wires_in_har_prod.count(k))])

    #Визначаю проводи під вязку по harnes та Wirelist
    #Створюю масив з проводами
    wires_in_har_Wirelist = []
    for k in Wirelist:
        if k[1] in one_separ_harn_index:
            wires_in_har_Wirelist.append(k[0])
    # Добавляю перевірку якщо заказались два однакові проводи
    for k in wires_in_har_Wirelist:
        if wires_in_har_Wirelist.count(k) > 1:
            Rez_mis.append(['Duplicate_of_wires_in_Wirelist: ' + str(i) + ' ' + str(k) + ' ' + str(wires_in_har_Wirelist.count(k))])

    #Порівнюю чи є всі проводи у Internal
    for k in wires_in_har_Wirelist:
        if k not in wires_in_har_prod:
            Rez_mis.append(['Is_in_Wirelist_absent_in_Internal: ' + str(i) + ' ' + str(k)])

    #Порівнюю чи є всі проводи у Wirelist
    for k in wires_in_har_prod:
        if k not in wires_in_har_Wirelist:
            Rez_mis.append(['Is_in_Internal_absent_in_Wirelist: ' + str(i) + ' ' + str(k)])

    return Rez_mis





