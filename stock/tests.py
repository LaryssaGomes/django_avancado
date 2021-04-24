from django.test import TestCase
from stock.models import Product, TimestampableMixin, StockEntry
from django.test.testcases import SimpleTestCase
from django.contrib.auth.models import User
from django.urls.base import reverse
# Create your tests here.
class ProductTest(SimpleTestCase):# teste que não trabalha com banco de dados
    def test_value_initial_stock_field(self):# sempre iniciar o metodo com teste 
        product = Product()
        self.assertEquals(0, product.stock)
    
    def test_product_has_timestampable(self):# sempre iniciar o metodo com teste 
        product = Product()
        self.assertIsInstance(product, TimestampableMixin)

    def test_exception_when_stock_less_zero(self):# sempre iniciar o metodo com teste
        product = Product()
        with self.assertRaises(ValueError) as exception:
            product.stock = 10
            product.decrement(11)
        self.assertEquals('Sem estoque disponível', str(exception.exception))

class ProductDatabaseTest(TestCase):# mysql e postsql não usa teste de banco pq demora
    fixtures = ['data.json']
    def setUp(self):
        self.product = Product.objects.create(
            name= "Produto y",
            stock_max= 200,
            price_sale= 50.50,
            price_purchase= 25.25,
        )
    
    def test_product_save(self):# sempre iniciar o metodo com teste
        
        self.assertEquals('Produto y', self.product.name)
        self.assertEquals(0, self.product.stock)

    def test_if_user_exists(self):# sempre iniciar o metodo com teste
        user = User.objects.all().first()
        self.assertIsNone(user)


class StockEntryHttpTest(TestCase):
    fixtures = ['data.json']
    def test_list(self):# sempre iniciar o metodo com teste
        response = self.client.get('/stock_entries/') # get pq está lisntando a aplicação
        self.assertEquals(200, response.status_code)
        self.assertIn('Produto y', str(response.content))

    def test_create(self):# sempre iniciar o metodo com teste
        url = reverse('entries_create')
        self.client.post(url, {'project': 1, 'amount': 20})
        entry = StockEntry.objects.filter( product_id=1).first()
        self.assertIsNotNone(entry)
        self.assertEquals(31, entry.product.stock)