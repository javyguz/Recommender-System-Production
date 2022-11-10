from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import render
import pandas as pd
import os
import json
from .template_tags.synopsis_algorithm import recommend
import json


def index(request):

    # Get data
    #data = pd.read_csv(os.path.abspath("polls/static/tables/df_subset.csv"))
    df1 = pd.read_csv(os.path.abspath("polls/static/tables/df1.csv"))
    df2 = pd.read_csv(os.path.abspath("polls/static/tables/df2.csv"))
    df3 = pd.read_csv(os.path.abspath("polls/static/tables/df3.csv"))
    df4 = pd.read_csv(os.path.abspath("polls/static/tables/df4.csv"))
    df5 = pd.read_csv(os.path.abspath("polls/static/tables/df5.csv"))

    # Merge data
    data = pd.concat([df1, df2, df3, df4, df5])

    if request.GET.get('mybtn'):

        if request.GET.get('mytextbox') != "":

            # Get cosine similarity matrix
            sg = pd.read_csv(os.path.abspath("polls/static/tables/sg.csv"), index_col=0)

            # Send a list with recommendations as links to images
            print(request.GET.get('mytextbox'))
            rec = recommend(sg, data, title=request.GET.get('mytextbox'))["image_url"]

            rec_list = list(rec)
            context = {"Recommendation": rec_list,
                    "First": "false",
                    "data": list(data.title)}

            return render(request, 'pages/index.html', context)

        else:
            return render(request, 'pages/index.html', context={'data': list(data.title),
                                                        'Recommendation': [],
                                                        'First': "True"})

    return render(request, 'pages/index.html', context={'data': list(data.title),
                                                        'Recommendation': [],
                                                        'First': "True"})


def cf(request):

    return render(request, 'pages/cf.html')

