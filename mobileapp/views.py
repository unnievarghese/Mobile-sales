from django.shortcuts import render,redirect
from mobileapp.forms import mobile_form,edit_mobile_form,buyer_form,userregistrationform,edit_order_form
from mobileapp.models import mobile_model,buyer_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def adminpage(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        if uname=='unnie' and pwd=='12345':
            mobile = mobile_model.objects.all()
            context = {}
            context['mobile'] = mobile
            return render(request, 'mobiles/base.html', context)
    return render(request,'mobiles/adminsignin.html')

def registration(request):
    form=userregistrationform()
    context={}
    context['form']=form
    if request.method=='POST':
        form=userregistrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(request,'mobiles/registration.html',context)

def signin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('password')
        user=authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'signin')
    return render(request,'mobiles/signin.html')

def signout(request):
    logout(request)
    return redirect('home')

def home(request):
    mobilelist=mobile_model.objects.all()
    context={}
    context['mobile']=mobilelist
    return render(request,'mobiles/home.html',context)

def add_new_mobile(request):
    if request.method=='GET':
        mobile=mobile_form()
        context={}
        context['mobile']=mobile
        mobilelist=mobile_model.objects.all()
        context['mobilelist']=mobilelist
        return render(request,'mobiles/add_new_mobile.html',context)
    else:
        mobile=mobile_form(request.POST,request.FILES)
        if mobile.is_valid():
            mobile.save()
            return redirect('add_mobile')
        else:
            context = {}
            context['mobile'] = mobile
            mobilelist = mobile_model.objects.all()
            context['mobilelist'] = mobilelist
            return render(request, 'mobiles/add_new_mobile.html', context)

def view_mobile(request,id):
    mobile=mobile_model.objects.get(id=id)
    context={}
    context['mobile']=mobile
    return render(request,'mobiles/view_mobile.html',context)

def edit_mobile(request,id):
    if request.method=='GET':
        mobileid=mobile_model.objects.get(id=id)
        mobile=edit_mobile_form(instance=mobileid)
        context={}
        context['mobile']=mobile
        return render(request,'mobiles/edit_mobile.html',context)
    else:
        mobileid=mobile_model.objects.get(id=id)
        mobile=edit_mobile_form(request.POST,request.FILES, instance=mobileid)
        if mobile.is_valid():
            mobile.save()
            return redirect('home')

def delete_mobile(request,id):
    mobile_model.objects.get(id=id).delete()
    return redirect('home')

@login_required()
def buyer_details(request,id):
    product=mobile_model.objects.get(id=id).model_name
    form=buyer_form(initial={'product':product,'user':request.user})
    context={}
    context['form']=form
    if request.method=="POST":
        form=buyer_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['form']=form
            return render(request, 'mobiles/buyer_details.html', context)
    return render(request,'mobiles/buyer_details.html',context)

def view_orders(request):
    if request.method=='GET':
        orders=buyer_model.objects.all()
        if buyer_model.objects.last().status==None:
            obj=buyer_model.objects.last()
            obj.status='New order'
            obj.save()
        context={}
        context['orders']=orders
    return render(request,'mobiles/vieworders.html',context)

def edit_order(request,id):
    if request.method=='GET':
        order=buyer_model.objects.get(id=id)
        form=edit_order_form(instance=order)
        context={}
        context['form']=form
        return render(request,'mobiles/editorder.html',context)
    else:
        order = buyer_model.objects.get(id=id)
        form = edit_order_form(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('order')

def cancel_order(request,id):
    buyer_model.objects.get(id=id).delete()
    return redirect('order')

def search(request):
    if request.method=="GET":
        return render(request,'mobiles/search.html')
    if request.method=="POST":
        item=str(request.POST.get('item'))
        mobilelist=mobile_model.objects.filter(Q(mobile_name__iexact=item) | Q(manufacturer__iexact=item))
        context = {}
        context['mobile'] = mobilelist
        context['item']=item
        return render(request, 'mobiles/home.html', context)

def filter(request):
    if request.method=="GET":
        return render(request,'mobiles/filter.html')
    if request.method=='POST':
        min_price=request.POST.get('price1')
        max_price = request.POST.get('price2')
        mobilelist=mobile_model.objects.filter(price__gte=min_price, price__lte=max_price)
        context = {}
        context['mobile'] = mobilelist
        context['item']=[min_price,max_price]
        return render(request, 'mobiles/home.html', context)
