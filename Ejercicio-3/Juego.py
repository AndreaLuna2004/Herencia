from Jugador1 import Jugador1
from Jugador2 import Jugador2
from Jugador1 import luigi
from Jugador2 import mario

class Juego(Jugador1,Jugador2):
    pass

    def Batalla():
        #ataque del jugador 1
        print(f"{luigi.nombre} ataca, resta {luigi.ataque} de la salud de {mario.nombre}")
        mario.salud = mario.salud - luigi.ataque
        print(f"La salud de {mario.nombre} es {mario.salud}")

        #ataque del jugador 2
        print(f"{mario.nombre} ataca, resta {mario.ataque} de la salud de {luigi.nombre}")
        luigi.salud = luigi.salud - mario.ataque
        print(f"La salud de {luigi.nombre} es {luigi.salud}")

        #ataque del jugador 1
        print(f"{luigi.nombre} ataca, resta {luigi.ataque} de la salud de {mario.nombre}")
        mario.salud = mario.salud - luigi.ataque
        print(f"La salud de {mario.nombre} es {mario.salud}")

        #ataque del jugador 2
        print(f"{mario.nombre} ataca, resta {mario.ataque} de la salud de {luigi.nombre}")
        luigi.salud = luigi.salud - mario.ataque
        print(f"La salud de {luigi.nombre} es {luigi.salud}")

        #ataque del jugador 1
        print(f"{luigi.nombre} ataca, resta {luigi.ataque} de la salud de {mario.nombre}")
        mario.salud = mario.salud - luigi.ataque
        print(f"La salud de {mario.nombre} es {mario.salud}")
        #ataque del jugador 2

        print(f"{mario.nombre} ataca, resta {mario.ataque} de la salud de {luigi.nombre}")
        luigi.salud = luigi.salud - mario.ataque
        print(f"La salud de {luigi.nombre} es {luigi.salud}")

        #ataque del jugador 1
        print(f"{luigi.nombre} ataca, resta {luigi.ataque} de la salud de {mario.nombre}")
        mario.salud = mario.salud - luigi.ataque
        print(f"La salud de {mario.nombre} es {mario.salud}")
        print(f"!!! {luigi.nombre} gana la batalla !!!")
       
pelea = Juego
print(pelea.Batalla())





