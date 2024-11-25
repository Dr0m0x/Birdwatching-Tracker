# Birdwatching-Tracker
from datetime import datetime

# List to store bird sightings
bird_sightings = []


# Function to add a new sighting
def add_sighting():
    bird_name = input("Enter the bird name: ")
    sighting_date = input("Enter the date of sighting (yyyy-mm-dd): ")
    location = input("Enter the location of sighting: ")

    # Convert date to a datetime object for consistency
    sighting_date = datetime.strptime(sighting_date, '%Y-%m-%d')

    # Create a sighting dictionary and append to the list
    sighting = {'bird_name': bird_name, 'sighting_date': sighting_date, 'location': location}
    bird_sightings.append(sighting)

    print("Sighting added successfully!\n")


# Function to view all sightings
def view_sightings():
    if len(bird_sightings) == 0:
        print("No sightings to display.\n")
    else:
        for sighting in bird_sightings:
            print(
                f"{sighting['bird_name']} spotted on {sighting['sighting_date'].strftime('%Y-%m-%d')} at {sighting['location']}")
        print()


# Function to filter sightings by bird name
def filter_by_bird_name():
    bird_name = input("Enter the bird name to filter by: ")
    filtered_sightings = [sighting for sighting in bird_sightings if bird_name.lower() in sighting['bird_name'].lower()]

    if len(filtered_sightings) == 0:
        print("No sightings found for that bird.\n")
    else:
        for sighting in filtered_sightings:
            print(
                f"{sighting['bird_name']} spotted on {sighting['sighting_date'].strftime('%Y-%m-%d')} at {sighting['location']}")
        print()


# Function to filter sightings by date
def filter_by_date():
    filter_date = input("Enter the date to filter by (yyyy-mm-dd): ")
    filter_date = datetime.strptime(filter_date, '%Y-%m-%d')

    filtered_sightings = [sighting for sighting in bird_sightings if
                          sighting['sighting_date'].date() == filter_date.date()]

    if len(filtered_sightings) == 0:
        print("No sightings found for that date.\n")
    else:
        for sighting in filtered_sightings:
            print(
                f"{sighting['bird_name']} spotted on {sighting['sighting_date'].strftime('%Y-%m-%d')} at {sighting['location']}")
        print()


# Function to filter sightings by location
def filter_by_location():
    location = input("Enter the location to filter by: ")
    filtered_sightings = [sighting for sighting in bird_sightings if location.lower() in sighting['location'].lower()]

    if len(filtered_sightings) == 0:
        print("No sightings found for that location.\n")
    else:
        for sighting in filtered_sightings:
            print(
                f"{sighting['bird_name']} spotted on {sighting['sighting_date'].strftime('%Y-%m-%d')} at {sighting['location']}")
        print()


# Main program loop
def main():
    running = True
    while running:
        print("Birdwatching Tracker")
        print("1. Add a new sighting")
        print("2. View all sightings")
        print("3. Filter sightings by Bird Name")
        print("4. Filter sightings by Date")
        print("5. Filter sightings by Location")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_sighting()
        elif choice == '2':
            view_sightings()
        elif choice == '3':
            filter_by_bird_name()
        elif choice == '4':
            filter_by_date()
        elif choice == '5':
            filter_by_location()
        elif choice == '6':
            running = False
        else:
            print("Invalid choice, try again.\n")


# Start the program
if __name__ == "__main__":
    main()
