from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from django.views.generic import TemplateView
import plotly.offline as opy
import plotly.graph_objs as go
import plotly.express as px
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

# Scatterplot
class ScatterPlotView(TemplateView):
    template_name = 'iris/scatterplot.html'

    def get_context_data(self, **kwargs):
        context = super(ScatterPlotView, self).get_context_data(**kwargs)
        df = pd.DataFrame(IrisData.objects.all().values())
        df['species_id'] = df['species_id'].apply(lambda s: specie_name(s))
        df.drop(['id'], axis=1, inplace=True)
        df.rename({'species_id': 'species'}, axis=1, inplace=True)
        x = df['petal_length']
        y = df['petal_width']
        color = df['species']
        correlation = x.corr(y)
        fig = px.scatter(df, x=x, y=y, color="species")
        fig.update_traces(marker=dict(size=12,
                                      line=dict(width=2, color='DarkSlateGrey')),
                          selector=dict(mode='markers'))
        div = opy.plot(fig, auto_open=False, output_type="div")
        context['graph'] = div
        context['corr'] = correlation
        return context

class Scatter3DPlotView(TemplateView):
    template_name = 'iris/scatterplot3D.html'

    def get_context_data(self, **kwargs):
        context = super(Scatter3DPlotView, self).get_context_data(**kwargs)
        df = pd.DataFrame(IrisData.objects.all().values())
        df['species_id'] = df['species_id'].apply(lambda s: specie_name(s))
        df.drop(['id'], axis=1, inplace=True)
        df.rename({'species_id': 'species'}, axis=1, inplace=True)
        x = df['petal_length']
        y = df['petal_width']
        correlation = x.corr(y)
        fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
        div = opy.plot(fig, auto_open=False, output_type="div")
        context['graph'] = div
        context['corr'] = correlation
        return context

class HistogramView(TemplateView):
    template_name = 'iris/histograms.html'

    def get_context_data(self, **kwargs):
        context = super(HistogramView, self).get_context_data(**kwargs)
        df = pd.DataFrame(IrisData.objects.all().values())
        df['species_id'] = df['species_id'].apply(lambda s: specie_name(s))
        df.drop(['id'], axis=1, inplace=True)
        df.rename({'species_id': 'species'}, axis=1, inplace=True)
        # histograms
        fig1 = px.histogram(df, x="sepal_length", color="species")
        graph1 = opy.plot(fig1, auto_open=False, output_type="div")
        context['graph1'] = graph1
        fig2 = px.histogram(df, x="sepal_width", color="species")
        graph2 = opy.plot(fig2, auto_open=False, output_type="div")
        context['graph2'] = graph2
        fig3 = px.histogram(df, x="petal_length", color="species")
        graph3 = opy.plot(fig3, auto_open=False, output_type="div")
        context['graph3'] = graph3
        fig4 = px.histogram(df, x="petal_width", color="species")
        graph4 = opy.plot(fig4, auto_open=False, output_type="div")
        context['graph4'] = graph4
        return context

class BoxPlotView(TemplateView):
    template_name = 'iris/histograms.html'

    def get_context_data(self, **kwargs):
        context = super(BoxPlotView, self).get_context_data(**kwargs)
        df = pd.DataFrame(IrisData.objects.all().values())
        df['species_id'] = df['species_id'].apply(lambda s: specie_name(s))
        df.drop(['id'], axis=1, inplace=True)
        df.rename({'species_id': 'species'}, axis=1, inplace=True)
        # histograms
        fig1 = px.box(df, x="sepal_length", color="species")
        graph1 = opy.plot(fig1, auto_open=False, output_type="div")
        context['graph1'] = graph1
        fig2 = px.box(df, x="sepal_width", color="species")
        graph2 = opy.plot(fig2, auto_open=False, output_type="div")
        context['graph2'] = graph2
        fig3 = px.box(df, x="petal_length", color="species")
        graph3 = opy.plot(fig3, auto_open=False, output_type="div")
        context['graph3'] = graph3
        fig4 = px.box(df, x="petal_width", color="species")
        graph4 = opy.plot(fig4, auto_open=False, output_type="div")
        context['graph4'] = graph4
        return context

class DensityContourView(TemplateView):
    template_name = 'iris/density.html'

    def get_context_data(self, **kwargs):
        context = super(DensityContourView, self).get_context_data(**kwargs)
        df = pd.DataFrame(IrisData.objects.all().values())
        df['species_id'] = df['species_id'].apply(lambda s: specie_name(s))
        df.drop(['id'], axis=1, inplace=True)
        df.rename({'species_id': 'species'}, axis=1, inplace=True)
        # density contours
        fig1 = px.density_contour(df, x="sepal_length", y="sepal_width")
        fig1.update_traces(contours_coloring="fill", contours_showlabels=True)
        graph1 = opy.plot(fig1, auto_open=False, output_type="div")
        context['graph1'] = graph1
        fig2 = px.density_contour(df, x="petal_length", y="petal_width")
        fig2.update_traces(contours_coloring="fill", contours_showlabels=True)
        graph2 = opy.plot(fig2, auto_open=False, output_type="div")
        context['graph2'] = graph2
        return context



