from datetime import datetime
# Implement the necessary static and class methods
# Use the static method to check if a given date is valid for an event
# Use the class method to keep track of how many events have been created 

class EventManager:
    event_count = 0

    def __init__(self, event_name, event_date):
        self.event_name = event_name
        self.event_date = event_date
        EventManager.event_count += 1

    @staticmethod
    def is_valid_date(date):
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return False
        if date_obj.weekday() >= 5:
            return False
        
        return True

    @classmethod
    def get_event_count(cls):
        
        return f"Total events: {cls.event_count}"

# Creating instances and testing the methods
    
event1 = EventManager("Concert", "2023-05-21")
event2 = EventManager("Conference", "2023-05-18")

print("Valid date for event 1: ", EventManager.is_valid_date(event1.event_date))
print("Valid date for event 2: ", EventManager.is_valid_date(event2.event_date))

print(EventManager.get_event_count())