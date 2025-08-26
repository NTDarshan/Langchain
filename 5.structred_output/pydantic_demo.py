from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
    name:str = 'darshan'   #default values 
    age : Optional[int] = None   #optional values
    email: EmailStr
    cgpa : float = Field( gt=0, lt=10 , default=0 , description="A float value which represents student cgpa")  # Field with validation : using this we add constraints to our field


new_student = { 'name': 'chethan' , 'age' : '25' , 'email' : 'chethan@gmail.com' , 'cgpa' : 8.5}    #here even if you pass the str '25' pydantic is smart enough to understand and it is type type coerce it to int 
student = Student(**new_student)
print(student.model_dump())
print(student.model_dump_json())