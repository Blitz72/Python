import sqlite3
# from contextlib import contextmanager


# conn = db.connect(':memory:')
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#     first TEXT,
#     last TEXT,
#     pay INTEGER
#     )""")

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    @property
    def email(self):
        return '{}.{}@ge.com'.format(self.first.lower(), self.last.lower())

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}' {})".format(self.first, self.last, self.pay)


# @contextmanager
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


# @contextmanager
def update_pay(emp, pay):
    with conn:
        c.execute("UPDATE employees SET pay=:pay WHERE first=:first AND last=:last", {'first': emp.first, 'last': emp.last, 'pay': pay})


# @contextmanager
def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first=:first AND last=:last", {'first': emp.first, 'last': emp.last})


emp1 = Employee('David', 'Bauer', 75000)
emp2 = Employee("Christy", "Bauer", 100000)

print(emp1.fullname) 
print(emp1.email)
print(emp1)
print(emp1.first)

#DO NOT DO THIS:
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(str(emp1.first), str(emp1.last), int(emp1.pay)))
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(str(emp2.first), str(emp2.last), int(emp2.pay)))
# c.execute("SELECT * FROM employees WHERE last='{}'".format(emp1.last))

# DO THESE INSTEAD:
# c.execute("INSERT INTO employees VALUES (?, ?, ?", (emp1.first, emp1.last, emp1.pay))
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp2.first, 'last': emp2.last, 'pay': emp2.pay})
# c.execute("SELECT * FROM employees WHERE last=?", (emp1.last,))
# print(c.fetchall())

# remove_emp(emp2)

# c.execute("SELECT * FROM employees WHERE first=:first", {'first': emp2.first})
# print(c.fetchall())

# conn.commit()

# insert_emp(emp2)
print(update_pay(emp1, 75500))
print(get_emps_by_name(emp1.last))


# print(c.connection)
conn.close()
# print(conn)