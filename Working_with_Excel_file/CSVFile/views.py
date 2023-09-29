from django.shortcuts import render
from traditional.models import StudentData
from django.http import HttpResponse
import time
import os
import csv

def GiveTemplate(request):
    if request.method == "POST":
        start = time.time()
        try:
            file = request.FILES['path']
            if not file.name.endswith('.csv'):
                return HttpResponse("Invalid file format. Please upload a CSV file.")

            data = []
            with open('./'+str(file.name)) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(StudentData(
                        name=row['first_name'],
                        email=row['email'],
                        Designation=row['Designation']
                    ))

            StudentData.objects.bulk_create(data)

            end = time.time()
            print('Time required to run:', (end - start) * 1000, "ms")
            return HttpResponse("Data inserted successfully.")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")

    if request.method == "GET":
        return render(request, "index.html")