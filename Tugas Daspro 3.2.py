def lists_to_dict(keys, values):
    # Pastikan panjang kedua list sama
    if len(keys) != len(values):
        raise ValueError("Panjang list kunci dan nilai harus sama")

    # Buat kamus kosong
    result_dict = {}

    # Gabungkan kunci dan nilai menjadi kamus
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]

    return result_dict

# Contoh data list
keys_list = ['nama', 'umur', 'kota']
values_list = ['Ivan', 20, 'Tidore']

# Buat kamus dari list
result_dict = lists_to_dict(keys_list, values_list)

# Cetak kamus hasil
print(result_dict)
