from personaje import Personaje
import random

class Juego:
    def __init__(self):
        self.jugador = None
        self.orco = None
        self.vidas = 5
        
    def iniciar(self):
        print("¡Bienvenido a 'Calabozo sin dragones'!\n¿Quién necesita dragones para pasar un mal rato, verdad?")
        nombre_heroe = input("¿Cuál será el nombre de tu héroe?\n")
        self.jugador = Personaje(nombre_heroe)
        self.nuevo_orco()

    def nuevo_orco(self):
        self.orco = Personaje("Orco")
        print("¡Ha aparecido un Orco!")
        self.jugador.mostrar_estado()
        self.orco.mostrar_estado()

    def enfrentamiento(self):
        while True:
            probabilidad_victoria = self.jugador.calcular_probabilidad_contra(self.orco)
            print(f"Tienes {probabilidad_victoria * 100:.1f}% de probabilidad de vencer al Orco.")
            decision = self.jugador.enfrentamiento_orco()
            if decision == 1:
                self.combate()
            elif decision == 2:
                print("Has decidido huir. El orco no te persigue más.")
                break
                #vidas -= 1
                #if self.preguntar_si_continuar(): #and vidas > 0:
                    #print(f"Te quedan {vidas} vidas")
                #    self.nuevo_orco()
                #else:
                #    print("Fin del juego. Gracias por jugar.")
                #    break

    def preguntar_si_continuar(self):
        respuesta = input("¿Deseas continuar jugando?\n1: Si\n2: NO\n")
        return respuesta.strip().lower() == '1'

    def combate(self):
        resultado_combate = random.uniform(0, 1)
        probabilidad_victoria = self.jugador.calcular_probabilidad_contra(self.orco)
        if resultado_combate <= probabilidad_victoria:
            print("¡Le has ganado al orco, felicidades!\n¡Recibirás 50 puntos de experiencia!")
            self.jugador.actualizar_estado(50)
            self.orco.actualizar_estado(-30)
        else:
            print("¡Oh no! ¡El orco te ha ganado!\n¡Has perdido 30 puntos de experiencia!")
            self.jugador.actualizar_estado(-30)
            self.orco.actualizar_estado(50)
            self.vidas -= 1
            
            if self.preguntar_si_continuar() and self.vidas > 0:
                print(f"Te quedan {self.vidas} vidas")
                self.nuevo_orco()
            else:
                print("Fin del juego. Gracias por jugar.")
        self.jugador.mostrar_estado()
        self.orco.mostrar_estado()
        #if self.preguntar_si_continuar():
        #    self.nuevo_orco()

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()
    juego.enfrentamiento()