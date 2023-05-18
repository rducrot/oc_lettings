from django.urls import reverse
import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.address = Address.objects.create(
            number=4,
            street="Main Street",
            city="New York",
            state="NY",
            zip_code=11000,
            country_iso_code="USA")
        self.letting = Letting.objects.create(
            title="Studio NY",
            address=self.address)

    def test_index(self, client):
        sut = client.get(reverse('lettings:index'))
        assert sut.status_code == 200
        assert b'<h1>Lettings</h1>' in sut.content

    def test_letting(self, client):
        sut = client.get(reverse('lettings:letting', kwargs={'letting_id': 1}))
        assert sut.status_code == 200
        assert b'<h1>Studio NY</h1>' in sut.content
