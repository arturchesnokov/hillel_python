import pandas

FILE = 'hw.csv'


# TODO: доделать вывод только нужных стобцов
def avg_by_pandas(data_file=FILE) -> str:
    df = pandas.read_csv(data_file, sep=',')
    print(df.columns)
    df.columns = ['index', 'height', 'weight']
    print(df['height'].mean())
    return str(df.mean(axis=0))


def avg_height_weight(data_file=FILE) -> dict:
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
    print(avg_by_pandas())
