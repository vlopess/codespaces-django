from rest_framework import viewsets
from products.models import Produto
from products.api.serializers import ProdutoSerializer

class ProdutoListCreateView(viewsets.ModelViewSet):
    queryset = Produto.objects.all() 
    serializer_class = ProdutoSerializer
