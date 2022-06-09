from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from .initial_func import pk_gen, staff_pk_gen

# def pk_gen():
# 	readers = Reader.objects.all()
# 	pk = 0
# 	for reader in readers:
# 		pk += 1
# 		if reader.pk != 'DG{}'.format(str(pk).zfill(6)):
# 			print(reader.pk)
# 			return 'DG{}'.format(str(pk).zfill(6))
# 	pk += 1
# 	return 'DG{}'.format(str(pk).zfill(6))


# def staff_pk_gen():
# 	staffs = Staff.objects.all()
# 	pk = 0
# 	for staff in staffs:
# 		pk += 1
# 		if staff.pk != 'NV{}'.format(str(pk).zfill(6)):
# 			print(staff.pk)
# 			return 'NV{}'.format(str(pk).zfill(6))
# 	pk += 1
# 	return 'NV{}'.format(str(pk).zfill(6))
class Customer(models.Model):
	user = models.OneToOneField(User, null=True,blank=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	birth = models.DateField(null=True, blank=True)
	address = models.CharField(max_length=200, null=True, blank=True)
	profile_pic = models.ImageField(default="profile_pic.png", null=True,blank=True)
	date_created = models.DateTimeField(null=True,  blank=True)

	def __str__(self):
		return self.name

class Reader(Customer):
	READER_TYPE = [
		('Male', 'Nam'),
		('Female', 'Nữ')
	]
	
	reader_type = models.CharField(max_length=200, null=True, choices=READER_TYPE, blank=True)
	email = models.EmailField(max_length=200, null=True, blank=True)
	rId = models.CharField(default=pk_gen, primary_key=True, unique=True, max_length=255)

class Staff(Customer):
	CETIFICATE = [
		('Baccalaureate', 'Tú tài'),
		('Intermediate', 'Trung cấp'),
		('College1', 'Cao đẳng'),
		('College2', 'Đại học'),
		('Master', 'Thạc sĩ'),
		('Doctor', 'Tiến sĩ')
	]
	POSITION = [
		('President','Giám đốc'),
		('Vice President','Phó giám đốc'),
		('Manager','Trưởng phòng'),
		('Deputy','Phó phòng'),
		('Staff','Nhân viên'),
	]
	SERVICE = [
		('Librarian', 'Thủ thư'),
		('Cashier', 'Thủ quỹ'),
		('Stockkeeper', 'Thủ kho'),
		('Board of manager', 'Ban giám đốc'),
	]
	certificate = models.CharField(max_length=200, null=True, choices=CETIFICATE, blank=True)
	position = models.CharField(max_length=200, null=True, choices=POSITION, blank=True)
	service = models.CharField(max_length=200, null=True, choices=SERVICE, blank=True)
	sId = models.CharField(default=staff_pk_gen, primary_key=True, unique=True, max_length=255)
	# force_password_change = models.BooleanField(default=True)


class BookCategory(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Book(models.Model):

	name = models.CharField(max_length=200, null=True)
	cover_pic = models.ImageField(default="logo.png", null=True,blank=True)
	ctg = models.ManyToManyField(BookCategory, blank=True)							# Category
	author = models.CharField(max_length=200, null=True, blank=True)					# Author
	price = models.PositiveIntegerField(null=True,blank=True)
	quantity = models.PositiveIntegerField(null=True,blank=True)
	publisher = models.CharField(max_length=200, null=True, blank=True)
	pubYear = models.PositiveIntegerField(default=datetime.date.today().year, validators=[MaxValueValidator(datetime.date.today().year+1), MinValueValidator(1500)])
	addDate = models.DateTimeField(null=True, auto_now_add=True)

	def __str__(self):
		return self.name