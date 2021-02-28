from users.models import ActivityLog


def add_activity(user, action, success=True):
    return ActivityLog.objects.create(user=user, action=action, success=success)
