import xmlrpc
from xmlrpc.client import ServerProxy
import unicodedata

class Conexion():
    usuario = ''
    password = ''
    url = ''
    database = ''
    uid = 0
    model = ''

    def __init__(self, data):
        self.usuario = data['usuario']
        self.password = data['password']
        self.url = data['url']
        self.database = data['db']
        self.login()

    def login(self):       
        common = ServerProxy('{}/xmlrpc/2/common'.format(self.url))             
        self.uid = common.authenticate(self.database, self.usuario, self.password, {})
        return self.uid

    def read(self, condiciones, campos):        
        registros = self._leer_registro(condiciones, campos, self.model)
        return registros

    def write(self, campos, id):
        models = ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        models.execute_kw(self.database, self.uid, self.password, self.model, 'write', [[id], campos])
    
    def _leer_registro(self,condiciones, campos, modelo):
        models = ServerProxy('{}/xmlrpc/2/object'.format(self.url))        
        registro =  models.execute_kw(self.database, self.uid, self.password, modelo, 'search_read',[condiciones], {'fields': campos })
        return registro
    
    def chau_acentos(self, s):
        nvalor = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
        return nvalor.upper()

class Conexion8(Conexion):
    def __init__(self):
        data_8 = {
            'usuario' : 'admin',
            'password': 'AJDN2576tft',
            'url': 'http://ranchu.anacsoft.com',
            'db' : 'ranchu_restaurada'
        }        
        super(Conexion8, self).__init__(data_8)

class Conexion11(Conexion):
    def __init__(self):
        data11 = {
            'usuario' : 'administrador_anac',
            'password': 'Fi947SM51ta',
            'url': 'http://ranchu2.anacsoft.com',
            'db' : 'ranchu11'
        }      
        super(Conexion11, self).__init__(data11)