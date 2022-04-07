from django.test import TestCase
from product.models import Discount, OffCode


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = Discount.objects.create(type_disc='price', value=10)
        self.discount2 = Discount.objects.create(type_disc='percent', value=20)

    def test1_profit_100(self):
        self.assertEqual(self.discount1.profit(100), 10)
        self.assertEqual(self.discount2.profit(100), 20)

    def test2_profit_20(self):
        self.assertEqual(self.discount1.profit(20), 10)
        self.assertEqual(self.discount2.profit(20), 4)

    def test3_profit_10(self):
        self.assertEqual(self.discount1.profit(10), 0)
        self.assertEqual(self.discount2.profit(10), 2)

    def test_is_delete(self):
        self.discount1.delete()
        self.discount2.delete()
        self.assertIn(self.discount1, Discount.objects.get_all().filter(is_delete=True))
        self.assertIn(self.discount2, Discount.objects.get_all().filter(is_delete=True))
        print(Discount.objects.get_all())

    def test_undelete(self):
        self.discount1.delete()
        self.discount2.delete()
        self.discount1.undelete()
        self.discount2.undelete()
        self.assertIn(self.discount1, Discount.objects.get_all())
        self.assertIn(self.discount2, Discount.objects.get_all())
        print(Discount.objects.get_all())

    def test_is_active(self):
        self.assertIn(self.discount1, Discount.objects.all().filter(is_active=True))
        self.assertIn(self.discount2, Discount.objects.all().filter(is_active=True))
        print(Discount.objects.get_all())

    def test_deactive(self):
        self.discount1.deactivate()
        self.discount2.deactivate()
        self.assertIn(self.discount1, Discount.objects.all().filter(is_active=False))
        self.assertIn(self.discount2, Discount.objects.all().filter(is_active=False))
        print(Discount.objects.all().filter(is_active=True))

    def test_str(self):
        self.assertEqual(self.discount1.__str__(), 'type of discount: price with 10 value')
        self.assertEqual(self.discount2.__str__(), 'type of discount: percent with 20 value')


class OffCodeTest(TestCase):
    def setUp(self) -> None:
        self.off_code1 = OffCode.objects.create(code='spring', type_disc='price', value=20)
        self.off_code2 = OffCode.objects.create(code='summer', type_disc='percent', value=30)

    def test4_profit_100(self):
        self.assertEqual(self.off_code1.profit(100), 20)
        self.assertEqual(self.off_code2.profit(100), 30)

    def test5_profit_40(self):
        self.assertEqual(self.off_code1.profit(40), 20)
        self.assertEqual(self.off_code2.profit(40), 12)

    def test6_profit_20(self):
        self.assertEqual(self.off_code1.profit(20), 0)
        self.assertEqual(self.off_code2.profit(20), 6)
