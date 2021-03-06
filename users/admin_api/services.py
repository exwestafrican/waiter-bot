from users.admin_api.selectors import get_role
from users.services import add_activity


def change_users_role(admin: object, user: object, new_role: str):
    old_group = user.groups.first()
    new_group = get_role(name=new_role)
    if old_group is not None and new_group is not None:
        old_group.user_set.remove(user)
        new_group.user_set.add(user)
        user.save()
        add_activity(
            admin,
            "{} changed {}'s role to {}".format(
                admin.first_name, user.first_name, new_role
            ),
        )
        return True
    else:
        add_activity(
            admin,
            "{} tried to change {}'s role to {}".format(
                admin.first_name, user.first_name, new_role
            ),
            success=False,
        )
        return False
