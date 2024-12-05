class RequiredFieldsMeta(type):
    def __new__(cls, name, bases, dct):
        required_fields = ['name', 'age']
        for field in required_fields:
            if field not in dct:
                raise TypeError(f"Missing required field: {field}")
        return super().__new__(cls, name, bases, dct)

# Class using the metaclass, this class is valid since it defines 'name' and 'age'
class Person(metaclass=RequiredFieldsMeta):
    name = 'John'
    age = 30

print("Person class created successfully:")

# Class missing a required field 'age', this will raise an error
try:
    class InvalidPerson(metaclass=RequiredFieldsMeta):
        name = 'Alice'
        # No 'age' field
except TypeError as e:
    print(e)  
