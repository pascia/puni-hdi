from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/form.html")

def results(request, link):

    from ipware import get_client_ip
    ip, is_routable = get_client_ip(request)

    return render(request, "pages/results.html",{
    "link":link
    })
