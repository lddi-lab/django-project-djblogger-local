import factory
from django.contrib.auth.models import User

from djblogger.blog.models import Post


class UserFactor(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactor)
    content = "x"
    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)
