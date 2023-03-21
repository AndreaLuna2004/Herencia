from Peliculas import Peliculas
from Tipo import Tipo
from Tipo import tipoCat
from Peliculas import peli

class Cliente(Peliculas):
    pass

    def __init__(self, elegir):
         self.elegir = elegir

    def Ver(self):
            if self.elegir == tipoCat.Caccion:
                 return 'la pelicula {} pertence a la categoria {}'.format(peli.nombreAccion, tipoCat.Caccion)

            elif self.elegir == tipoCat.Ccomedia:
                 return 'la pelicula {} pertence a la categoria {}'.format(peli.nombreComedia, tipoCat.Ccomedia)

                

            elif self.elegir == tipoCat.Cterror:
                return 'la pelicula {} pertence a la categoria {}'.format(peli.nombreTerror, tipoCat.Cterror)


Ver =  Cliente("accion")

print(Ver.Ver())
