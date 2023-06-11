
# harnesess = module.Choose_file.choose_harnesses_in_folder('C://1_disk_D//python//LEPS//Test_harnesses')
# virt = module.Choose_file.choose_Virt('C://1_disk_D//python//LEPS//Virt_X254.csv')
# intern = module.Choose_file.choose_Intern('C://1_disk_D//python//LEPS//Int_X254.csv')


def Harness_to_Internal (i, one_separ_harn, virt, intern, Readed_Int_and_number_of_virt, only_index_virt):
    #Головна змінна вязка і Internal під вязку
    Internal_module = []
    #Змінна для виводу помилок на вязки
    Mistakes_harn = []
    #створюю віртуали під вязку
    virt_harn = []
    for k in virt:
        for j in one_separ_harn:
            if k[1] == j[4] and k[2][:-1] == j[2][:len(k[2])-1]: #Друга умова для визначення однакового типу вязки
                virt_harn.append(k)
    #Відсутні індекси в мастердаті віртуал
    for k in one_separ_harn:
        if k[4] not in only_index_virt:
            Mistakes_harn.append(['No_index_in_virtual_master_data: ' + str(i) + ' ' + str(k[4])])

    #створюю інтернал під вязку
    intern_harn = []
    for k in intern:
        for j in virt_harn:
            if k[2] == j[0] and k[3] == j[2]: #Друга умова для типів вязок
                intern_harn.append(k)
            #створюю додаткові умови для типів зязок (в віртуалі і інтерналі беру за основу менший за довжиною рядок типу вязки
            if len(k[3]) < len(j[2]) and k[3][:-1] == j[2][:len(k[3])-1]:
                intern_harn.append(k)
            if len(k[3]) > len(j[2]) and k[3][:len(j[2])-1] == j[2][:-1]:
                intern_harn.append(k)

    #Визначаю список унікальних груп під вязку
    uniq_group_harn = []
    for k in intern_harn:
        if k[1] not in uniq_group_harn:
            uniq_group_harn.append(k[1])
    #Проходжу циклом по кожній групі під вязку
    for k in uniq_group_harn:
        #Проходжу циклом для відбору окремої групи під вязку
        one_group = []
        for j in intern_harn:
            if k == j[1]:
                one_group.append(j)
        #Роблю масив з інтерналів
        just_inernal_in_one_group = []
        for j in one_group:
            just_inernal_in_one_group.append(j[0])
        # Роблю масив з інтерналів без дублікатів
        internal_and_number_of_virt = []
        for j in just_inernal_in_one_group:
            if j not in internal_and_number_of_virt:
                internal_and_number_of_virt.append(j)
        # Масив з інтерналів під групу і кількості віртуалів під ці інтернали під конкретну вязку
        number_of_internal = []
        for j in internal_and_number_of_virt:
            if j not in number_of_internal:
                number_of_internal_pev = []
                number_of_internal_pev.append(j)
                number_of_internal_pev.append(just_inernal_in_one_group.count(j))
                number_of_internal.append(number_of_internal_pev)
        #Добавляю додаткову перевірку щоб відкинути непотрібні інтернали
        number_of_internal_gen = []
        for j in number_of_internal:
            if j in Readed_Int_and_number_of_virt:
                number_of_internal_gen.append(j)
        # print(number_of_internal_gen)
        # Роблю масив з кількість віртуалів
        number_of_virt = []
        for j in range(len(number_of_internal_gen)):
            number_of_virt.append(number_of_internal_gen[j][1])
        #Вибираю максимальне число віртуалів але добавляю умову, тому що якшо у групі нереалізований віртуал то його відкинули при попередній перевірці і масив пустий
        if len(number_of_virt) > 0:
            max_virt = max(number_of_virt)
            #Вибираю з масиву всі знаяення з більшими віртуалами, зробив так бо LEPS тоже видає якщо у групі виконалось дві умови
            for j in range(len(number_of_internal_gen)):
                if max_virt == number_of_internal_gen[j][1]:
                    Internal_piece = []
                    Internal_piece.append(i)
                    Internal_piece.append(number_of_internal_gen[j][0])
                    Internal_module.append(Internal_piece)
                    #Добавляю вивід якшо заказались два інтернали в помилки
                    if number_of_virt.count(max_virt) > 1:
                        Mistakes_harn.append(['More_than_one_internal_in_one_group: ' + str(i) + ' ' + str(number_of_internal_gen[j][0])])

    #Перевірка на нереалізовані віртуали
    #масив для віртуалів які є у вязці
    realized_virt_in_harn = []
    for k in Internal_module:
        for j in intern:
            if k[1] == j[0]:
                realized_virt_in_harn.append(j[2])
    #вичичляю які віртуали заказались але не виконалась умова і вони не пішли у вязки через інтернали
    for k in virt_harn:
        if k[0] not in realized_virt_in_harn:
            Mistakes_harn.append(['Unrealized_Virtual_module: ' + str(i) + ' ' + str(k[0])])

    return Internal_module, Mistakes_harn



# Harness_to_Internal(harnesess, virt, intern)
# print(Harness_to_Internal(harnesess, virt, intern))
#
# module.read_record_csv.record(Harness_to_Internal(harnesess, virt, intern), 'C://1_disk_D//python//LEPS//new222.csv')
