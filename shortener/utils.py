import random
import string

from django.conf import settings


def generate_code(size=settings.SHORTCODE_MIN, codes=string.ascii_letters + string.digits):
    return ''.join(random.choice(codes) for _ in range(size))


def create_shortcode(instance, size=settings.SHORTCODE_MIN):
    new_code = generate_code(size=size)
    code_exists = instance.__class__.objects.filter(short_code=new_code).exists()
    if code_exists:
        return create_shortcode(size=size)
    return new_code
