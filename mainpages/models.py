from django.db import models
from cloudinary.models import CloudinaryField


class CertificateModel(models.Model):
    """Model definition for CertificateModel."""

    certificate_image = CloudinaryField('certificate image')

    class Meta:
        """Meta definition for CertificateModel."""

        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        """Unicode representation of CertificateModel."""
        return str(self.certificate_image)


class WorkModel(models.Model):
    """Model definition for WorkModel."""

    work_image = CloudinaryField('work image')

    class Meta:
        """Meta definition for WorkModel."""

        verbose_name = 'Work Image'
        verbose_name_plural = 'Work Images'

    def __str__(self):
        """Unicode representation of WorkModel."""
        return str(self.work_image)
