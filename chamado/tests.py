from django.test import TestCase, Client
from .models import Chamado, Cliente, Analista, Equipamento
from django.utils import timezone

class ChamadoTest(TestCase):

    def setUp(self):
        titulo = 'Problema com placa de video'
        tipo = Chamado.TIPO_DE_CHAMADO[0][0] #escolhendo incidente
        status = Chamado.STATUS_DE_CHAMADO[0][0] #escolhendo aberto
        cliente = Cliente.objects.create_user(username='cliente1', password='secret', endereco='rua tal')
        analista = Analista.objects.create_user(username='analista1', password='secret')
        equipamento = Equipamento.objects.create(descricao='Computador1', local='Rh')
        descricao = 'Computador não aparece video'
        abertura = timezone.now()

        self.chamado = Chamado.objects.create(
            titulo_chamado= titulo,
            tipo_chamado= tipo,
            status= status,
            cliente= cliente,
            equipamento= equipamento, 
            descricao= descricao,
            solucao = '',
            data_abertura= abertura,
        )

    def test_abrir_chamado(self):
        self.assertEqual(self.chamado.status, 'ABERTO' )
    
    def test_template_used(self):
        """Verifica se é o template correto que esta renderizando"""

        self.c = Client()

        self.assertTrue(
            self.c.login(
            username='cliente1',
            password='secret',
            )
        )

        response = self.c.post(
            '/', 
            username='cliente1',
            password='secret',
            follow=True,
        )
        self.assertTemplateUsed(response, 'chamado/chamados_list.html')

class LoginTest(TestCase):

    
    def setUp(self):
        self.credeciais_cliente = {
            'username': 'testcliente',
            'password': 'secret',
        }

        self.credeciais_analista = {
            'username': 'testanalista',
            'password': 'secret',
        }

        Cliente.objects.create_user(**self.credeciais_cliente)
        Analista.objects.create_user(**self.credeciais_analista)
    
   
    def test_login_Logout_cliente(self):
        """
        Teste de login para cliente
        """
        
        self.c = Client()
        self.assertTrue(self.c.login(**self.credeciais_cliente))

        """
        Teste de logout para cliente
        """

        self.assertTrue(self.c.logout)

    
    def test_login_Logout_analista(self):
        """
        Teste de login para analista
        """
        self.a = Client()
        self.assertTrue(self.a.login(**self.credeciais_analista))

        """
        Teste de logout para analista
        """

        self.assertTrue(self.a.logout)


    def test_redirect_login(self):
        """sempre que aceessar a pagina home tem que ser redirecionado para a 
        pagina de login"""
        self.c = Client()

        #verifica se foi redirecionado
        response = self.c.post('/', **self.credeciais_cliente, follow=False)
        self.assertEqual(response.status_code, 302)

        #verifica se uma pagina foi encontrada no final do redirecionamento
        response1 = self.c.post('/', **self.credeciais_cliente, follow=True)
        self.assertEqual(response1.status_code, 200)
   
