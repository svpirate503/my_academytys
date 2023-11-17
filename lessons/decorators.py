from functools import wraps 
from django.http import HttpResponseForbidden


def user_has_purchased_course(view_function):
    @wraps(view_function)
    def _wrapped_view(request,*args,**kwargs):
        curso_id = kwargs.get("curso_id")
        if request.user.compra_set.filter(curso_comprado=curso_id).exists():
            return view_function(request,*args,**kwargs)
        else:
            return HttpResponseForbidden("No tienes acceso a este curso")
    return _wrapped_view