# @staticmethod

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahreheit(celsius):
        return (celsius * 9/ 5) + 32
    
print(TemperatureConverter.celsius_to_fahreheit(0)) 