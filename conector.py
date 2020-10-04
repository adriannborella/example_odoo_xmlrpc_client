import xmlrpc
from xmlrpc.client import ServerProxy
import unicodedata

class Conexion():
    user = ''
    password = ''
    url = ''
    database = ''
    uid = 0
    model = ''

    def __init__(self, data):
        self.user = data['user']
        self.password = data['password']
        self.url = data['url']
        self.database = data['db']
        self.login()

    def login(self):       
        common = ServerProxy('{}/xmlrpc/2/common'.format(self.url))             
        self.uid = common.authenticate(self.database, self.user, self.password, {})
        return self.uid

    def read(self, condiciones, campos):        
        registros = self._read_registro(condiciones, campos, self.model)
        return registros

    def write(self, campos, id):
        models = ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        models.execute_kw(self.database, self.uid, self.password, self.model, 'write', [[id], campos])
    
    def _read_registro(self,condiciones, campos, modelo):
        models = ServerProxy('{}/xmlrpc/2/object'.format(self.url))        
        registro =  models.execute_kw(self.database, self.uid, self.password, modelo, 'search_read',[condiciones], {'fields': campos })
        return registro
    