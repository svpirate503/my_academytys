from django.urls import path 
from . import views

urlpatterns=[
    path('cursos/',views.course_list,name="curso-list"),
    path('cursos/<int:curso_id>/',views.course_detail,name="curso-detail"),
    path('curso-detail/<int:curso_id>/',views.course_access,name="curso-access"),
    path('signup/',views.register,name="signup"),
    path('sigin/',views.log_in,name="sigin"),
    path('checkout-session/<int:curso_id>/',views.comprar_curso,name="comprar-curso"),
    path('stripe-webhook/',views.stripe_webhook,name="stripe-webhook"),
    path('curso/<int:curso_id>/leccion/<int:leccion_id>/',views.ver_video,name="ver-video"),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.login_out,name='logout'),
    path('tutoriales/',views.tutoriales,name='tutoriales'),
    path('tutoriales/<int:tuto_id>/',views.tutoriales_detail,name='tutoriales-detail')
    
]