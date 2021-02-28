from django.contrib.auth.models import Group


def get_role(**args):
    return Group.objects.filter(**args).first()