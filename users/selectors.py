from django.contrib.auth import get_user_model


User = get_user_model()


def get_user(**kwargs):
    return User.objects.filter(**kwargs).first()


def user_exists(**kwargs):
    return (
        User.objects.filter(**kwargs).exists(),
        User.objects.filter(**kwargs).first(),
    )
