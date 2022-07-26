from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render
import numpy as np
import pandas as pd
import os
from .template_tags.synopsis_algorithm import recommend


def index(request):
    if request.GET.get('mybtn'):
        data_path = os.path.abspath("polls/static/tables/data_.csv")
        data = pd.read_csv(data_path)

        sg_path_1 = os.path.abspath("polls/static/tables/sg1.npy")
        sg1 = np.load(sg_path_1)

        sg_path_2 = os.path.abspath("polls/static/tables/sg2.npy")
        sg2 = np.load(sg_path_2)

        sg_path_3 = os.path.abspath("polls/static/tables/sg3.npy")
        sg3 = np.load(sg_path_3)

        sg_path_4 = os.path.abspath("polls/static/tables/sg4.npy")
        sg4 = np.load(sg_path_4)

        sg_path_5 = os.path.abspath("polls/static/tables/sg5.npy")
        sg5 = np.load(sg_path_5)

        sg = np.concatenate([sg1, sg2, sg3, sg4, sg5])

        context = {"Recommendation": list(recommend(sg, data, title=request.GET.get('mytextbox'))["image"]),
                   "First": "false"}

        return render(request, 'pages/index.html', context)
    return render(request, 'pages/index.html')


def cf(request):

    return render(request, 'pages/cf.html')

