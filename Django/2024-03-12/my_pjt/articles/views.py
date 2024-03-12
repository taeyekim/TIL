from django.shortcuts import render

# Create your views here.
def intro(request):
    # print(request)
    return render(request, 'intro.html')

def next_page(request):
    return render(request, 'next.html')
