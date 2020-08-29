from django.shortcuts import render
from .models import Csv
from .forms import CsvForm
import csv
import pandas
from Iris.models import Species, IrisData

# Create your views here.
def data_import_view(request):
    # Initial values
    error_message = None
    success_message = None

    # instantiate the form
    form = CsvForm(request.POST or None, request.FILES or None)
    # check for validity and save
    if form.is_valid():
        form.save()
        # reset the form
        form = CsvForm()
        # get data from form
        csv_file = Csv.objects.get()
        with open(csv_file.filename.path, "r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                # Populate species based on the last column
                specie, created = Species.objects.get_or_create(species=row[4])
                # Populate the IrisData based on the other array columns
                IrisData.objects.create(
                    species=specie,
                    sepal_length=float(row[0]),
                    sepal_width=float(row[1]),
                    petal_length=float(row[2]),
                    petal_width=float(row[3])
                )

        success_message = "File successfully uploaded"

    else:
        error_message = "There is a problem with the upload"

    context = {
        'form': form,
        'success': success_message,
        'failure': error_message,
    }

    return render(request, "csvs/csv_upload.html", context)
