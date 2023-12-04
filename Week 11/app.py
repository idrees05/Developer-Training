
import sys
from database import Database

def main_menu():
    print("\nMain Menu:")
    print("1. Add a record")
    print("2. Delete a record")
    print("3. Amend a record")
    print("4. Print all records")
    print("5. Reporting")
    print("6. Exit")
    choice = input("Enter choice (1-6): ")
    return choice

def reporting_menu():
    print("\nReporting Menu:")
    print("1. Print details of all films")
    print("2. Print all films of a particular genre")
    print("3. Print all films of a particular year")
    print("4. Print all films of a particular rating")
    print("5. Exit")
    choice = input("Enter choice (1-5): ")
    return choice

def validate_input(input_str, input_type):
    while True:
        try:
            if input_type == 'int':
                return int(input(input_str))
            elif input_type == 'str':
                result = input(input_str)
                if result:
                    return result
                else:
                    raise ValueError("Input cannot be empty")
        except ValueError as e:
            print(f"Invalid input: {e}")

def print_records(records):
    if records:
        for record in records:
            print(f"ID: {record[0]}, Title: {record[1]}, Year: {record[2]}, Rating: {record[3]}, Duration: {record[4]} mins, Genre: {record[5]}")
    else:
        print("No records found.")

def main():
    db = Database('filmflix.db')
    while True:
        choice = main_menu()
        if choice == '1':
            title = validate_input("Enter film title: ", 'str')
            year = validate_input("Enter year released: ", 'int')
            rating = validate_input("Enter rating: ", 'str')
            duration = validate_input("Enter duration: ", 'int')
            genre = validate_input("Enter genre: ", 'str')
            db.add_record((title, year, rating, duration, genre))
        elif choice == '2':
            film_id = validate_input("Enter film ID to delete: ", 'int')
            db.delete_record(film_id)
        elif choice == '3':
            film_id = validate_input("Enter film ID to update: ", 'int')
            title = validate_input("Enter new film title: ", 'str')
            year = validate_input("Enter new year released: ", 'int')
            rating = validate_input("Enter new rating: ", 'str')
            duration = validate_input("Enter new duration: ", 'int')
            genre = validate_input("Enter new genre: ", 'str')
            db.update_record(film_id, (title, year, rating, duration, genre))
        elif choice == '4':
            records = db.fetch_all_records()
            print_records(records)
        elif choice == '5':
            report_choice = reporting_menu()
            if report_choice == '1':
                records = db.fetch_all_records()
                print_records(records)
            elif report_choice == '2':
                genre = validate_input("Enter genre: ", 'str')
                records = db.fetch_records_by_genre(genre)
                print_records(records)
            elif report_choice == '3':
                year = validate_input("Enter year: ", 'int')
                records = db.fetch_records_by_year(year)
                print_records(records)
            elif report_choice == '4':
                rating = validate_input("Enter rating: ", 'str')
                records = db.fetch_records_by_rating(rating)
                print_records(records)
            elif report_choice == '5':
                continue
        elif choice == '6':
            db.close()
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
