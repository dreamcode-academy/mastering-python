class DataProcessor:
    def __init__(self, data):
        self.data = data


    def filter(self, criteria):
        self.data = [item for item in self.data if criteria(item)]
        return self
    
    def transform(self, function):
        self.data = [function(item) for item in self.data]
        return self
    
    def output(self, destination):
        print(f'Data output to {destination}: {self.data}')
        