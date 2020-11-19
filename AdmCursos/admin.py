from django.contrib import admin
from .models import Alumno
from .models import Docente
from .models import Curso
from .models import Curso_Docente
from .models import Curso_Alumno

admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Curso)

admin.site.register(Curso_Alumno)
admin.site.register(Curso_Docente)
# Register your models here.

