import pandas

FILE = 'hw.csv'


def avg_by_pandas(data_file=FILE):
    df = pandas.read_csv(data_file, sep=',')
    return df.mean(axis=0)


def avg_height_weight(data_file=FILE):
    with open(data_file) as file:
        text = file.read()
    strings = text.split('\n')
    height = 0
    weight = 0
    count = 0
    for s in strings[1:]:
        if s:
            s = s.split(',')
            height += float(s[1])
            weight += float(s[2])
            count += 1
    return {"avg_height": height / count, "avg_weight": weight / count}


if __name__ == '__main__':
    print(avg_height_weight())
