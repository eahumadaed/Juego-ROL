class Personaje:
    def __init__(self, nombre_heroe):
        self.nombre = nombre_heroe
        self.nivel = 1
        self.exp_actual = 0
        
    def mostrar_estado(self):
        print(f'NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.exp_actual}')

    def actualizar_estado(self, experiencia_nueva):
        exp_total = self.exp_actual + experiencia_nueva
        while exp_total >= 100:
            self.nivel += 1
            exp_total -= 100
        while exp_total < 0 and self.nivel > 1:
            self.nivel -= 1
            exp_total += 100
        self.exp_actual = max(0, exp_total)

    def __gt__(self, otro_heroe):
        return self.nivel > otro_heroe.nivel

    def __lt__(self, otro_heroe):
        return self.nivel < otro_heroe.nivel

    def calcular_probabilidad_contra(self, adversario):
        if self < adversario:
            return 0.33
        elif self > adversario:
            return 0.66
        return 0.5

    def enfrentamiento_orco(self):
        print("¡Un Orco ha aparecido frente a ti!")
        accion = int(input("Selecciona una acción:\n1. Atacar\n2. Huir\n"))
        return accion