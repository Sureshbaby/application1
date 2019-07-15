from django.shortcuts import render,redirect,HttpResponse
from Crud.forms import king,dummy
from Crud.models import King,Dummy


def kingcreate(request):

    form = king()
    if request.method == 'POST':
        form = king(request.POST)
        if form.is_valid():
            form.save()
            return redirect(kingindex)

    return render(request,'create.html',{'form':form})

def kingindex(request):

    data = King.objects.all()
    return render(request,'kingindex.html',{'data':data})

def kingupdate(request,sn):
        data = King.objects.get(id=sn)

        form = king(instance=data)
        if request.method =='POST':
            form = king(request.POST,instance=data)
            if form.is_valid():
                form.save()
                return redirect(kingindex)

        return render(request, 'update.html', {'form': form})

def kingdelete(request,id):
   data = King.objects.get(id=id)
   data.delete()
   return redirect(kingindex)

def idcreate(request):

    form =dummy()
    if request.method == 'POST':
        form =dummy(request.POST)
        if form.is_valid():
            form.save()
            return redirect(idindex)

    return render(request,'create.html',{'form':form})

def idindex(request):

    data = Dummy.objects.all()
    return render(request,'dummy.html',{'data':data})

def idupdate(request,sn):
        data = Dummy.objects.get(id=sn)

        form =dummy(instance=data)
        if request.method =='POST':
            form =dummy(request.POST,instance=data)
            if form.is_valid():
                form.save()
                return redirect(idindex)

        return render(request, 'update.html', {'form': form})

def iddelete(request,id):
   data = Dummy.objects.get(id=id)
   data.delete()
   return redirect(idindex)

