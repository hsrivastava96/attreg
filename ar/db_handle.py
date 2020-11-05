from .models import department
from .models import year
from .models import division
from .models import subjects
from .models import student
from .models import attendance
from .models import teacher

DEPT = department()
YEAR = year()
DIV = division()
SUB = subjects()
STU = student()
ATT = attendance()
TCH = teacher()

def get_All_Departments():
	final_List = DEPT.retrieve_all()
	return final_List

def get_All_Years():
	final_List = YEAR.retrieve_all()
	return final_List

def get_All_Divisions():
	final_List = DIV.retrieve_all()
	return final_List

def get_Al_Subjects():
	final_List = SUB.retrieve_all()
	return final_List

def get_All_Students():
	final_List = STU.retrieve_all()
	return final_List

def get_All_Attendance():
	final_List = ATT.retrieve_all()
	return final_List

def get_All_teachers():
	final_List = TCH.retrieve_all()
	return final_List

