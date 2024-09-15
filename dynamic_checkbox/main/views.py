from django.shortcuts import render
from django.http import JsonResponse
from .models import checkbox

def home(request):
    choices=checkbox.objects.all()
    return render(request, "main/home.html",{'choices':choices})

def update_checkbox(request):
    if request.method=="POST":
        level = int(request.POST.get('level'))
        choice = request.POST.get('choice')
        is_checked = request.POST.get('is_checked') == 'true'
        print(level)
        if is_checked:

            checkbox.objects.update_or_create( #if checkbox is checked, create or update the choice
                level=level,
                defaults={'choice':choice}
            )

            checkbox.objects.filter(level__gt=level).delete()   #delete all levels > current level

            return JsonResponse({'status':'success', 'action': "updated", 'level': level, 'choice': choice})
       
        else: 
            #if checkbox is unchecked, delete current and any greater levels 
            checkbox.objects.filter(level__gte=level).delete()     

            return JsonResponse({'status':'success', 'action': "deleted", 'level': level})
        
    return JsonResponse({'status':'error', 'action': "invalid request"})

def clear_checkboxes(request):
    if request.method == "DELETE":
        # Clear all checkboxes from the database-> this is used when the page is refreshed
        checkbox.objects.all().delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)
