from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from .models import Species, IrisData
from .utils import specie_name

# Create your views here.
def TableView(request):
    # get the Iris Data and change species_id to specie
    df = pd.DataFrame(IrisData.objects.all().values())
    df['species_id'] = df['species_id'].apply(lambda s: specie_name(s))
    df.drop(['id'], axis=1, inplace=True)
    df.rename({'species_id': 'species'}, axis=1, inplace=True)


    context = {
        'df': df,
    }
    return render(request, 'iris/table.html', context)

