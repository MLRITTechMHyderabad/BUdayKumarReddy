class Base:
    def __init__(self,name, health, attack_power, defense, speed):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.defense=defense
        self.speed=speed

        def attack(self,target):
           self.target=take_damage(self.attack_power)
        
        def take_damage(amount):
             self.health-=amount

        def is_alive(self):
            if self.health<=0:
                  return False
            return True
                     


class warrior(Base):
        def __init__(self,rage,name, health, attack_power, defense, speed):
            super().__init__(name, health, attack_power, defense, speed)
            self.rage=rage
        def BerserkMode(self,health):  
            if health < 0.3:
                self.attack_power*=2

               

class Mage(Base):
     def __init__(self,mana,rage,name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed) 
        self.mana=mana
     def fireball(self,health,amount):
        

class  Archer(Base):
     def __init__(self, critical,amount):
          super().__init__(name, health, attack_power, defense, speed)
          self.critical+=amount   
     def PrecisionShot(self,health,amount, ):
               self.health+=amount
               self.attack_power-=amount       

