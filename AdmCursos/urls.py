from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/add/<int:tipo_id>', views.add, name='add'),
    path('/addparticipantes/<int:curso_id>', views.addParticipantes, name='addParticipantes'),
    path('/asociarparticipante/<int:curso_id>/<int:tipo_id>', views.asociarParticipante, name='asociarParticipante'),
    path('/bajaparticipante/<int:entidad_id>/<int:curso_id>/<int:tipo_id>', views.bajaParticipante, name='bajaParticipante'),
    path('/delete/<int:entidad_id>/<int:tipo_id>', views.delete, name='delete')
]