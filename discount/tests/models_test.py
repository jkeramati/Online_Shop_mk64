from django.test import TestCase
from discount.models import Discount, OffCode


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = Discount.objects.create(type_disc='price', value=10)
        self.discount2 = Discount.objects.create(type_disc='percent', value=20)

    def test1_profit_100(self):
        self.assertEqual(self.discount1.profit(100), 10)
        self.assertEqual(self.discount2.profit(100), 20)

    def test1_profit_20(self):
        self.assertEqual(self.discount1.profit(20), 10)
        self.assertEqual(self.discount2.profit(20), 4)

    def test1_profit_10(self):
        self.assertEqual(self.discount1.profit(10), 0)
        self.assertEqual(self.discount2.profit(10), 2)


class OffCodeTest(TestCase):
    def setUp(self) -> None:
        self.off_code1 = OffCode.objects.create(code='spring', type_disc='price', value=20)
        self.off_code2 = OffCode.objects.create(code='summer', type_disc='percent', value=30)

    def test1_profit_100(self):
        self.assertEqual(self.off_code1.profit(100), 20)
        self.assertEqual(self.off_code2.profit(100), 30)

    def test1_profit_40(self):
        self.assertEqual(self.off_code1.profit(40), 20)
        self.assertEqual(self.off_code2.profit(40), 12)

    def test1_profit_20(self):
        self.assertEqual(self.off_code1.profit(20), 0)
        self.assertEqual(self.off_code2.profit(20), 6)