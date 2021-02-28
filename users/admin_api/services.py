from users.admin_api.selectors import get_role
from users.services import add_activity


def change_users_role(admin: object, user: object, new_role: str):

    group = get_role(name=new_role)
    print(group)
    if group is not None:
        user.groups.remove(group)
        new_group = get_role(name=new_role)
        user.groups.add(new_group)
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
