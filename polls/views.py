from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import render
import pandas as pd
import os
from .template_tags.synopsis_algorithm import recommend


def index(request):
    if request.GET.get('mybtn'):
        data = pd.read_csv(os.path.abspath("polls/static/tables/df_subset.csv"))
        sg = pd.read_csv(os.path.abspath("polls/static/tables/sg.csv"), index_col=0)

        context = {"Recommendation": list(recommend(sg, data, title=request.GET.get('mytextbox'))["image_url"]),
                   "First": "false"}

        return render(request, 'pages/index.html', context)
    return render(request, 'pages/index.html')


def cf(request):

    return render(request, 'pages/cf.html')

