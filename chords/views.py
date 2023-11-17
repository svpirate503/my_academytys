from django.shortcuts import render
from django.http import HttpResponse





grados = {"c": 1, "d": 2, "e": 3, "f": 4, "g": 5, "a": 6, "b": 7}

def cambiar_tonalidad(request):
    nuevos_acordes=""
    acordes_de_la_cancion = ""
    rango = ""
    if request.method == 'POST':
        acordes_de_la_cancion = int(request.POST.get('numero1'))
        rango = range(1,acordes_de_la_cancion+1)
  
        tonalidad_original = request.POST.get('tonoreal').lower()
        nueva_tonalidad = request.POST.get('new_tone').lower()
       
        # Calcula la diferencia entre los grados de las dos tonalidades
        try:
            diferencia_de_tonalidad = grados[nueva_tonalidad] - grados[tonalidad_original]
        except KeyError:
            return HttpResponse("Invalido parametro")
       

        nuevos_acordes = []

        for i in range(1, acordes_de_la_cancion + 1):
            
            acorde = request.POST.get(f'acorde_{i}').lower()
           

            nuevo_grado = (grados[acorde] + diferencia_de_tonalidad - 1) % 7 + 1
            nuevo_acorde = [k for k, v in grados.items() if v == nuevo_grado][0]
            nuevos_acordes.append(nuevo_acorde)

        result = "Nuevos acordes en la tonalidad " + nueva_tonalidad + ": " + " ".join(nuevos_acordes)
        return HttpResponse(result)
    else:
        return render(request, 'chords/changue_tone.html',{'acordes_de_la_cancion':rango})





               



            
        
                
            

        """ if chord:
                        acorde_original = chord.lower()
                        nuevo_grado = (grados[acorde_original] + diferencia_de_tonalidad - 1) % 7 + 1
                        nuevo_acorde = [k for k, v in grados.items() if v == nuevo_grado][0]
                        nuevos_acordes.append(nuevo_acorde)

                        """

                   

                
            

               

                    
                    
            
                    




    return render(request,'changue_tone.html',{'rango':rango,'acordes':nuevos_acordes})
