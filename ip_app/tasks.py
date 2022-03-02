from requests import get

from django.conf import settings

from celery import shared_task

from . import models


@shared_task
def insert_ip_data(ip):
    ip_add = settings.IP_INFO_ADDRESS + ip
    response = get(ip_add)
    if response.status_code == 200:
        data = response.json()
        data.pop('readme', None)
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        loc = data.get('loc')
        org = data.get('org')
        timezone = data.get('timezone')
        postal = data.get('postal')
        host_name = data.get('host_name')
        bogon = data.get('bogon')
        obj, _ = models.IpData.objects.get_or_create(
            ip=ip
        )
        obj.city = city
        obj.region = region
        obj.country = country
        obj.location = loc
        obj.organization = org
        obj.timezone = timezone
        obj.postal = postal
        obj.host_name = host_name
        obj.bogon = bogon
        obj.save()
        return 'Successful'
    return 'Failed'
