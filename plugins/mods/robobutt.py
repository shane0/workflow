# testme
import csv
import os

class CSV_CRUD:
    def __init__(self, filename="data.csv"):
        self.filename = filename
        self.headers = []
        self.data = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                self.headers = next(reader, None) # Read headers if they exist
                if self.headers: # Check for empty file with no headers
                  self.data = [row for row in reader]
        else:
            print(f"File '{self.filename}' not found. Creating a new file.")
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "Age", "City"]) # Example headers

    def show_header(self):
        if self.headers:
            print(", ".join(self.headers))
        else:
            print("No headers found in the file.")
    
    def show_all(self):
        if self.headers:
          print(", ".join(self.headers))
          for row in self.data:
              print(", ".join(row))
        else:
            print("No data found in the file.")

    def show_one(self):
        if not self.data:
            print("No data to display.")
            return

        for i, row in enumerate(self.data):
            print(f"{i}: {', '.join(row)}")

        while True:
            try:
                line_index = int(input("Enter the line number to view: "))
                if 0 <= line_index < len(self.data):
                    break
                else:
                    print("Invalid line number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        selected_row = self.data[line_index]

        if self.headers:
            for i, header in enumerate(self.headers):
                print(f"{i}: {header}")
            
            while True:
                try:
                    header_index = int(input("Enter the header index to view: "))
                    if 0 <= header_index < len(self.headers):
                        break
                    else:
                        print("Invalid header index. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            print(selected_row[header_index])
            
        else:
            print("No headers are defined for this CSV.")

# Example usage (you can create data.csv in advance, or this will create a new file with headers)
manager = CSV_CRUD()
manager.show_header()
print("---")
manager.show_all()
print("---")
manager.show_one()
