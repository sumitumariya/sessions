from django.shortcuts import render

# Create your views here.
def Register(request):
    return render(request,'Resgiter.html')



def RegisterData(request):
    if request.method == "POST":
       
        email = request.POST.get('email')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        request.session['name']=name
        request.session['email']=email
        request.session['contact']=contact
        request.session['password']=password

        return render(request,'Resgiter.html')
    
def login(request):
    return render(request,'login.html')
    
def logindata(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
       
        email1=request.session.get('email')
        name1=request.session.get('name')
        contact1=request.session.get('contact')
        password1=request.session.get('password')
        context={
            'Em':email1,
            'Nm':name1,
            'Cm':contact1,
            'Ps':password1
        }
        print(email1,name1,password1,contact1)
        if email1 == email:
            if password1==password:
                return render(request,'dashboard.html',{'context':context})
            else:
                msg="successful"
                return render(request,'login.html',{'msg':msg})

def dashboard(request):
    return render(request,'dashboard.html')

def logout(request):
    if request.session:
        request.session.flush()
        return render(request,'Resgiter.html')

