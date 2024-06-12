from django.shortcuts import render
from django.views import View

# Create your views here.


def home(request):
    return render(request, "project/home.html")

class SubmitRecording(View):
    def get(self, request):
        return render(request, "project/submitrecording.html")
    def post(self, request):
        context = {}
        error_occurred = False
        error_message = ""
        result = ""
        if error_occurred:
            context["error_message"] = error_message
        else:
            context["result"] = result
        return render(request, "project/result.html", context)
