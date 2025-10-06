import os
class Announcement:
    def __init__(self, department, priority, duration, title): #1m - Correct attributes for Announcement class constructor
        """
        Initialize an Announcement object with department, priority, duration (in seconds), and title.
        """
        self.department = department
        self.priority = priority
        self.duration = int(duration)
        self.title = title

    def __str__(self): #1m - __str__() returns appropriate str representation of announcement
        """
        Return a human-readable string representation of the announcement.
        Example: "CCA - Science Fair (90s)"
        """
        return f"{self.department} - {self.title} ({self.duration}s)"

    def csv_str(self): #1m - csv_str() returns appropriate csv representation of announcement
        """
        Return a CSV-formatted string for writing to file.
        Example: "CCA,High,90,Science Fair"
        """
        return f"{self.department},{self.priority},{self.duration},{self.title}"


class Queue:
    def __init__(self): #1m - Constructor
        """
        Initialize an empty queue using a Python list.
        """
        self.items = []

    def enqueue(self, item): #1m - Enqueue a new announcement
        """
        Add an item to the back of the queue.
        """
        self.items.append(item)

    def dequeue(self): #1m - Dequeue announcement
        """
        Remove and return the item at the front of the queue, if not empty.
        """
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self): #1m - Check if queue is empty, return True/False
        """
        Return True if the queue is empty.
        """
        return len(self.items) == 0

    def output(self, file):
        """
        Write each item in the queue to a file, one per line, using its output() method.
        """
        for i in self.items:  #1m - Process eachannouncement in the queue
            print(i.csv_str(), file=file) #1m - ... write each announcement with output method

class AnnouncementScheduler:
    def __init__(self, time_limit=300): #1m - constructor with appropriate values
        """
        Initialize the scheduler with an optional time limit (in seconds).
        Sets up data structures for queues and scheduled announcements.
        """
        self.time_limit = time_limit
        self.deferred_file = "deferred_announcement.txt"
        self.announcement_file = "announcement.txt"
        self.archive_file = "read_announcements_archived.txt"
        self.scheduled = []
        self.total_time = 0
        self.queues = {"High": Queue(), "Medium": Queue(), "Low": Queue()} 

    def load_announcements(self):
        """
        Load announcements from both deferred and new announcement files.
        Returns a combined list of Announcement objects.
        """
        deferred = self.load_file(self.deferred_file) #1m - combines and returns announcements from both files
        new_ann = self.load_file(self.announcement_file)
        return deferred + new_ann 

    def load_file(self, filename):
        """
        Load Announcement objects from a CSV-formatted file.
        Returns a list of Announcement objects.
        """ 
        announcements = []
        if os.path.exists(filename): #1m - check if file exist
            with open(filename) as f:
                for line in f:
                    parts = line.strip().split(',') #1m process the file
                    if len(parts) == 4:
                        announcements.append(Announcement(*parts)) 
        return announcements #1m returns list of Announcement objects created from file contents

    def categorize(self, announcements):
        """
        Sorts announcements into the internal priority queues
        based on their 'priority' attribute.
        """
        for ann in announcements: #1m - Enqueues each announcement in correct sub-queue
            self.queues[ann.priority].enqueue(ann) 

    def process(self):
        """
        Processes announcements from high to low priority queues.
        Adds them to the schedule until the time limit is reached.
        Returns a queue containing deferred announcements.
        """
        deferred_queue = Queue() 
        for level in ["High", "Medium", "Low"]: #1m process announcements in correct order
            queue = self.queues[level]
            while not queue.is_empty():
                ann = queue.dequeue()
                if self.total_time + ann.duration <= self.time_limit: #1m - until time limit is reached
                    self.scheduled.append(ann)
                    self.total_time += ann.duration #1m - updates total_time
                else:
                    deferred_queue.enqueue(ann)
        return deferred_queue #1m - Return list of unscheduled announcements

    def display_schedule(self):
        """
        Prints the list of scheduled announcements and total time used.
        """
        print("Today's Announcements:")
        for i, ann in enumerate(self.scheduled, 1): #1m - prints out scheduled appointments  and total_time
            print(f"{i}. {ann}")
        print(f"Total Time: {self.total_time}s\n") 

    def archive_scheduled(self):
        """
        Appends the list of scheduled announcements to the archive file.
        Adds a separator line for readability.
        """
        with open(self.archive_file, "a") as f: #1m - output archived announcements
            for ann in self.scheduled:
                print(ann, file=f)
            print("=" * 80, file=f)

    def save_deferred(self, deferred_queue):
        """
        Writes the deferred announcements to the deferred announcement file
        for processing on the next day.
        """
        with open(self.deferred_file, "w") as f: #1m - output deferred announcement
            deferred_queue.output(f)

    def clear_today_file(self):
        """
        Clears the contents of the new announcement file in preparation for the next day.
        """
        open(self.announcement_file, "w").close() #1m - clears announcement.txt file

    def run(self):
        """
        Executes the full announcement scheduling routine:
        1. Load deferred and new announcements
        2. Categorize into priority queues
        3. Schedule announcements within time limit
        4. Display and archive the scheduled announcements
        5. Save unscheduled announcements
        6. Clear today's new announcements
        """
        all_ann = self.load_announcements()
        self.categorize(all_ann)
        deferred = self.process()
        self.display_schedule()
        self.archive_scheduled()
        self.save_deferred(deferred)
        self.clear_today_file()


if __name__ == "__main__":
    scheduler = AnnouncementScheduler()
    scheduler.run()