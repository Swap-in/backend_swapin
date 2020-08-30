from django.db import models

TYPE_STATUS = [
        ("ACTIVE","ACTIVE"),
        ("INACTIVE","INACTIVE")
        ]

class SwapinModel(models.Model):
    created_at = models.DateTimeField(
        'created at', 
        auto_now_add=True,
        help_text='Date time on wich object was created.'
    )

    updated_at = models.DateTimeField(
        'modified at', 
        auto_now=True,
        help_text='Date time on wich object was last modified.'
    )

    status = models.CharField(max_length=8,choices=TYPE_STATUS)

    class Meta:
        """Meta option."""
        abstract = True