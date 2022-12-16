import csv

def data_entry_txt(introduction_txt):
    with open("Phone_number.txt", "a") as file:
        for  line in introduction_txt:
            file.write(line + '\t')
        file.write('\n')


def data_output_txt():
    with open('Phone_number.txt', 'r') as file:
        read_file = file.read()
    return read_file


def data_entry_csv(introduction_txt):
    with open('Phone_number.csv', 'a') as f:
        writer = csv.writer(f, delimiter = "-", lineterminator="\r")
        writer.writerow(introduction_txt)
    return


# def data_output_csv():
#     with open("Phone_number.csv", encoding='utf-8') as r_file:
#         lst = []
#         reader_object = csv.reader(r_file, delimiter="-")
#         for row in reader_object:
#             lst.append(row)
#         print(*lst, end='\n')


def data_output_csv():
    with open("Phone_number.csv", encoding='utf-8') as r_file:
        lst = []
        reader_object = csv.reader(r_file, delimiter="-")
        for row in reader_object:
            lst.append(row)
        for i in lst:
            print(*i,'\n',end='')
