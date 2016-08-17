from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from . import auxiliar

# Create your views here.

def makematrix(request):

	matrix=auxiliar.consult()

	superlist=[]
	superlist.append(matrix[0].row)
	superlist.append(matrix[1].row)
	superlist.append(matrix[2].row)

	context={
		'list':superlist,
	}

	return render(request,'reportes/home.html',context)