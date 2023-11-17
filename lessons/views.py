from enum import UNIQUE
from sqlite3 import IntegrityError
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,JsonResponse
import stripe 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .decorators import user_has_purchased_course
from django.core.mail import send_mail
from django.contrib import messages





def tutoriales_detail(request,tuto_id):
    tutos = Tutoriales.objects.get(pk=tuto_id)
    comments = comentarios.objects.all()
    messagess = ''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')
        profile_picture = request.POST.get('profile_picture')


        comment = comentarios.objects.create(name=name,email=email,question=question,avatar=profile_picture)
        comment.save()
        messages.success(request,'your comment was sent.')
        return redirect('http://127.0.0.1:8000/lessons/tutoriales/1/')


    return render(request,'lessons/tutoriales_detail.html',{'tutorial':tutos,'messages':messagess,'comments':comments})





def tutoriales(request):
    tutos = Tutoriales.objects.all()

    return render(request,'lessons/tutoriales.html',{'tutoriales':tutos})



@login_required
def login_out(request):
    message = ""
    if request.method == "POST":
       
        logout(request)
        messages.success(request,"You've been successfully logout.")
        return redirect('http://127.0.0.1:8000/lessons/sigin')
      


        
    return render(request,'lessons/logout.html')


def register(request):
    error = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        picture = request.POST.get('profile_picture')
        if password == password2:
            try:
     
               
                user = User.objects.create_user(username=email,password=password)
                if user:
        
            
                    user = authenticate(request, username=email, password=password)
                    if user is not None:

                        user.save()
                        login(request,user)
                        return redirect("http://127.0.0.1:8000/lessons/cursos/")
                else:
                    error = "Usuario ya existe."
            except IntegrityError:
                error = "Este usuario ya existe"
            
        else:
        
            error = "Password doesn't match"

     
    return render(request,"lessons/register.html",{'error':error})

def log_in(request):
    error = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
       

            return redirect("http://127.0.0.1:8000/lessons/cursos/")
        else:
            error = "Email or Password incorrect."
        

   
    return render(request,"lessons/login.html",{'error':error})


def course_list(request):
    lessons = Curso.objects.all()
    return render(request,'lessons/lessons.html',{'lessons':lessons})








def course_detail(request,curso_id):
    curso = Curso.objects.get(pk=curso_id)
   # texto = LoqueAprenderas.objects.filter(curso=curso)
    texto = curso.loqueaprenderas_set.all()
    return render(request,'lessons/course_detail.html',{'curso':curso,'textos':texto})


stripe.api_key = settings.STRIPE_SECRET_KEY 

@login_required
def comprar_curso(request,curso_id):
    curso = Curso.objects.get(pk=curso_id)

    checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(curso.price) * 100,
                        "product_data": {
                            "name": curso.name,
                            "description": curso.description,
                            "images": [
                                f"{settings.BACKEND_DOMAIN}/{curso.thumbnail.url}"
                            ],
                        },
                    },
                    "quantity":1,
                }
            ],
            metadata={"curso_id":curso.id,'user_id':request.user.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL+str(curso.id),
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
   
    return redirect(checkout_session.url)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
            # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
            # Invalid signature
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        print("Payment successful")
       
        session = event["data"]["object"]
        curso_id=session['metadata']['curso_id']
        curso = Curso.objects.get(pk=curso_id)
        usuario_id = session['metadata']['user_id']
        email = session['customer_details']['email']
        usuarioo = User.objects.get(pk=usuario_id)

        compra = Compra(curso_comprado=curso,user=usuarioo)
        compra.save()
      

            

    return HttpResponse(status=200)
















    """ if request.method == "POST":
        cantidad = request.POST.get("cantidad")
        if request.user.is_authenticated and int(cantidad)==curso.price:
            user = request.user
            compra = Compra.objects.create(curso_comprado=curso,usuario=user)
            compra.save()
            return redirect("../../curso-detail/{}".format(curso.id))

            """




@login_required
@user_has_purchased_course
def course_access(request,curso_id):
    

    curso = Curso.objects.get(pk=curso_id)


   
    return render(request,'lessons/course_detail_paga.html',{'curso':curso})

@login_required
@user_has_purchased_course
def ver_video(request,leccion_id,curso_id):
    curso = Curso.objects.get(pk=curso_id)
    leccion = Leccion.objects.get(pk=leccion_id)
    return render(request,'lessons/ver_video.html',{'leccion':leccion,'curso':curso})




@login_required
def user_profile(request):
    usuario = request.user
    cursos = Compra.objects.filter(user=usuario)

    return render(request,'lessons/profile.html',{'cursos':cursos,'usuario':usuario})