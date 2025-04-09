class patients:
    def __init__(self, name, age, date_latest_admission, medical_history):
        self.name = name
        self.age = age
        self.date_latest_admission = date_latest_admission
        self.medical_history = medical_history

    def print_details(self):
        print(f"{self.name}, {self.age}, {self.date_latest_admission}, {self.medical_history}")

# Example of using the patients class
patient1 = patients("Anna Carter", 35, "2024-05-01", "Asthma")
patient1.print_details()