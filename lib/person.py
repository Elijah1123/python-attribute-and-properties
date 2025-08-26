APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = APPROVED_JOBS  # Use the global list for consistency

    def __init__(self, name="Unknown", job="Admin"):
        self.name = name
        self.job = job

    # Name property with validation and title casing
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case before saving
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")

    # Job property with validation
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.approved_jobs:
            self._job = value
        else:
            raise ValueError(f"Job must be in the approved list: {Person.approved_jobs}")



if __name__ == "__main__":
    print("=== Person Class Demo (All Valid Values) ===")

    
    p1 = Person("Elijah Mzalindu", "ITC")
    print(f"Name: {p1.name}, Job: {p1.job}")

    
    p2 = Person("Alice", "Finance")
    print(f"Name: {p2.name}, Job: {p2.job}")

    
    p3 = Person("Bob", "Marketing")
    print(f"Name: {p3.name}, Job: {p3.job}")

    
    p4 = Person("Clara", "Human Resources")
    print(f"Name: {p4.name}, Job: {p4.job}")