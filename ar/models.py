from django.db import models
from django.db import connection

# Create your models here.

class department(models.Model):
	d_name = models.TextField()

	def retrieve_all(self):
		con = connection.cursor()
		query = "select * from ar_department"
		con.execute(query)
		rows = con.fetchall()
		return rows

class year(models.Model):
	y_name = models.TextField()

	def retrieve_all(self):
		con = connection.cursor()
		query = "select * from ar_year"
		con.execute(query)
		rows = con.fetchall()
		return rows

class division(models.Model):
	div_name = models.TextField()

	def retrieve_all(self):
		con = connection.cursor()
		query = "select * from ar_division"
		con.execute(query)
		rows = con.fetchall()
		return rows

class subjects(models.Model):
	s_name = models.TextField()
	y_id = models.IntegerField()
	sem = models.IntegerField()
	d_id = models.IntegerField()

	def retrieve_all(self):
		con = connection.cursor()
		query = "select * from ar_subjects"
		con.execute(query)
		rows = con.fetchall()
		return rows

class student(models.Model):
	stu_name = models.TextField()
	stu_class = models.IntegerField()
	stu_roll = models.IntegerField()
	stu_dept  = models.IntegerField()

	def retrieve_all(self):
		con = connection.cursor()
		query = "select * from ar_student"
		con.execute(query)
		rows = con.fetchall()
		return rows

class attendance(models.Model):
	a_date = models.DateField()
	subject_id = models.IntegerField()
	student_rolls = models.TextField()

	def retrieve_all(self):
		con = connection.cursor()
		query = "select * from ar_attendance"
		con.execute(query)
		rows = con.fetchall()
		return rows

class teacher(models.Model):
	t_name = models.TextField()
	t_email = models.TextField()
	t_pwd = models.TextField()

	def retrieve_all(self):
		con = connection.cursor()
		query = "select * from ar_teacher"
		con.execute(query)
		rows = con.fetchall()
		return rows
