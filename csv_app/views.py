import csv

from django.http import HttpResponse

from ip_app import models


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    opts = models.IpData._meta
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in models.IpData.objects.all():
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
