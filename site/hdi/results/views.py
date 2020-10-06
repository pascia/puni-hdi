from django.shortcuts import render, HttpResponseRedirect
from ipware import get_client_ip
import csv
import sys
import os

module_dir = os.path.dirname(__file__)

# Create your views here.
def index(request):
    return render(request, "pages/form.html")

def results(request, id):

    with open(os.path.join(module_dir, 'db1.csv'), mode='r') as file0:
        readfile = list(csv.reader(file0))
        data= readfile[id]



    return render(request, "pages/results.html",{"link":data})


def redirect(request):
    isim = request.GET.get("isim", None)
    egitim = request.GET.get("egitim", None)
    yil = request.GET.get("yaş", None)
    mail = request.GET.get("mail", None)
    ip, is_routable = get_client_ip(request)

    row = []

    with open(os.path.join(module_dir, 'db1.csv'), mode='r') as file0:
        dba = list(csv.reader(file0))
        dba = dba[-1]
        id = int(dba[0])+1

    with open(os.path.join(module_dir, 'db1.csv'), mode='a', newline='') as file1:
        db = csv.writer(file1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        row.append(id)
        row.append(ip)
        row.append(isim)
        row.append(egitim)
        row.append(yil)
        row.append(mail)
        db.writerow(row)

    return HttpResponseRedirect(f"/res/{id}")
