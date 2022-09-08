def summary_stats(data):

    mean = median = std = 0 # default initialization

    # calculating sum and sorted
    sum_total = sum(data)
    data = sorted(data)

    # calculating mean
    mean = sum_total / len(data)

    # calculating median (offset by -1, since indexing starts from 0)
    median = 0
    if len(data) % 2 == 0:
        median = (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
    else:
        median = data[(len(data) + 1) // 2 - 1]
    # calculating standard deviation
    new_data = []
    for val in data:
        new_data.append((val-mean) ** 2)
    std = (sum(new_data) / (len(data))) ** 0.5

    return mean, median, std
