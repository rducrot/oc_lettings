from django.contrib.auth.models import User
from django.urls import reverse
import pytest

from profiles.models import Profile


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.user = User.objects.create_user(
            username='4meRomance',
            password='Abc1234!',
            email='mail@mail.com'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Berlin',
        )

    def test_index(self, client):
        sut = client.get(reverse('profiles:index'))
        assert sut.status_code == 200
        assert b'<h1 class="w-100 text-center mt-5">Profiles</h1>' in sut.content

    def test_profile(self, client):
        sut = client.get(reverse('profiles:profile', kwargs={'username': '4meRomance'}))
        assert sut.status_code == 200
        assert b'<h1 class="w-100 text-center mt-5">4meRomance</h1>' in sut.content
