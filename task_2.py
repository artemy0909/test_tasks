import re
import os


def uppercase_inside_lowercase(line: str):
    i = 0
    result = []
    while i < len(line) - 2:
        if line[i].islower():
            y = i + 1
            while y < len(line) and line[y].isupper():
                y += 1
                if y < len(line) and line[y].islower():
                    result.append((line[i], line[y]))
        i += 1
    return result


def find_inside_uppercase(line: str):
    i = 0
    result = []
    while i < len(line) - 5:
        if line[i].isupper() and line[i+1:i+3].islower() and line[i+3:i+6].isupper():
            result.append((line[i], line[i+5]))
        i += 1
    return result


def list_to_str(tuple_list):
    string = f"'{tuple_list[0][0]}{tuple_list[0][1]}'"
    for e in tuple_list[1:]:
        string += f", '{e[0]}{e[1]}'"
    return string


if __name__ == '__main__':
    try:
        with open("task_2_line") as f_obj:
            LINE = f_obj.read()
    except OSError:
        print("Невозможно загрузить ключевую строку")
        quit(1)

    re_find = re.findall(r"([a-z])[A-Z]+([a-z])", LINE)
    print(f"1. с помощью re \t{list_to_str(re_find)}")
    print(f"1. без помощи re \t{list_to_str(uppercase_inside_lowercase(LINE))}")

    re_find = re.findall(r"([A-Z])[a-z]{2}[A-Z]{2}([A-Z])", LINE)
    print(f"2. с помощью re \t{list_to_str(re_find)}")
    print(f"2. без помощи re \t{list_to_str(find_inside_uppercase(LINE))}")

    dir_name = "task_2_files"
    if not os.path.exists(f"{dir_name}/"):
        os.mkdir(dir_name)
    for n in range(1, 6):
        with open(f"{dir_name}/file_{n}", "w") as f_obj:
            f_obj.write(LINE[n - 1])
    print(f"3. файлы сохранены в папку {dir_name}")
