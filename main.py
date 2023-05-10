from peewee import *
import argparse
import sys

db = PostgresqlDatabase('notes', 
                        user='ca', 
                        password='123',
                        host='localhost', 
                        port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField()
    contents = TextField()
    

def note_taker():
    db.create_tables([Note])
    user_input = input('Welcome to Note Taker! What would you like to do?\nCreate a note (type: create),\nUpdate a note (type: update),\nDelete a note (type: delete),\nView all notes (type: view)\nor exit (type: exit)?:\n')
    # user_input2 = input('What else would you like to do while here?\ncreate, update, delete, view, or exit?:\n')
    if user_input.lower() == 'create':
        note_title = input('Note Title: ')
        note_contents = input('Note Contents: ')
        note1 = Note(title= f'{note_title}', contents= f'{note_contents}')
        note1.save()
        print(note1.title)
        print(note1.contents)
        note_taker()
    elif user_input.lower() == 'update':
        list_of_notes = Note.select()
        print([notes.title for notes in list_of_notes])
        note_update_input = input("What note would you like to edit?\n")
        note_update = Note.get(Note.title == f'{note_update_input}')
        note_update_detail = input("Do you want to edit the title or the content?\n")
        if note_update_detail.lower() == 'title':
            note_update_title = input("What would you like the title to be instead?\n")
            note_update.title = note_update_title
            print('Thanks! Your note title has been updated!')
            note_update.save()
        elif note_update_detail.lower() == 'content':
            note_update_contents = input("What would you like the contents to be instead?\n")
            note_update.contents = note_update_contents
            print('Thanks! Your note contents have been updated!')
            note_update.save()
        else:
            print('Please input the proper value!')
        note_taker()
    elif user_input.lower() == 'delete':
        list_of_notes = Note.select()
        print([notes.title for notes in list_of_notes])
        note_delete_input = input("Please input the title of the note that you would like to delete:\n")
        note_delete = Note.get(Note.title == f'{note_delete_input}')
        note_delete.delete_instance()
        print('Your note has been deleted!')
        note_taker()
    elif user_input.lower() == 'view':
        list_of_notes = Note.select()
        print([notes.title for notes in list_of_notes])
        note_find_title = input("Which note would you like to view:\n")
        note_title = Note.select().where(Note.title == f'{note_find_title}')
        print([note.contents for note in note_title])
        note_taker()
    elif user_input.lower() == 'exit':
        print('Bye Bye')
        return
    else:
        print('Please type in a valid response!')
        note_taker()
        
note_taker()
            


# db.drop_tables([Note])
# db.create_tables([Note])

# sys.arg[1]

# note_title = input('Note Title: ')
# note_contents = input('Note Contents: ')
# note1 = Note(title= f'{note_title}', contents= f'{note_contents}')
# note1.save()

# note1 = Note(note_title= f'{sys.argv[1]}', note_contents= f'{sys.argv[2]}')
# note1.save()

# note_finder = input('Which note would you like to view? Please input the title of the note below.\n')

# list_of_notes = Note.select()
# print([notes.contents for notes in list_of_notes])

# note_lookup = Note.select().where(Note.title == f'{note_finder}')
# print([note.contents for note in note_lookup])

# list_of_notes = Note.select()
# print([notes.contents for notes in list_of_notes])
# print([notes.contents for notes in list_of_notes])

