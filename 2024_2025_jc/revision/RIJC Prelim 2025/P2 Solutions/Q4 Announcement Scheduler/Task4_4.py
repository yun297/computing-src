
def add_announcement(filename="announcement.txt"):
    """
    Prompts the user to input a new announcement's details and appends it to the announcements file.

    Parameters:
    - filename (str): The file to which the announcement should be saved. Default is 'announcements.txt'.

    Expected Input from User:
    - Department (e.g., 'CCA', 'Science')
    - Priority ('High', 'Medium', or 'Low')
    - Duration in seconds (e.g., 90)
    - Title of the announcement

    The function writes the announcement in CSV format to the specified file.
    """
    print("Enter a new announcement:") #1m - prompts for all required fields and formats to valid CSV string
    department = input("Department: ")
    priority = input("Priority (High/Medium/Low): ")
    duration = input("Duration (seconds): ")
    title = input("Title: ")
    new_announcement = f"{department},{priority},{duration},{title}\n"
    with open(filename, "a") as f:
        f.write(new_announcement) #1m Appends CSV-string to file
    print("Announcement added successfully.\n")

add_announcement()
