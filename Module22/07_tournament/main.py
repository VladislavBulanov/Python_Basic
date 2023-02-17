import os

def get_next_tour_participants(datafile_path):
    datafile = open(datafile_path, 'r')
    data = datafile.read().split('\n')

    points_to_pass = int(data[0])
    next_tour_participants = dict()

    for index in range(1, len(data)):
        current_participant = data[index].split()
        if int(current_participant[2]) > points_to_pass:
            next_tour_participants[f'{current_participant[1][:1]}. '
                                   f'{current_participant[0]}'] = \
                                   int(current_participant[2])

    datafile.close()
    return sort_dictionary_by_value(next_tour_participants)


def write_information_to_file(required_path, statistics):
    result_file = open(required_path, 'a')

    result_file.write(f'{str(len(statistics))}\n')
    position = 1
    for player, points in statistics.items():
        result_file.write(f'{position}) {player} {points}\n')
        position += 1

    result_file.close()


def sort_dictionary_by_value(dictionary):
    inverted_dictionary = {value: key for key, value in dictionary.items()}
    sorted_keys_list = sorted(list(inverted_dictionary.keys()), reverse=True)
    return {inverted_dictionary[key]: key for key in sorted_keys_list}


path_to_datafile = os.path.abspath('first_tour.txt')
path_to_result_file = os.path.abspath('second_tour.txt')
next_tour_information = get_next_tour_participants(path_to_datafile)
write_information_to_file(path_to_result_file, next_tour_information)
