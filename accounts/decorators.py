from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'reader':
			return view_func(request, *args, **kwargs)

		if group == 'librarian':
			return redirect('borrowers') 

		if group == 'stockkeeper':
			return redirect('list_book')

		if group == 'cashier':
			return redirect('receipt_list')

		if group == 'manager':
			return view_func(request, *args, **kwargs)

		if group == None:
			logout(request)
			return redirect('login')
	return wrapper_func