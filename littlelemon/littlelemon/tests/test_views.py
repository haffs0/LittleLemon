from django.test import TestCase

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="ChoCream", price=80, inventory=100)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer_menu = MenuSerializer(menus, many=True)
        self.assertEqual(len(serializer_menu), 2)