from django.shortcuts import render
from .models import Photo
from .forms import PhotoForm
from .customVision import customVisionPrediction

# Create your views here.
def home(request):


    return render(request, "home.html")

def customVision(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            image = Photo.objects.last()
            url = image.image.url
            predictionResults = customVisionPrediction(url)
            # results = ""
            # for prediction in predictionResults.predictions:
            #     # print("\t" + prediction.tag_name +
            #     #       ": {0:.2f}%".format(prediction.probability * 100))
            #     results += f"\n{prediction.tag_name}: {str(prediction.probability*100)}"

            context = {'form': PhotoForm(), 'form_class': PhotoForm, 'results': predictionResults}
            return render(request, "customVision.html", context)
    else:
        form = PhotoForm()
        form_class = PhotoForm

    context = {'form' : form, 'form_class': form_class}
    return render(request, "customVision.html", context)