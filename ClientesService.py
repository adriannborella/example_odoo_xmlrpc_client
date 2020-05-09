from conector import Conexion8, Conexion11
import unicodedata

class PartnerService(Conexion8):
    def __init__(self):        
        self.model = 'res.partner'
        self.serviceCliente = ClienteService()
        super(PartnerService, self).__init__()
    
    def listarPartners(self):
        partners = self.read([],['name', 'id', 'phone', 'mobile', 'email', 'website'])
        for reg in partners:
            self.serviceCliente.sincronizarcliente(reg)

    def getOne(self, nombre):
        one = self.read(['name','=', nombre], ['name', 'id'])
        return one
    

class ClienteService(Conexion11):
    def __init__(self):        
        self.model = 'asw.cliente'
        super(ClienteService, self).__init__()
    
    def sincronizarcliente(self, cliente):
        print("Sincronizando datos", cliente)
        nombre_busqueda = self.chau_acentos(cliente['name'])
        acliente = self.read([['cli_razon_social','=', nombre_busqueda]],['cli_razon_social','id', 'cli_nro_doc'])
        if(len(acliente) > 0):
            update = {
                'cli_mail': cliente['email'],
                'cli_telefono': cliente['phone'],
                'cli_celular': cliente['mobile']
            }
            self.write(update, acliente[0]['id'])


if __name__ == "__main__":   
    service = PartnerService()
    service.listarPartners()