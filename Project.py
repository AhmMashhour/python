class Person:
    """Represents a basic person with health and mood attributes."""
    
    def __init__(self, name: str, money: float, mood: str, health_rate: int):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = max(0, min(health_rate, 100))  # clamped between 0 and 100

    def sleep(self, hours: int) -> None:
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals: int) -> None:
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items: int) -> None:
        self.money -= 10 * items


class Car:
    """Represents a car with fuel and velocity constraints."""
    
    def __init__(self, name: str, fuel_rate: int, velocity: int):
        self.name = name
        self.fuel_rate = max(0, min(fuel_rate, 100))
        self.velocity = max(0, min(velocity, 200))

    def run(self, velocity: int, distance: float) -> None:
        self.velocity = max(0, min(velocity, 200))

        while distance > 0 and self.fuel_rate > 0:
            distance -= 10
            self.fuel_rate -= 10

        self.stop(distance)

    def stop(self, remaining_distance: float) -> None:
        self.velocity = 0
        if remaining_distance > 0:
            print(f"You stopped with {remaining_distance} km left due to no fuel.")
        else:
            print("You have arrived at your destination.")


class Employee(Person):
    """Extends Person with job-related attributes and behaviors."""

    def __init__(self, name: str, money: float, mood: str, health_rate: int,
                 emp_id: int, car: Car, email: str, salary: float, distance_to_work: float):
        super().__init__(name, money, mood, health_rate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = max(1000, salary)  # enforce a minimum salary
        self.distance_to_work = distance_to_work

    def work(self, hours: int) -> None:
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance: float) -> None:
        self.car.run(self.car.velocity, distance)

    def refuel(self, gas_amount: int = 100) -> None:
        self.car.fuel_rate = min(self.car.fuel_rate + gas_amount, 100)

    def send_mail(self, to: str, subject: str, body: str, receiver_name: str) -> None:
        with open("email.txt", "w") as f:
            f.write(f"To: {to}\nSubject: {subject}\nBody: {body}\nReceiver: {receiver_name}")


class Office:
    """Manages a collection of employees."""
    
    employees_num = 0

    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def get_all_employees(self) -> list:
        return self.employees

    def get_employee(self, emp_id: int) -> Employee | None:
        return next((emp for emp in self.employees if emp.id == emp_id), None)

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        Office.employees_num += 1

    def fire(self, emp_id: int) -> None:
        self.employees = [emp for emp in self.employees if emp.id != emp_id]
        Office.employees_num = max(0, Office.employees_num - 1)

    def deduct(self, emp_id: int, deduction: float) -> None:
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary = max(0, emp.salary - deduction)

    def reward(self, emp_id: int, reward: float) -> None:
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward

    def check_lateness(self, emp_id: int, move_hour: float) -> None:
        emp = self.get_employee(emp_id)
        if emp and emp.car.velocity > 0:
            is_late = Office.calculate_lateness(9, move_hour, emp.distance_to_work, emp.car.velocity)
            if is_late:
                self.deduct(emp_id, 10)
            else:
                self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(target_hour: float, move_hour: float, distance: float, velocity: float) -> bool:
        if velocity == 0:
            return True  # can't move, definitely late
        arrival_time = move_hour + (distance / velocity)
        return arrival_time > target_hour

    @classmethod
    def change_emps_num(cls, num: int) -> None:
        cls.employees_num = max(0, num)
