import json
import os


def main():
    parsed_json = load_trello_output()
    list_to_print = select_list(parsed_json)
    cards_text = return_the_cards(list_to_print, parsed_json)
    finished = format_output(cards_text)


def load_trello_output():
    with open('hst_output.json', 'r', encoding='latin-1') as data_file:
        raw_json = json.load(data_file)
    return raw_json


def select_list(raw_data):
    list_id = 0
    mylist = []
    for item in raw_data['lists']:
        list_id += 1
        mylist.append(item['name'])
        print(list_id, ' ', item['name'])

    list_to_print = input('Select from list(numbers only)')
    list_to_print = int(list_to_print)
    selected_list = raw_data['lists'][list_to_print - 1]
    return selected_list


def return_the_cards(list_name, raw_data):
    output_list = []
    for item in raw_data['cards']:
        if item['idList'] == list_name['id']:
            output_list.append(item['name'])

    return output_list


def format_output(cards):
    # need to write to file and console. currently just writes to console.
    for card in cards:
        print('* {}'.format(card))


if __name__ == '__main__':
    main()
