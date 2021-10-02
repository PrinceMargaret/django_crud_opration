from django.shortcuts import render,HttpResponse ,redirect
from .models import Person
from .form import nameForm
# Create your views here.
def home(request):
                              
                      #fetch data from database 
                      
   #person= Person.objects.all()                                     #person is a list of objects
   #person= Person.objects.all().order_by('-id')                     #reverse order get objects in descending order
   #person= Person.objects.all().order_by('id')                      #ascending order get objects in ascending order
   #person= Person.objects.all().order_by('-id')[:5]                 #get 5 objects in descending order
   #person= Person.objects.all().order_by('id')[:5]                  #get 5 objects in ascending order
   #person=Person.objects.get(id=2)                                  #get object with id=2
   
                      # apply in Templates
              
              
                         #{% for board in boards %}
                         #{{ board.name }} <br>
                         #{% endfor %}
             
             #Board.objects.create(coulmn1='...', coulmn2='...')      #create as well as  save both
             
             #board = Board()
             #board.save()                                         #  for save save
   person=Person.objects.all()
   '''l=[]
   for i  in person:
     l.append(i)'''
   d={"p":person}
    #response_html = '<br>'.join(Person.fname)
   #return HttpResponse(person)
   return render(request,'index.html',d)
   
 
   
def newForm(request):
  
  if request.method == 'POST':
    fm= nameForm(request.POST)  # html form 
    
    if fm.is_valid():
      f=fm.cleaned_data['fname']
      l=fm.cleaned_data['lname']
      
      r=Person(fname=f,lname=l)    # table
      #p=Person.objects.get(id=3)
      r.save()
      #return redirect("home")
      return HttpResponse(f"Your Data sucessfully submitted")
  else:
    fm = nameForm()
    return  render(request, 'form.html', {'form': fm})