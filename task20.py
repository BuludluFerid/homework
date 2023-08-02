class Player:
    def _init_(self):
        self.health = 100

class Soldier(Player):
    def _init_(self, name , power, bullets):
        super().__init__()
        self.name = name
        self.power = power
        self.bullets = bullets

    def attack(self, enemy):
        if self.bullets > 0:
            enemy.take_damage(self.power)
            self.bullets -= 1
        else:
            raise ValueError("Güllə sayı bitib,Atəş açıla bilməz")
        
class Doctor(Player):
    def _init_(self, name, power, healing_potions, healing_power=60):
        super()._init_()
        self.name = name
        self.power = power
        self.healing_potions = healing_potions
        self.healing_power = healing_power

    def heal(self, ally):
        if self.healing_potions > 0:
            if ally.health < 100:
                ally.health += self.healing_power
                self.healing_potions -= 1
                if ally.health > 100:
                    ally.health = 100
                print(f"{self.name}, {ally.name}-ın sağlığını {self.healing_power} gücündən artırıb.")
            else:
                print(f"{ally.name} tamamilə sağlamdır.")
        else:
            print(f"{self.name} artıq sağaltıcı içki sayı bitib. Sağalmaq mümkün deyil.")

