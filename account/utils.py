import random
from django.utils.text import slugify


def slugify_instance_name(instance, save=False, new_username=None):
    print('hi')
    if new_username is not None:
        username = new_username
    else:
        username = slugify(f"{instance.first_name} {instance.last_name}")
    Klass = instance.__class__
    qs = Klass.objects.filter(username=username).exclude(id=instance.id)
    rand_int = random.randint(300_000, 500_000)
    if qs.exists():
        username = f'{username}-{rand_int}'
        return slugify_instance_name(instance, save=save, new_username=username)
    instance.username = username
    if save:
        instance.save()
    return instance

