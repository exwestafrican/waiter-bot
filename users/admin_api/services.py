from users.admin_api.selectors import get_role


def change_users_role(user: object, new_role: str, old_role=None):
    old_role = user.groups.first().name if old_role is None else old_role
    group = get_role(name=old_role)
    user.groups.remove(group)
    new_group = get_role(name=new_role)
    user.groups.add(new_group)
    return True
