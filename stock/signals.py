from django.db.models.signals import post_save, pre_save
from stock.emails import StockGreaterMax
from stock.models import StockEntry
from django_avancado.settings import MAIL_STOCK_BOSS
from django.dispatch.dispatcher import Signal

product_stock_changed = Signal()
# receptor
# o elemento created e boleano false: conteudo atualizado e true para conteudo criado
def increment_stock(sender, created , instance, **kwargs):
    if created is True:
        product = instance.product
        product.stock = product.stock + instance.amount
        product.save()
        product_stock_changed.send(sender=None, instance=product)

def send_mail_stock_max(sender, instance, **kwargs):
    if instance.stock > instance.stock_max:
        StockGreaterMax(instance).send(MAIL_STOCK_BOSS)

def test_save(sender, created , instance, **kwargs):
    print(created)

def test_pre_save(sender, instance, **kwargs):
    print("test_pre_save")

product_stock_changed.connect(send_mail_stock_max, sender=None)
#post_save.connect(increment_stock, sender=StockEntry)
post_save.connect(test_save, sender=StockEntry)
pre_save.connect(test_pre_save, sender=StockEntry)
#pre_delete - antes de excluir
#post_delete - depois de excluir
#m2m_changed - quando há alteração no relacionamento muitos para muitos
#request_started - quando um requisição é recebida
#request_finished - quando tem uma resposta HTTP para ser enviada