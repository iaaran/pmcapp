def get_average():
    with open("Files/data.txt", 'r') as file_local:
        data_local = file_local.readlines()

    values = data_local[1:]
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)
