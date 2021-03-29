from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# login class
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        template = 'login.html'
        return render(request, template)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        customer = User.loginCustomer(email)

        if customer:
            if check_password(password, customer.password):
                request.session["customer_id"] = customer.id
                request.session["username"] = customer.user_name
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error_message = "Email or Password is Invalid!!!"
        else:
            error_message = "Email or Password is Invalid!!!"

        context = {
            'error': error_message
        }
        return render(request, 'login.html', context)


# logout
def logout(request):
    request.session.clear()
    return redirect('login')


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.method == 'POST':
            pst = request.POST
            uname = pst.get('username')
            phone = pst.get('mobilenumber')
            email = pst.get('email')
            password = pst.get('password')

            # validation data
            existing_value = {
                'uname': uname,
                'phone': phone,
                'email': email
            }

            customer = User(
                user_name=uname,
                phone_number=phone,
                email=email,
                password=password
            )

            # calling validation
            error_message = self.validationCustomer(customer)

            reformdata = {'exvalues': existing_value, 'error': error_message}

            if len(error_message) == 0:
                # password hashing
                customer.password = make_password(customer.password)

                # save data
                customer.register()
                return redirect('home')
            else:
                return render(request, 'signup.html', reformdata)



    def validationCustomer(self, customer):
        error_message = []
        if not customer.user_name:
            error_message.append("User Name is Required")
        elif len(customer.user_name) < 3:
            error_message.append("Minimum 3 characters is required for User name")

        if not customer.email:
            error_message.append("Email is Required")

        if not customer.password:
            error_message.append("Password is Required")

        elif len(customer.password) < 6:
            error_message.append("Minimum required length for password is 6")

        if customer.isExist():
            error_message.append("Email already exists!")

        if not customer.phone_number:
            error_message.append("Phone Number is Required")

        elif (len(customer.phone_number) == 14 and customer.phone_number.startswith('+88') == True) or (
                len(customer.phone_number) == 11 and customer.phone_number.startswith('0') == True):
            pass
        else:
            error_message.append("The Phone number is not valid!")
        return error_message

