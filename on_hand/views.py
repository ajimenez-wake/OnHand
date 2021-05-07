from django.shortcuts import redirect

def homepage(request):
    return redirect('camera_list_view')
