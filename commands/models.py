from django.db import models

# Create your models here.


class Command(models.Model):
    name = models.CharField(
        max_length=15,
        help_text="commands are named like this e.g order, make_refund. no spaces allowed or special characters allowed",
        unique=True,
    )
    description = models.TextField(help_text="what does this command do")
    example = models.TextField(help_text="example usage of this command")

    def __str__(self):
        return "#{self.name}"

    @property
    def example_command_format(self):
        return "#example_{}".format(self.name)
