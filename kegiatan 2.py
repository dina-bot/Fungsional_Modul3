data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
integer_values = []

for item in data:
    parts = item.split()
    # Menggunakan filter dan isdigit() untuk mendapatkan nilai integer
    integer_values.append(list(filter(str.isdigit, parts)))

for item in integer_values:
    print(item)