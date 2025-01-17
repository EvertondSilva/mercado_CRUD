from django.db import models

class Produto(models.Model):
    codigo_produto = models.BigAutoField(auto_created=True, primary_key=True)
    produto = models.CharField(max_length= 100, null=False, blank= False)
    codigo_de_barrar = models.CharField(max_length= 100, null=False, blank= False)
    valor_de_venda = models.FloatField(null=False, blank= False)
    quantidade_em_estoque = models.IntegerField(null=False, blank= False, default=0)
    valor_compra = models.FloatField(null=False, blank= False)
    data_cadastro = models.DateField(auto_now_add=True, null=False, blank= False)

class Vendas(models.Model):
    codigo_venda = models.BigAutoField(auto_created=True, primary_key=True)
    produto_venda = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False, blank= False)
    data_venda = models.DateField(auto_now_add=True, null=False, blank= False)
    quantidade_venda = models.IntegerField(null=False, blank= False)
    cliente = models.CharField(max_length= 100, null=False, blank= False)


class Compra(models.Model):
    codigo_compra = models.BigAutoField(auto_created=True, primary_key=True)
    produto_compra = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False, blank= False)
    quantidade_compra = models.IntegerField(null=False, blank= False)
    fornecedor = models.CharField(max_length= 100, null=False, blank= False)
    data_compra = models.DateField(auto_now_add=True, null=False, blank= False)
