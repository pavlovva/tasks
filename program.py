import logging

FILE = './manga.txt'

publisher_name = input('Enter publisher name: ')


def get_publisher_list():
    with open(FILE, 'r', encoding='utf-8') as file:
        current_publisher_list = []
        for string in file:
            split_string = string.rstrip().replace(' ', '').split(',')
            if split_string[1].replace(' ', '') == publisher_name:
                current_publisher_list.append(split_string)
    return current_publisher_list


def get_name_of_manga(current_publisher_list: list) -> str:
    try:
        result = current_publisher_list[0][0]
        return result
    except IndexError:
        logging.error('Can not get name of the manga')


def get_number_of_published_volumes(current_publisher_list: list) -> int:
    result = len(current_publisher_list)
    if result > 0:
        return result
    else:
        logging.error('Can not get number of the published volumes')


def get_number_of_chapters(current_publisher_list: list) -> int:
    number_of_chapters = 0
    for element in current_publisher_list:
        try:
            number_of_chapters += len(element[4::])
        except IndexError:
            logging.error('Can not get number of chapters')
    return number_of_chapters


def lengths_of_all_manga_chapters(current_publisher_list: list) -> list:
    chapters_list = []
    lengths_of_all_manga_chapters = []

    for element in current_publisher_list:
        try:
            chapters = [int(element) for element in element[3::]]
            chapters.sort()
            chapters_list.append(chapters)
        except IndexError:
            logging.error('Can not get lengths of all manga chapters')

    for element in chapters_list:
        lengths_of_all_manga_chapters += [element[x + 1] - element[x] for x in range(len(element) - 1)]

    return lengths_of_all_manga_chapters


def get_average_chapter_length(current_publisher_list: list) -> float:
    number_of_chapters = get_number_of_chapters(current_publisher_list)
    chapter_length = sum(lengths_of_all_manga_chapters(current_publisher_list))
    average_chapter_length = float('{0:.2f}'.format(chapter_length / number_of_chapters))

    return average_chapter_length


def get_final_string() -> str:
    result_string = ""
    result_string += get_name_of_manga(get_publisher_list()) + ', '
    result_string += str(get_number_of_published_volumes(get_publisher_list())) + ', '
    result_string += str(get_number_of_chapters(get_publisher_list())) + ', '
    result_string += str(get_average_chapter_length(get_publisher_list())) + '\n'

    for element in lengths_of_all_manga_chapters(get_publisher_list()):
        result_string += str(element) + ', '
    return result_string[0:-2]


def create_final_file(name: str):
    file_name = name.replace(' ', '_')
    with open(f'./{file_name}.txt', 'w') as file:
        file.write(get_final_string())


create_final_file(publisher_name)
