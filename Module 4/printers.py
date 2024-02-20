class Printer:
    def print_document(self, document):
        raise NotImplementedError("Subclass must implement abstract method")
    
class InkjetPrinter(Printer):
    def print_document(self, document):
        print(f"Inkjet Printer: Printing {document}")


class LaserPrinter(Printer):
    def print_document(self, document):
        print(f"Laser Printer: Printing {document}")

documents = ['doc1', 'doc2']

printers = [InkjetPrinter(), LaserPrinter()]

for printer in printers:
    for doc in documents:
        printer.print_document(doc)
        