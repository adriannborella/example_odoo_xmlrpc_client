from conector import Conexion
import unicodedata

class LPService(Conexion):
    def __init__(self):
        data_8 = {
            'usuario' : 'admin',
            'password': 'AJDN2576tft',
            'url': 'http://ranchu.anacsoft.com',
            'db' : 'ranchu_restaurada'
        }        
        self.model = 'koozo.lista.precios'
        self.fsService = FLPService()
        super(LPService, self).__init__(data_8)
        
    
    def getLp(self):
        datos = self.read([],['id', 'lpr_pro_id', 'name', 'lpr_cli_ids'])
        
        for lp in datos:
            clientes = self._leer_registro([['id','in', lp['lpr_cli_ids']]],['name'], modelo='res.partner')
                    
            self.fsService.sincronizarLista(lp, clientes)
    
class FLPService(Conexion):
    def __init__(self):
        data = {
            'usuario' : 'administrador_anac',
            'password': 'Fi947SM51ta',
            'url': 'http://ranchu2.anacsoft.com',
            'db' : 'ranchu11'
        }
        self.model = 'asw_lp.lista_precios'
        super(FLPService, self).__init__(data)
        self.login()
    
    def sincronizarLista(self, lista, clientes):
        # print("Sincronizando Lista", lista, clientes)
        lista = self.read([['name','=', lista['name']]],['name'])[0]
        print(lista)
        arrclientes = []
        
        for cli in clientes:
            nombre_busqueda = self.chau_acentos(cli['name'])
            id_cliente = self._leer_registro([['cli_razon_social','=', nombre_busqueda]],['id', 'cli_razon_social'], 'asw.cliente')
            arrclientes.append(id_cliente[0]['id'])
            
        if(len(arrclientes) != len(clientes)):
            # aviso de la lista de precio con error
            pring("La lista de precios tiene clientes sin encontrar", lista)
        
        update = {
            'lp_clientes' : [[6, 0, arrclientes]]
        }
        self.write(update, lista['id'])
        

if __name__ == "__main__":   
    service = LPService()
    service.login()
    service.getLp()