from django.shortcuts import render
from traditional.models import StudentData
from django.http import HttpResponse
import time
import pandas as pd

def GiveTemplate(request):
    if request.method == "POST":
        start = time.time()
        try:
            file = request.FILES['path']
            if not file.name.endswith('.xlsx'):
                return HttpResponse("Invalid file format. Please upload an Excel (.xlsx) file.")

            df = pd.read_excel(file)

            # Convert DataFrame to a list of dictionaries
            data = df.to_dict(orient='records')

            # Use bulk_create for batch insertion
            StudentData.objects.bulk_create(
                [StudentData(name=row['first_name'], email=row['email'], Designation=row['Designation']) for row in data]
            )

            end = time.time()
            print('Time required to run:', (end - start) * 1000, "ms")
            return HttpResponse("Data inserted successfully.")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")

    if request.method == "GET":
        return render(request, "index.html")







    '''def GiveTemplate(request):
    if request.method == "POST":
        start = time.time()
        try:
            file = request.FILES['path']
            if not file.name.endswith('.csv'):
                return HttpResponse("Invalid file format. Please upload a CSV file.")

            df = pd.read_csv(file)

            # Convert DataFrame to a list of dictionaries
            data = df.to_dict(orient='records')

            # Use bulk_create for batch insertion
            StudentData.objects.bulk_create(
                [StudentData(name=row['first_name'], email=row['email'], Designation=row['Designation']) for row in data]
            )

            end = time.time()
            print('Time required to run:', (end - start) * 1000, "ms")
            return HttpResponse("Data inserted successfully.")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")

    if request.method == "GET":
        return render(request, "index.html")'''
