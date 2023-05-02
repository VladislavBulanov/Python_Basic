import json
from typing import Optional, List


def get_data_from_json(filename: str) -> Optional[dict]:
    """
    The function returns dictionary with data from specified JSON-file.
    :param filename: name of JSON-file
    """
    try:
        with open(f'{filename}.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Указанный файл не найден.')


def compare_dictionaries(
        dictionary_1: dict, dictionary_2: dict, diff_list: List[str]
) -> dict:
    """
    The function compares two dictionaries by specified keys. If values are
    different the value of second dictionary is added in result dictionary.
    :param dictionary_1: first dictionary (old data)
    :param dictionary_2: second dictionary (new data)
    :param diff_list: keys by which the differences are searching for
    :return: dictionary with the newest data
    """
    result_dictionary = dict()
    for key, value in dictionary_1.items():
        if (dictionary_1[key] != dictionary_2[key]) and (key in diff_list):
            result_dictionary[key] = dictionary_2[key]
        else:
            if isinstance(value, dict):
                result = compare_dictionaries(value, dictionary_2[key], diff_list)
                if result:
                    result_dictionary[value] = result
    return result_dictionary


if __name__ == '__main__':
    old_data = get_data_from_json('json_old')
    new_data = get_data_from_json('json_new')
    difference_list = ["services", "staff", "datetime"]
    changed_data = compare_dictionaries(old_data, new_data, difference_list)
    print(changed_data if changed_data
          else 'Данные по указанным ключам не изменились.')
