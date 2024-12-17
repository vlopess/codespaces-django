import unittest
from unittest.mock import patch
from rest_framework.test import APIClient
from products.models import Produto
from products.api.serializers import ProdutoSerializer
from rest_framework.utils.serializer_helpers import ReturnList

class ProductAPITest(unittest.TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.product = Produto.objects.create(
                                        nome='Teste Produto',
                                        descricao='Teste Descrição', 
                                        preco=100.0,
                                        quantidade=2
                                    )
        
    @patch("products.api.views.Produto.objects.all")
    def test_get_product_list(self, mock_all):
        mock_all.return_value = [self.product]

        response = self.client.get('/api/produto/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 13)
        self.assertEqual(type(response.data), ReturnList)
        self.assertEqual(response.data[0]["nome"], "Arroz")


    