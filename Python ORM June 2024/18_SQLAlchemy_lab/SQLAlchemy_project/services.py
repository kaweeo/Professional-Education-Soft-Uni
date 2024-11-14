from sqlalchemy import desc

from main import Session
from models import Employee, City

# Perform Database Operations

# Create a new session, create a new employee object, add it to that session,
# and then commit the changes to the database
with Session() as session:
    employee = Employee(
        first_name='John',
        last_name='Doe',
        age=33
    )
    session.add(employee)
    session.commit()

# Retrieve all data from a table
with Session() as session:
    employees = session.query(Employee).all()
    for e in employees:
        print(e.last_name, e.age)

# Retrieve filter and order data
with Session() as session:
    employees = (
        session.query(Employee)
        .filter(Employee.last_name == 'Doe')
        .order_by(desc(Employee.last_name))
        .all()
    )

# Update a record from the db
with Session() as session:
    employee_to_update = session.query(Employee).filter(Employee.last_name == 'Doe').first()
    if employee_to_update:
        employee_to_update.last_name = 'Smith - The Hammer'
        session.commit()
        print("Employee's name updated")
    else:
        print("Employee not found")

# Delete a record from the database
with Session() as session:
    employees_to_delete = session.query(Employee).filter(Employee.age >= 65).all()
    for employee in employees_to_delete:
        session.delete(employee)
        session.commit()

# with Session() as session:
#     # Bulk delete all employees who are 65 or older
#     session.query(Employee).filter(Employee.age >= 65).delete(synchronize_session='fetch')
#     session.commit()


# Populate with multiple employees the database
employees = [
    ('John', 'McRole', 32),
    ('Sarah', 'Smith', 41),
    ('Mike', 'Johnson', 29),
    ('Emma', 'Brown', 24),
]

with Session() as session:
    employees_to_add = []
    for e in employees:
        employees_to_add.append(Employee(first_name=e[0], last_name=e[1], age=e[2]))

    session.add_all(employees_to_add)
    session.commit()
    print('All users added successfully')

# Populate with multiple employees the database
cities = [
    ('Shumen'),
    ('Sofia'),
    ('Varna'),
]

with Session() as session:
    cities_to_add = []
    for c in cities:
        cities_to_add.append(City(name=c))

    session.add_all(cities_to_add)
    session.commit()
    print('All cities added successfully')


# Simple queries for Relationships
with Session() as session:
    city = session.query(City).first()
    for e in city.employees:
        print(e.last_name, city.name )