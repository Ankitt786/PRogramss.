from django.shortcuts import render,redirect
from django.http import HttpResponse
from icecream.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib.auth import logout

# from django.contrib.auth import auth_login

def index(request):
    # # if request.user.is_authenticated:
    return render( request,"index.html")

    return render( request,"index.html")

def home(request):
    return render( request,"home.html")

def contact(request):
    if request.method=="POST":
      firstname=request.POST.get("firstname")
      lastname=request.POST.get("lastname")
      email=request.POST.get("email")
      phone=request.POST.get("phone")
      contact=Contact(firstname=firstname,lastname=lastname,email=email,phone=phone,)
      contact.save()
      messages.success(request, 'Your message has been sent!')
    return render(request,"contact.html")

def services(request):
    return render( request,"services.html")


def signup(request):
	if request.user.is_authenticated:
		return  redirect('/')

	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		number = request.POST['number']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		
		number_check = User.objects.filter(username=number).exists()
		email_check = User.objects.filter(email=email).exists()
		
		if number_check == True :
			messages.error(request,"Your Number  Already Exists")
			return redirect('/signup')
		
		if email_check == True:
			messages.error(request,"Your Email Already Exists")
			return redirect('/signup')


		if len(number) != 10:
			messages.error(request,'Number Should Be 10 Digit')
			return redirect('/signup')
		
		elif password != cpassword:
			messages.error(request,"Password And Confirm Did'nt Match")
			return redirect('/signup')

		else:
			user = User.objects.create_user(username=number,email=email,password=cpassword)
			user.first_name = fname 
			user.last_name = lname 
			user.save()
			messages.success(request,"Your Account Successfully Created")
			return redirect('/login')


	return render(request,'auth/signup.html')
    

def login(request):
    if request.user.is_authenticated:
      return redirect("/home")
       
    if request.method == "POST":
      number = request.POST['number']
      password=request.POST['password']

      user =authenticate(request,username=number,password=password)
      print(user)
    #   by diffult it return none in case we have to do a a logic bellow
      if user is not None:
         auth_login(request,user)
         messages.success(request,"You are Succesfully Login")
         return redirect("/home")
      else:
         messages.error(request,"Smothing went wrong!")
         return redirect("/login")
    return render(request,"auth/login.html")

def logout(request):
   auth_logout(request)
   messages.success(request,"You are succesfully log-out")
   return redirect("/home")
 


def contact_2(request):
     return render(request,"auth/contact_2.html")



