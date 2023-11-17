from django.db import models

from django.contrib.auth.models import User 



class Curso(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnail") #imagenes de portada en el curso
    video = models.FileField(upload_to="welcome_videos") #Videos de presentacion del curso
    price = models.DecimalField(max_digits=7,decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


    

    def __str__(self):
        return self.name 
    
class LoqueAprenderas(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    
class Compra(models.Model):
    curso_comprado = models.ForeignKey(Curso,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer_email = models.EmailField() 
   

class Capitulo(models.Model):
    title = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    video_capitulo = models.FileField(upload_to="presentacion_del_capitulo")

    def __str__(self):
        return self.title



class Leccion(models.Model):
    leccion_name = models.CharField(max_length=100)
    capitulo = models.ForeignKey(Capitulo,on_delete=models.CASCADE)
    content = models.FileField(upload_to="lecciones") #videos de cada leccion
    video_url = models.URLField()

    def __str__(self):
        return self.leccion_name


class Tutoriales(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="thumbnail")
    video = models.FileField(upload_to="tutoriales")
    description = models.TextField()


    def __str__(self):
        return self.title
    

class comentarios(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    avatar = models.ImageField(upload_to="avatars")

    def __str__(self):
        return self.name