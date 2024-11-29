from profiles.models import Profile


def get_user_obj():
    user_object = Profile.objects.first()
    return user_object
