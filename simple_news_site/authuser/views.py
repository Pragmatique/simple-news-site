from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from .token_generator import account_activation_token
from .models import MyUser
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except Exception:
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')


def signing_up(request):
    user_form = UserRegistrationForm()
    context_dictionary = {
        "user_form": user_form,
    }

    if request.method=="POST":
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=MyUser.objects.create_user(**user_form.cleaned_data)
            new_user.is_active = False
            new_user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('authuser/activate_account.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
            })
            # to_email = new_user.email
            # email = EmailMessage(email_subject, message, to=[to_email])
            # email.send(fail_silently=False)

            return redirect('authuser:signing_in')

    return render(request, 'authuser/sign_up.html',context_dictionary)

def signing_in(request):
    login_form = UserLoginForm()
    context_dictionary = {
        "login_form": login_form,
    }
    print('Hi')


    if request.method == "POST":
        # login_form = UserLoginForm(request.POST)
        user = authenticate(
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        print(user)
        if user:
            login(request, user)
            return redirect('news_posts:post_list')
        else:
            return redirect('authuser:wrong_credentials')



    return render(request, 'authuser/sign_in.html', context_dictionary)


def signing_out(request):
    logout(request)
    return redirect('news_posts:list')


def wrong_credentials(request):
    return render(request, 'authuser/wrong_credentials.html')
