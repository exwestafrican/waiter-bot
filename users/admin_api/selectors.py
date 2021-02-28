from django.contrib.auth.models import Group


def get_role(**args):
    return Group.objects.get(**args)