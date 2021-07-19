from django.test import TestCase
from django.urls import reverse
from factorizem.views import FactorizemView

class FactorizemTestCase(TestCase):
    def test_factorize_view_ok(self):
        resp = self.client.get(reverse('factorizem:index'))
        self.assertEqual(resp.status_code, 200)

    def test_factorize_post_valid_vals_ok(self):
        respFor5 = self.client.post(reverse('factorizem:index'),{'num': 5})
        self.assertEqual(respFor5.status_code, 200)
        self.assertContains(respFor5, "Factors for 5")
        self.assertContains(respFor5, "5 is a prime number")
        self.assertContains(respFor5, "<li>1</li>")
        self.assertContains(respFor5, "<li>5</li>")
        self.assertNotContains(respFor5, "Error")
        
        respFor10 = self.client.post(reverse('factorizem:index'),{'num': 10})
        self.assertEqual(respFor10.status_code, 200)
        self.assertContains(respFor10, "Factors for 10")
        self.assertNotContains(respFor10, "10 is a prime number")
        self.assertContains(respFor10, "<li>2</li>")
        self.assertContains(respFor10, "<li>5</li>")
        self.assertContains(respFor10, "<li>10</li>")
        self.assertNotContains(respFor10, "Error")

    def test_factorize_post_invalid_vals_ok(self):
        respForNegative3 = self.client.post(reverse('factorizem:index'),{'num': '-3'})
        self.assertEqual(respForNegative3.status_code, 200)
        self.assertNotContains(respForNegative3, "Factors for")
        self.assertNotContains(respForNegative3, "is a prime number")
        self.assertNotContains(respForNegative3, "<li>1</li>")
        self.assertContains(respForNegative3, "Error")
        self.assertContains(respForNegative3, "Please provide a positive integer.")

    def test_factorize_method_ok(self):
        # factorize 6
        factorListFor6 = FactorizemView.find_positive_factors(FactorizemView.as_view(), 1, 6)
        self.assertEqual(len(factorListFor6), 4)
        self.assertTrue(2 in factorListFor6)
        self.assertTrue(3 in factorListFor6)
        # factorize 1
        factorListFor1 = FactorizemView.find_positive_factors(FactorizemView.as_view(), 1, 1)
        self.assertEqual(len(factorListFor1), 1)
        # factorize 18
        factorListFor18 = FactorizemView.find_positive_factors(FactorizemView.as_view(), 1, 18)
        self.assertEqual(len(factorListFor18), 6)
        self.assertTrue(2 in factorListFor18)
        self.assertTrue(3 in factorListFor18)
        self.assertTrue(6 in factorListFor18)
        self.assertTrue(9 in factorListFor18)
        # factorize -8
        factorListForNeg = FactorizemView.find_positive_factors(FactorizemView.as_view(), 1, -8)
        self.assertEqual(len(factorListForNeg), 1)
        