'''
class Notification:
    def alert(self):
        print("Bip bip")

class EmailNotification(Notification):
    def alert(self):
        super().alert()
        print('Ping')

email_alert = EmailNotification()
email_alert.alert()
'''
# *args, **kwargs


class Greeter:
    def greet(self, name="Guest", greeting = "Hello"):
        print(f"{greeting}, {name}")


greeter = Greeter()
greeter.greet()
greeter.greet(name = "Alice")
greeter.greet(greeting="Welcome")