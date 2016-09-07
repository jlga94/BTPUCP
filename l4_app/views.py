from django.shortcuts import render
from django.contrib.auth import logout

def reports(request):
  context = {
    'user' : request.user,
    'boards' : ['BTPUCP', 'Aptitus', 'Bumeran'],
    'careers' : ['Ingeniería Informática', 'Ingeniería Industrial'],
    'reports' : ['Dimensión de empresas', 'Sector económico', 'Área funcional', 'Cargo solicitado', 'Conocimiento por área', 'Idiomas', 'Software', 'Grado académico', 'Competencias personales', 'Habilidades blandas'],
    'report_title' : 'Dimension de empresas'
  }
  return render(request,'l4_app/reports.html', context)

def logout_view(request):
  logout(request)
  return render(request, 'logout.html')