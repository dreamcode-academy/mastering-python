'''
system that manages electronic devices, 
specifically smartphones and digital cameras, 
and then we will use multiple inheritance to create 
a hybrid device that combines features of both.

'''
class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Device Brand: {self.brand}, Model: {self.model}")


class Smartphone(ElectronicDevice):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def make_call(self):
        print(f"Making a call on the {self.brand} {self.model}")

class Camera(ElectronicDevice):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def take_photo(self):
        print(f"Taking a photo with the {self.brand} {self.model}")

        
class SmartCamera(Smartphone, Camera):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def use_as_phone_and_camera(self):
        self.make_call()
        self.take_photo()

my_phone = Smartphone('Apple', 'iPhone13')
my_camera = Camera('Canon', 'EOS R5')
my_smart_camera = SmartCamera('Samsung', 'Galaxy Zoom')

my_phone.display_info()
my_phone.make_call()

my_camera.take_photo()

my_smart_camera.take_photo()
my_smart_camera.make_call()





