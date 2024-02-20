from data_processor import DataProcessor

data = [1,2,3,4,5]

processor = DataProcessor(data)

processor.filter(lambda x: x>2).transform(lambda x: x* x).output("Console")