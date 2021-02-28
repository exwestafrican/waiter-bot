from django.db import models


class TimeStampMixin(models.Model):
    "determins when model was created and edited"
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """
        declearing abstract class allows class attributes to be used as fields
        when inherited
        """

        abstract = True

    def __str__(self):
        return self.name