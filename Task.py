import json
import datetime

def read_notes_file(file_name):
    with open(file_name,'r') as f:
        notes = json.load(f)
    return notes

def save_notes_json(notes, file_name):
    with open(file_name, 'w') as f:
        json.dump(notes, f)

def filter_notes_by_date(notes, date):
    filter_notes = []
    for note in notes:
        note_date = datetime.datetime.strptime(note["timestamp"], '%Y-%m-%d')
        if note_date.date() == date:
            filter_notes.append(note)
    return filter_notes

def print_notes(notes):
    if not notes:
        print('Заметок не найдено ')
    else:
        for note in notes:
            print(f'ID: {note["id"]}')
            print(f'Заголовок: {note["title"]}')
            print(f'Тело заметки: {note["body"]}')
            print(f'Дата: {note["timestamp"]}')

def add_note(notes):
    id = len(notes) + 1
    title = input('Введите заголовок:  ')
    body = input('Введите тело заметки:  ')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d')
    new_note = {'id': id, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(new_note)
    print('Заметка успешно добавлена  ')
    return notes

def edit_note(notes, id):
    for note in notes:
            if note["id"] == id:
                print(f'Заметка ID: {note["id"]}')
                print(f'Заголовок: {note["title"]}')
                print(f'Тело заметки: {note["body"]}')
                print(f'Дата: {note["timestamp"]}')
                print('Введите изменения:  ')
                new_title = input('Введите новый заголовок:   ')
                new_body = input('Введите новое тело заметки:  ')
                note["title"] = new_title
                note["body"] = new_body
                note["timestamp"] = datetime.datetime.now().strftime('%Y-%m-%d')                
                print('Заметка успешно изменена  ')
                print('***********************************************')
                break

    return notes

def delete_note(notes, id):
    for note in notes:
            if note["id"] == id:
                print(f'Заметка ID: {note["id"]}')
                print(f'Заголовок: {note["title"]}')
                print(f'Тело заметки: {note["body"]}')
                print(f'Дата: {note["timestamp"]}')
                print('Заметка удалена ')
                notes.remove(note)
                print('***********************************************')
                break
    return notes
    




file_name = 'notes.json'
notes = read_notes_file(file_name)
while True:
    print('***********************************************')
    print('Выберите действие: ')
    print('1 - Вывести все заметки ')
    print('2 - Вывести заметки за определенную дату ')
    print('3 - Вывести конкретную заметку ')
    print('4 - Добавить новую заметку ')
    print('5 - Редактировать заметку ')
    print('6 - Удалить заметку ')
    print('7 - Выход ')
    print('***********************************************')

    choice = input('Ваш выбор:   ')

    if choice == '1':
        print_notes(notes)

    elif choice == '2':
            date_str = input('Введите дату в формате ГГГГ-ММ-ДД:    ')
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            filter_notes = filter_notes_by_date(notes, date)
            print(f'Заметки за дату -> {date_str}:  ')
            print_notes(filter_notes)
    
    elif choice == '3':
        id = int(input('Введите ID заметки:   '))
        note = [note for note in notes if note['id'] == id]
        print_notes(note)

    elif choice == '4':
        notes = add_note(notes)
        save_notes_json(notes, file_name)
    
    elif choice == '5':
        id = int(input('Введите ID  заметки для редактирования:   '))
        notes = edit_note(notes,id)
        save_notes_json(notes, file_name)
        
    
    elif choice == '6':
        id = int(input('Введите ID заметки для удаления:   '))
        notes = delete_note(notes, id)
        save_notes_json(notes, file_name)
    
    elif choice == '7':
        break

    else:
        print('недопустимый выбор')
