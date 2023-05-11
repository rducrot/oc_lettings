from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestViews:

    def test_index(self, client):
        sut = client.get(reverse('index'))
        assert sut.status_code == 200
        assert b'<h1 class="w-100 text-center mt-5">Welcome to Holiday Homes</h1>' in sut.content
