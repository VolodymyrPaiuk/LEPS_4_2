import module.Choose_file

# harnesess = module.Choose_file.choose_harnesses_in_folder('C://1_disk_D//python//LEPS//Test_harnesses')
# virt = module.Choose_file.choose_Virt('C://1_disk_D//python//LEPS//Virt_X254.csv')
# intern = module.Choose_file.choose_Intern('C://1_disk_D//python//LEPS//Int_X254.csv')

def Harness_to_Internal (harnesess, virt, intern):
    #Головна змінна вязка і Internal під вязку
    Internal_module = []
    #визначення списку унікальних вязок
    uniq_har = []
    for i in harnesess:
        if i[0] not in uniq_har:
            uniq_har.append(i[0])
    #Роблю список інтернал і кількість віртуалів(умов) під інтернал, щоб в кінці відсіяти умови які виконались але це умови під більші конфігурації
    internal_withaut_harn = []
    internal_withaut_harn_mas = []
    internal_withaut_harn_gen = []
    for i in intern:
        if i[0] not in internal_withaut_harn:
            internal_withaut_harn.append(i[0])
    for i in intern:
        internal_withaut_harn_mas.append(i[0])
    for i in internal_withaut_harn:
        add_in_mass = []
        add_in_mass.append(i)
        add_in_mass.append(internal_withaut_harn_mas.count(i))
        internal_withaut_harn_gen.append(add_in_mass)
    # print(internal_withaut_harn_gen)

    # Проходжу циклом по унікальних вязках
    for i in uniq_har:
        #Проходжу циклом для відбору окремої вязки в масив
        one_separ_harn_prev = []
        for k in harnesess:
            if i == k[0]:
                one_separ_harn_prev.append(k)
        #Видаляю дублікати щоб не було помилки при закиданні однакових вязок
        one_separ_harn = []
        for k in one_separ_harn_prev:
            if k not in one_separ_harn:
                one_separ_harn.append(k)
        #створюю віртуали під вязку
        virt_harn = []
        for k in virt:
            for j in one_separ_harn:
                if k[1] == j[4]:
                    virt_harn.append(k)
        #створюю інтернал під вязку
        intern_harn = []
        for k in intern:
            for j in virt_harn:
                if k[2] == j[0]:
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
                if j in internal_withaut_harn_gen:
                    number_of_internal_gen.append(j)
            # print(number_of_internal_gen)
            # Роблю масив з кількість віртуалів
            number_of_virt = []
            for j in range(len(number_of_internal_gen)):
                number_of_virt.append(number_of_internal_gen[j][1])
            #Вибираю максимальне число віртуалів
            max_virt = max(number_of_virt)
            #Вибираю з масиву всі знаяення з більшими віртуалами, зробив так бо LEPS тоже видає якщо у групі виконалось дві умови
            for j in range(len(number_of_internal_gen)):
                if max_virt == number_of_internal_gen[j][1]:
                    Internal_piece = []
                    Internal_piece.append(i)
                    Internal_piece.append(number_of_internal_gen[j][0])
                    Internal_module.append(Internal_piece)
    return Internal_module


# Harness_to_Internal(harnesess, virt, intern)
# print(Harness_to_Internal(harnesess, virt, intern))
#
# module.read_record_csv.record(Harness_to_Internal(harnesess, virt, intern), 'C://1_disk_D//python//LEPS//new222.csv')
