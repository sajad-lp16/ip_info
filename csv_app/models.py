from django.core.validators import FileExtensionValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .tasks import add_ips


class CsvFile(models.Model):
    csv_file = models.FileField(
        verbose_name=_('csv file'),
        validators=[FileExtensionValidator(allowed_extensions=['csv'])]
    )
    create_time = models.DateTimeField(
        auto_now_add=True
    )
    update_time = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.create_time.__str__()

    class Meta:
        verbose_name = _('import csv file')
        verbose_name_plural = _('import csv files')
        db_table = 'csv_files'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(CsvFile, self).save(force_insert=False, force_update=False, using=None,
                                  update_fields=None)

        add_ips.delay(self.create_time)
