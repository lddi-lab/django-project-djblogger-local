import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_return(self, post_factory):
        post = post_factory(title="post-test")
        assert post.__str__() == "post-test"
