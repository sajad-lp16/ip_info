from django.utils.translation import ugettext_lazy as _
from django.db import models

from ip_app.tasks import insert_ip_data


class IpData(models.Model):
    ip = models.GenericIPAddressField(
        verbose_name=_('ip')
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('city')
    )
    region = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('region')
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('country')
    )
    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('location')
    )
    organization = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=_('organization')
    )
    timezone = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        verbose_name=_('timezone')
    )
    postal = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    host_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    bogon = models.BooleanField(
        blank=True,
        null=True
    )
    create_time = models.DateTimeField(
        auto_now_add=True
    )
    update_time = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = _('ip data')
        verbose_name_plural = _('ip data')
        db_table = 'ip_data'

    def __str__(self):
        return self.ip.__str__()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)
        if not all([self.city, self.region, self.country, self.location]):
            insert_ip_data.delay(self.ip)
