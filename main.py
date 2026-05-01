#4-m
class Employee:
    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience
        
    def work(self):
        print(f"{self.name} ishlamoqda")
        
    
class Manager(Employee):
    def __init__(self, name, salary, experience, dapartment, team_size):
        super().__init__(name, salary, experience)
        self.dapartment = dapartment
        self.team_size = team_size
        
    def work(self):
        super().work()
        print(f"Maneger {self.dapartment} bo'limi boshqarmoqda")
        
m1 = Manager("Ali", "Gtd", "mmm", "Dasturchi", "Eglish team")
m1.work()
             
