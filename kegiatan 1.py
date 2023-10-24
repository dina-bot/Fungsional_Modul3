def convert_to_minutes(weeks, days, hours, minutes):
    return (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes

def curried_converter(weeks):
    def inner_curried_converter(days):
        def inner_inner_curried_converter(hours):
            def inner_inner_inner_curried_converter(minutes):
                return convert_to_minutes(weeks, days, hours, minutes)
            return inner_inner_inner_curried_converter
        return inner_inner_curried_converter
    return inner_curried_converter

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
outputData = []

for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    result = curried_converter(weeks)(days)(hours)(minutes)
    outputData.append(result)

print(outputData)