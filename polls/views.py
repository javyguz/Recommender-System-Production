from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import render
import pandas as pd
import os
import json
from .template_tags.synopsis_algorithm import recommend
import json


def index(request):

    # Get data
    data = pd.read_csv(os.path.abspath("polls/static/tables/df_subset.csv"))

    if request.GET.get('mybtn'):

        # Get cosine similarity matrix
        sg = pd.read_csv(os.path.abspath("polls/static/tables/sg.csv"), index_col=0)

        # Send a list with recommendations as links to images
        rec = recommend(sg, data, title=request.GET.get('mytextbox'))["image_url"]

        rec_list = list(rec)
        context = {"Recommendation": rec_list,
                   "First": "false"}

        return render(request, 'pages/index.html', context)

    return render(request, 'pages/index.html', context={'data': list(data.title),
                                                        'recommendation': []})


def cf(request):

    return render(request, 'pages/cf.html')

