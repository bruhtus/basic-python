import csv

with open('./weight-height.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') #reader method to read csv file.
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are: {", ".join(row)}')
            line_count += 1

        else:
            print(f'\t The gender is {row[0]}. The height is {row[1]} and the weight is {row[2]}.')
            line_count += 1

    print(f'Number of lines: {line_count}')
