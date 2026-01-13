def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

def is_admin(user):
    return user.is_superuser