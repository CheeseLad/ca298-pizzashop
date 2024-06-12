from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import * 
from .models import *
from datetime import timedelta

def index(request):
    if request.user.is_authenticated:
      orders = PizzaOrder.objects.filter(user=request.user)
    else:
      orders = None
    return render(request, 'index.html', {'title': 'Home', 'orders': orders})


@login_required
def order_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            new_order = form.save()
            newPizzaOrder = PizzaOrder(user=request.user, pizza=new_order, payment=None)
            newPizzaOrder.save()
            return redirect(payment)
        else:
            return render(request, 'order_pizza.html', {'form': form, 'title': 'Order'})
    else:
        form = PizzaForm()
        return render(request, 'order_pizza.html', {'form': form, 'title': 'Order'})
    
@login_required
def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            filter = PizzaOrder.objects.filter(user=request.user).latest('id')
            new_payment = form.save()
            filter.payment = new_payment
            filter.save()
            latest_order_date = filter.date_ordered + timedelta(minutes=30)
            formatted_date = latest_order_date.strftime("%b. %d, %Y, %I:%M %p")
            return render(request, 'order_complete.html', {'order': filter, 'title': 'Order Complete', 'arrival_time': formatted_date})
        else:
            return render(request, 'payment.html', {'form': form, 'title': 'Payment'})
    else:
        form = PaymentForm()
        return render(request, 'payment.html', {'form': form, 'title': 'Payment'})

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class UserLoginView(LoginView):
    template_name='login.html'


def logout_user(request):
    logout(request)
    return redirect("/")