def encode_json():

	ruta = {'ruta':{ 'id':1, 'camion': camiones_dict() }}
        buspoint = {'transporte': ruta }
        return buspoint



def camion(id,latitud,longitud,hora):
        """(int,double,double,int) -> dict of key:value
        >>>camion(id,latitud,longitud,hora)
        {"id":id,"latitud":latitud,"longitud":longitud,"hora":hora}
        >>>camion(3,25.32,-97.4553,2342342342)
        {"id":3,"latitud":25.32,"longitud":-97.4353,"hora":2342342}
        >>> camiones = [camion1,camion2,camion3]
        >>> print json.dumps(camiones,indent =4 )

        """
        camion = {'id':id,'latitud':latitud,'longitud':longitud,'hora':hora}
        return camion

def camiones_dict():
        """ ()-> dict of key: [list of {dict of keys:values}]
        >>>camiones_list():
        {'camion':[{'id':6,'latitud':78,'longitud':567,'hora':676},{},{}]}
        """
        camiones = []

        for x in range(5):
                camiones.append(camion(x,x*23,x*25,x*123))

        return camiones

