def display_notes(notes):
    """Display all notes."""
    if not notes:
        print("No notes available.")
    else:
        print("\nYour Notes:")
        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note}")
        print()

def add_note(notes):
    """Add a new note."""
    note = input("Enter your note: ")
    notes.append(note)
    print("Note added.\n")

def remove_note(notes):
    """Remove a note by its number."""
    display_notes(notes)
    try:
        note_num = int(input("Enter the number of the note to remove: "))
        if 1 <= note_num <= len(notes):
            removed_note = notes.pop(note_num - 1)
            print(f"Note '{removed_note}' removed.\n")
        else:
            print("Invalid note number.\n")
    except ValueError:
        print("Invalid input.\n")

def note_taking():
    notes = []
    
    print("Welcome to the Note-Taking Application!")
    
    while True:
        print("1. View Notes")
        print("2. Add Note")
        print("3. Remove Note")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            remove_note(notes)
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    note_taking()
