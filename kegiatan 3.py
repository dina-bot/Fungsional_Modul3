random_list = [3.1, 5, 'Hello', 1, 0.27, 'Python', 'world', 7.37, 42, 'AI']

# Filter untuk memisahkan nilai float, int, dan string
data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_dict(num):
    if num < 10:
        return {'ratusan': 0, 'puluhan': 0, 'satuan': num}
    elif num < 100:
        puluhan = num // 10
        satuan = num % 10
        return {'ratusan': 0, 'puluhan': puluhan, 'satuan': satuan}
    else:
        ratusan = num // 100
        puluhan = (num % 100) // 10
        satuan = num % 10
        return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

data_int_mapped = list(map(map_int_to_dict, data_int))

# Output
print("Data Float : ")
print(data_float)
print("Data Int : ")
for item in data_int_mapped:
    print(item)
print("Data String : ")
print(data_string)