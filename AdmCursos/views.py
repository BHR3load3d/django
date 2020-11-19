from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from django.shortcuts import redirect

import datetime

from .models import Curso, Alumno, Docente, Curso_Alumno, Curso_Docente

import pprint


def index(request):
    template = loader.get_template('AdmCursos/index.html')
    c = Curso.objects.filter(activo = True) #ojo: filter retorna un queryset no un solo objeto, no se puede usar .save()
    a = Alumno.objects.filter(activo = True) #ojo: filter retorna un queryset no un solo objeto, no se puede usar .save()
    d = Docente.objects.filter(activo = True) #ojo: filter retorna un queryset no un solo objeto, no se puede usar .save()
    context = {'fecha_hora': datetime.datetime.now(), 'cursos': c, 'docentes': d, 'alumnos': a}
    
    return HttpResponse(template.render(context, request))

def delete(request, entidad_id, tipo_id):
    if tipo_id == 1:
        c = Curso.objects.get(id = entidad_id)
        c.activo = False
        c.save()
    elif tipo_id == 2:
        d = Docente.objects.get(id = entidad_id)
        d.activo = False
        d.save()
    elif tipo_id == 3:
        a = Alumno.objects.get(id = entidad_id)
        a.activo = False
        a.save()
    else:
        pass


    return redirect('/AdmCursos')

def add(request, tipo_id):
    if tipo_id == 1:
        tipo_desc = 'Curso'
    elif tipo_id == 2:
        tipo_desc = 'Docente'
    elif tipo_id == 3:
        tipo_desc = 'Alumno'
    else:
        tipo_desc = 'Elección no soportada'

    template = loader.get_template('AdmCursos/add.html')
    context = {'tipo_id': tipo_id, 'tipo_desc':tipo_desc}
    return HttpResponse(template.render(context, request))

def addParticipantes(request, curso_id):
    c = Curso.objects.get(id=curso_id)
    a = Alumno.objects.all()
    d = Docente.objects.all()

    #ca = Curso_Alumno.objects.filter(curso_id=c.id)
    #cd = Curso_Docente.objects.filter(curso_id=c.id)

    ca2 = Curso_Alumno.objects.filter(curso_id=c.id).select_related('alumno_id')
    cd2 = Curso_Docente.objects.filter(curso_id=c.id).select_related('docente_id')

    # attrs = vars(ca2)
    # print(', '.join("%s: %s" % item for item in attrs.items()))


    template = loader.get_template('AdmCursos/addParticipantes.html')
    context = {'curso':c, 'lstAlumnos':a, 'lstDocentes':d, 'lstDocAsoc':cd2, 'lstAlumAsoc':ca2, 'queryAlumno': str(ca2.query)}
    return HttpResponse(template.render(context, request))

def bajaParticipante(request, entidad_id, curso_id, tipo_id):
    if tipo_id == 3:
        curso = Curso_Alumno.objects.get(alumno_id = entidad_id, curso_id = curso_id)
        curso.activo = False
        curso.delete()
    elif tipo_id == 2:
        curso = Curso_Docente.objects.get(docente_id = entidad_id, curso_id = curso_id)
        curso.activo = False
        curso.delete()
    return redirect('/AdmCursos/addParticipantes/' + str(curso_id))

def asociarParticipante(request, curso_id, tipo_id):
    if tipo_id == 3:
        curso = Curso_Alumno()
        curso.curso_id = Curso.objects.get(id=curso_id)
        curso.alumno_id = Alumno.objects.get(id=request.POST['AlumSelect'])
        curso.save()
    elif tipo_id == 2:
        curso = Curso_Docente()
        curso.curso_id = Curso.objects.get(id=curso_id)
        curso.docente_id = Docente.objects.get(id=request.POST['DocSelect'])
        curso.save()
    return redirect('/AdmCursos/addParticipantes/' + str(curso_id))