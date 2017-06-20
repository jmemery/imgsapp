from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'landscapes/index.html')
def show(request, id):
    context = {
    "id" : id
    }
    print id
    if int(id) >= 1 and int(id) <= 9 :
        return render(request, 'landscapes/snow.html', context)
    if int(id) >= 10 and int(id) <= 20:
        return render(request, 'landscapes/desert.html', context)
    if int(id) >= 21 and int(id) <= 30:
        return render(request, 'landscapes/forest.html', context)
    if int(id) >= 31 and int(id) <= 40:
        return render(request, 'landscapes/vineyard.html', context)
    if int(id) >= 41 and int(id) <= 50:
        return render(request, 'landscapes/tropics.html', context)
    else:
        return render(request, 'landscapes/invalid.html')
