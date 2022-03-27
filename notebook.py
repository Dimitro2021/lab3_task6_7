""" Notebook """

import datetime
# Store the next available id for all new notes
last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''
    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    def match(self, filter):
        '''Determine if this note matches the filter
         text. Return True if it matches, False otherwise.
         Search is case sensitive and matches both text and
         tags.
         >>> a = Note('memo', 'tag')
         >>> a.match('memo')
         True
         '''
        return filter in self.memo or filter in self.tags




class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''
    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []
    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.
        >>> b = Notebook()
        >>> b.new_note('memo11', 'tag22')
        >>> isinstance(b.notes, list)
        True
         '''
        self.notes.append(Note(memo, tags))
    def _find_note(self, note_id):
        '''Locate the note with the given id.
        >>> b = Notebook()
        >>> b.new_note('memo11', 'tag22')
        >>> b._find_note('33')
        '''
        for note in self.notes:
            if note.id == int(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.
        >>> b = Notebook()
        >>> b.new_note('memo11', 'tag22')
        >>> print(b.notes[0].id)
        3
        >>> b.modify_memo(3, 'memo_new')
        '''
        self._find_note(note_id).memo = memo
    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        tags to the given value.
        >>> b = Notebook()
        >>> b.new_note('memo11', 'tag22')
        >>> b. modify_memo(4, 'tag_new')
        '''
        for note in self.notes:
            if note.id == int(note_id):
                note.tags = tags
                break
    def search(self, filter):
        '''Find all notes that match the given filter
        string.
        >>> b = Notebook()
        >>> b.new_note('memo11', 'tag22')
        >>> b.search('memo11')[0].id
        6
        '''
        return [note for note in self.notes if
                note.match(filter)]

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
