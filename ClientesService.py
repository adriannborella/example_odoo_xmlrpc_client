from conector import Conexion
import unicodedata

class PartnerService(Conexion):
    def __init__(self):        
        self.model = 'res.partner'      
        data = {
            'user' : 'read',
            'password' : 'read!23.98-23',
            'url' : 'https://nube.anacsoft.com/aborella',
            'db' : 'falange_aborella',
        }  
        super(PartnerService, self).__init__(data)

    
    def readPartners(self):
        partners = self.read([],['name', 'id', 'phone', 'mobile', 'email', 'website'])
        for partner in partners:
            print(partner)            

    def getOne(self, nombre):
        one = self.read(['name','=', nombre], ['name', 'id'])
        return one
    
if __name__ == "__main__":   
    service = PartnerService()
    service.readPartners()