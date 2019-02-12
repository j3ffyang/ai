from django.http import HttpResponse

def start(request):
    return HttpResponse("CNC-Classifier server starting!")
