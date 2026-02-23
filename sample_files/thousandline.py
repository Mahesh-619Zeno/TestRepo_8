def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()def notes_menu():
    notes = load_data(NOTES_FILE)
    while True:
        clear_screen()
        print("=== NOTES ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
            wait_key()

def view_notes(notes):
    clear_screen()
    print("=== Your Notes ===")
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")
            print(f"    {note['content']}")
    wait_key()

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({'title': title, 'content': content})
    save_data(NOTES_FILE, notes)
    print("Note added!")
    wait_key()

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Delete which number? ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_data(NOTES_FILE, notes)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")
    wait_key()