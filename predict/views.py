from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "index.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def options(request):
    return render(request, "options.html")

def prediction(request):
    return render(request, "prediction.html")

def monitor(request):
    return render(request, "monitor.html")

def apple(request):
    #file = request.files.get('upload')
    #model= keras.models.load_model("model_vgg19(apple).h5")
    name=""
    p_affected=0
    return render(request, "prediction.html", name, p_affected)

def im_upload(request):
    return render(request, "im_upload.html")