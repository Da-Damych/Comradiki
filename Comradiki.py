import time
import random
import os
import textwrap

print(" ")
print(" ")
print(" ██████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ██████╗ ██╗██╗  ██╗██╗    ")
print("██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║██║ ██╔╝██║    ")
print("██║     ██║   ██║██╔████╔██║██████╔╝███████║██║  ██║██║█████╔╝ ██║    ")
print("██║     ██║   ██║██║╚██╔╝██║██╔══██╗██╔══██║██║  ██║██║██╔═██╗ ██║    ")
print("╚██████╗╚██████╔╝██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║██║  ██╗██║   ")
print(" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝   ")
print("")
print("")
start = input("Нажмите [ENTER] для продолжения")
os.system('cls')

#Главный герой
class Hero:
    def __init__(self):
        self.items = []
        self.teams = []
        self.inventar = []
        self.attack_power = 25
        self.revpoint = 0
        self.kappoint = 0
        self.health = 100
        self.mana = 100
        self.name = "Крош"

krosh = Hero()

#Капиталюги   
class Enemy:
    def __init__(self, enemy_type):
        self.type = enemy_type
        if enemy_type == "робот":
            self.health = 40
            self.attack_power = 10
        elif enemy_type == "менеджер":
            self.health = 80
            self.attack_power = 15
        elif enemy_type == "оптимизатор":
            self.health = 100
            self.attack_power = 20

#Класс Битвы
class Battle:
    def __init__(self, enemies, win_scene, lose_scene):
        self.enemies = [Enemy(enemy_type) for enemy_type in enemies]
        self.win_scene = win_scene
        self.lose_scene = lose_scene
    
    def player_attack(self):
        battle_boost = random.randint(self.player.attack_power - 5, self.player.attack_power + 5)
        return battle_boost
    
    def hack_robot(self):
        robots = [e for e in self.enemies if e.type == "робот"]
        if not robots:
            print("Ёлки-иголки! Нет роботов для взлома!")
            return False
        
        target = random.choice(robots)
        print(f"Взлом робота...")
        
        for _ in range(3):
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-", "*"])
            primer = f"{a} {op} {b}"
            answer = eval(primer)
            
            try:
                user_answer = int(input(f"Решите пример: {primer} = "))
                if user_answer != answer:
                    print("Ёлки-иголки! Взлом не удался! Пропуск хода...")
                    return False
            except:
                print("Ёлки-иголки! Взлом не удался! Пропуск хода...")
                return False
        
        target.health = 0
        print("Робот взломан!")
        return True

    #Лечение (Сначал забрать у Нюши конфеты)
    def heal(self):
        if "конфеты" in self.player.items:
            self.player.health = self.player.health + 35
            print("Восстановлено 35 HP")
            return True
        else:
            print("Нет конфет для лечения!")
            return False

    #Сам бой
    def start_battle(self):
        self.player = krosh
        
        while True:
            # Ход Кроша
            print(" ")
            print(f"\nВаше HP: {self.player.health}")
            print("Враги:")
            for i, enemy in enumerate(self.enemies):
                if enemy.health > 0:
                    print(f"{i+1}. {enemy.type} (HP: {enemy.health})")
            
            action = input("\nВыберите действие (1-атака, 2-лечение, 3-взлом): ")
            
            if action == "1":
                target = int(input("Выберите цель: ")) - 1
                damage = self.player_attack()
                self.enemies[target].health -= damage
                print(f"Нанесено {damage} урона {self.enemies[target].type}!")
            
            elif action == "2":
                if not self.heal():
                    continue
            
            elif action == "3":
                if "Пин" not in self.player.teams:
                    print("Взлом недоступен!")
                    continue
                if not self.hack_robot():
                    continue
            
            # Проверка на победу
            if all(e.health <= 0 for e in self.enemies):
                print("\nПобеда!")
                self.win_scene()
                return
            
            # Ход капиталюг
            for enemy in self.enemies:
                if enemy.health > 0:
                    damage = random.randint(enemy.attack_power - 5, enemy.attack_power + 5)
                    self.player.health -= damage
                    print(f"{enemy.type} наносит Крошу {damage} урона!")
            
            # Проверка на поражение
            if self.player.health <= 0:
                print("\nПоражение!")
                self.lose_scene()
                return

#Постепенный вывод текста
def prs(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True) 
        time.sleep(delay)
    print()

#Начальная локация. Домик кроша
def home():
    os.system('cls')
    print(" ")
    print(" ")
    prs("Ромашковая долина с момента окончания сериала цвела и пахла, развивалась семимильными шагами. Несколько лет спустя в один обычный ничем не примечательный день на остров к главному и по совместительству единственному порту, из далека по бескрайнему морю приплывает корабль. На нем были смешарики из города, только они не были такими же жизнерадостными и дружелюбными, а более мрачными и грустными. Они выкупили остров Ромашковой долины и предложили местному населению переехать в другое место на краю города, где были множество заброшенных хижин. Но только наши герои были не согласны с бумажкой, что все показывали люди с корабля, доказывая – этот остров куплен одной ужасной капиталистической организацией без души. Люди с корабля ничего не сделали на протесты и возникшее недовольство, а так же недовольство местных жителей. На этом моменте история могла закончиться, если бы не вторгшиеся на остров капиталисты на следующий день.")
    prs("Утром Крош проснулся не от лучей утреннего солнца, что так мотивировало его на работу во благо всей их коммуны, весь остров в моменте поразило землетрясение. Свинина упала, подумал наш герой. А так же техника капиталистических мразей вскапывавшая коммунистическую землю, вырывая котлован для какой то постройки.")
    prs("Кролик не мог оставить это все так как есть и поднявшись с кровати он надел свою фуражку с сербом, молотом и звездой и отправился чистить их земли от забугорских капиталистов пришедшие на эти земли только чтобы забрать их общее и присвоить себе.")
    print("")
    print("Выйти на улицу?")
    print("")
    print("1. Да")
    print("2. Нет")
    print(" ")
    choise = input("Твой выбор (1-2): ")
    if choise == "2":
        end_home()
    else:
        outside()

#Улица
def outside():
    os.system('cls')
    print(" ")
    print(" ")
    prs("Крош выходит из своего домика и оглядывает местность. В дали виднеются трактора, роботы и странно выглядящие люди. Видя это Крош наполняется решительной ненавистью к этим капиталюгам.")
    print("")
    print("Куда вы напрявитесь?")
    print("")
    print("1. Надо бежать к Ёжидзе, вдруг с ним что-то случилось! Он может быть в опасности!")
    print("2. Первым делом лучше пойти к Лосяшу, он умный и что-нибуть придумает.")
    print("3. Пин! Наш техник точно смастерит полезную штуковину")
    print("4. Стоит сходить к Нюше, нужно проверить как она.")
    print("")
    choise = input("Выберите ответ (1-4): ")
    if choise == "1":
        home_ezik()
    elif choise == "2":
        home_los()
    elif choise == "3":
        home_pin()
    else:
        home_svin()

#Домик Ёжика 1 часть
def home_ezik():
    os.system('cls')
    ascii_art = """                                  &&&&&                                                                                         
                                                &$$&&$xX$&&$$$&&                                                                                  
                                               &Xx+X$&x+$&Xx+x$$$$                                                                                
                                                &$x+x$X+X$x+x$x++X$                                                                               
                                                   $Xx$$&X+xx+++$&&                                                                               
                                          &&&&&&&&&&&$xxx++xX$$&&                                                                                 
                                   &&&&&&$$XXXXXX$$x+++++xxxxX&&&&&&&                                                                             
                              &&&&$$XxxxXXX$$$$$$$$Xx+++++xX$&$$$XXX$$&&&&                                                                        
                          &&&$$XxxxXX$$$$$$$$$XxxxXX$&&$$$Xx+xX$$$$$$XXXX$$&&&                                                                    
                       &&&$X+++x$$$$XXXXX$Xx+++X$$XX$&$XXX$Xx+++XXXXXXXX$$XxX$&&&                                                                 
                    &&&$x+++X$$$$XxxxxXXx++++XXXXXX$&$XxXXXXXXx++xXXXXXXXXXX$$xxX&&&                                                              
                  &&$x+++x$$XXX$$&$XXXx++++XXXXXxxX$&$XxxxxxxXXX+++xXxxxxxxxXX$$$x+X&&$                                                           
                &&$++++X$XXXX$XXXXXX+++++XXXxxxxxX$X$XXxxxxxXxxxXX+++XXxxxx+xX$X$&$X+x$&&                                                         
              &&X+++x$$XXXX$$xxxXXx++++xXXXXxxxXXXxxX$XxxXXXxXxxxXXx+++XXX$$&$X$XXX$$X++X&&$                                                      
            &&$x++x$$$$$$$$$xxxXx++++xXXxxxxxXxxxxxxxXXXXxxxxxX$$$$XX+++xXXXxxxx$XXXX$$X++x$&$                                                    
           &$x++x$$XXXXXxX$XxXXx++++XXXxxxxxxxxxxxxxxxxxxxxxxxxxxXxxXXx++xXxxxx+X$XXXXX$$x++X$&                                                   
         &&$+++X&$XXxxxxxxX$$X++++xX$XxxxxxxXXxxxxxxxxxXXxxxxxxxx$xxxxXx+++XXxxx$$XxxXX$$$$+++X&&                                                 
        &&X++x$$$XxxxxxxxxxXX++++XXXX$$XXXXXX$XXxxxxxXX$XXxx+++xX$XxxxxXX+++XXXX$xX$$$$XXX$$X++x$&                                                
       &&x++X&XX$Xx+xxxxxxXX++++XXxxxxxxXXxxXXX$$$&&&&$XX$$XXX$&$xx$xxxX$$+++x$XxxxxxxXXXXX$$$+++X&$                                              
      &&+++$$XXXX$$XxxxX$$X+++xXXxxxxxxXXXXXx++++++++++x$XXXXxXxxxxxxXXXxx$++++$xxxxxxx$xXXXX$$x++x$&                                             
     &&+++$$XXxxxXxXXXXxXX+++xXXxxxxxxXX$Xx+x$$$$xxX$$x+++XXXXXxxxxxxxxXxxx$x+++$xxxxxx$$$XxXX$&X++x$&                                            
     &x++$$xxxx$XxxxxxxXX+++x$XxxxxxxX$$X++XXXX$X+XXXX$$x++xXXXXxxxxxxxxXxxx$x+++$xxxxx$XxX$$$$$$X++xX&                                           
    &x++$$XXX$$XxxxxxxXXx++xXXXXxxxX$$$$x+xXXX$Xx+xXXX$&$+++XXX$Xx+xxxxx$Xxxx$x+++$xxxX$xxxxXXXX$$$++xX&                                          
   &X++X$$$$$XXx+xxxxxXx++xXXxxXX$$XXXXX++++++++++++++++++++x$$$$$xxxxX$XxX$$$$+++x$XX$xxxxxxX$XX$$$++xX&                                         
  &&++x$$XXxxxX$x+xxxXX+++XXxxxxxxxxxX$X+xXXXXX++xxxxxx+++;+x$$XXX$$$$$xxxxxxxX$+++x$XxxxxxxxxX$$X$$X++x$&                                        
  &X++$$$xXxxxxX$$$XX$x++XXxxxxxxXxxxX$X++XXX$$xxXXXXXX$$x++X$XXXXxxxXxxxxxxxxx$X+++XXXxxxxxxxxX$$$$$X++x$&                                       
  &++x$$$xxxxxxxxXXXXX++x$xxxxxxXXxxxXX$X++X$$XxXXX$$$&$x+++$$XXXXxxxXxxxxxxxxx$$x+++$X$xx+xxxxXXXXX$$X++X&                                       
 &X++$$$$xxxxxxX$XxX$+++$$XxxxX$$xxxxXX$$X++x$X+X&&&$Xx+++x$$XXXXXxxXXXxx++++x&XX$+++x$X$$X$$$$XXXXXX$$x+xX&                                      
 &x++$$X$$Xxxx$&XxX$X++x$XXX$$XxxX$XX$&$X$$x+++++++++++++$$$$Xxxxxx$$xxxX$$$&$xxXXX+++$$XXXXXXxxxxXXXX$$++x$&                                     
 &++x$$XX$&$XXXX$XX$x++XXXXxXXxxxxxxXXXXXXX$$$Xx++++xX$$$$XXX$$XX$$XxxxxxXxxxxxxxX$+++x$XXxxxXxxxxxxxX$$X+xX&      &&&              &XX$$         
&$++x$XXXX&XxxxxX$$$++x$$$X$$xxxxxxxXXXXXXXXX$$$$$$$$$$$XXXXXXX$XXXXxxxxxXxxxxx+xX$X+++$XXxxX$XXxxxX$$$$Xx+x$&  &&$XXX$&     &$xxxxX$$$xX$        
&$++X$XxX$XxXxxxXX$X++x$XXXXXXxxxxxX$XXXXXXXX$XXXXXXXX$XXXXXXXX$XXXxxxxxx$XXxxXX$XX$+++X$Xx$$XxXX$$$XXXX$X+x$&&&&$$&&$XX&&&&&$XX$$XxxXXX$         
&X++$$$$$$XxxxXXXX$x++x$XXxxxXXxxX$$XXxxxxxX$$XXXXXxX$$XXxxxxX$$XXxxxxxX$XxxXX$XxxX$X++x&$$XxxxxxxXXXXXX$Xx+X$$$$$$$$&$X$$$$$XXXXxxXx$$&          
&X++$$XXXX$XxxXXX$$+++X$XXxxxxX$$$XxXX$XXX$$$XXXxxX$$XX$XXXX$$XXXX$$X$&$xxxxxxXxxxXX$+++$XXxxxxxxxxXXXXXXXx+X&&$$$&&&&XX$&&&&$xX$                 
 &X$$$XXXXX$&$$$$$$+++X$XXxxxxXXxxxXXXXXXXXXXXXXX$XXXXXXXXX$XXXXXXXxxXxxxxxxxxXx+xXX$+++X$XxxxxxxxX$XXXX$$x+x$&&&&  &&XX&    &XxX$                
   &$XxxxX$XXXXXX$X+++X&$XxxxX$XxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx$xxxxxx+x$XxxxX$x++x&$XxxxxxX$XXXXXXXX+x$&    &&XX$      &$xX$               
   &&$$$$&XXxXXX$$X+++X$$$&$$XXX$XXxxx$$XxxxxxxX$$XXxxxxxx$$XxXXXXxxX$Xxx++xx$$X$&&&&X++x&XX$$&&$XXXXXXXXXXxxX&  &&&$xX$&&    &&X++xxX&&          
     &&&&&$$XXXX$$$+++X&$$XXXXXXXXX$$$XXX$$$$$$$$XX$$$XX$$$X$XxxxxxX$XXXX$$$$XXXXXXX$$++x$$XXXX$$XXXXXXX$$$$$$ &&$XXXXXxx+X$&$xxXX$$$Xxx$&        
     &&&&  &&&&&&&$x++$$$$XxXXXXXXXXXXXXXXXXXXXXXXXXX$$$XXXXXX$$$$$$XXXXXX$XXXXXXXXX$$+++$$XXXx$&$xxxX$$&&    &&$X$&   &&$xX$xX$&     &$+$$       
  $&&Xxx&&       $&$$X$XXX$XXXX$$$XXXXXXxxXXXXXXXXXxXXXXXXXXXXX$XXXXXXXxXX$XXxxXXXXX$$++x&$XXxX$$&$$&&&       &$X$       &$xxx$&       &xx$       
 &$$$xxX&&&&$$$&&$Xxxxxxxxx$$&&$xXXXxxxxxX$xXXxxxxxX$XXXXXXxxXX$XXXXxxxXX$xX$XxxxxX$$$Xx$$XXXXXxx&            &$X$&      &$X$xX&      &&xX$       
 $&$X$$X$&$&&xxx&$XxX$$$$++xXxxXXxxX$$$$$Xx++xX$$$$XxXXXXXxXX$$xxX$$$$$$$x++xX$$$$$x++xXx+++++++xX&           &&XX&&&&&&&$X$&$X$&&&&&&&xx&&       
 $&XxX$$&&&$Xxx$$$$$$xxX$$XXXxxX$$xxx++++++++++++++++++xxX$$$Xx++++++xxx+++xXx+++++++++++++++++++x$            &&$XX$&&$XX&& &&$XX$$XxX$&         
   &$$&&&$&$XXXX$$$$XXx$$$X$XX$X$&$x+xXx++++++++++++++++++++++++++XXXx++++$x+x$X++++++++++;;;;;+++X&             &&&&&&&&&      &&&&&&            
         $$$xXX$$$$$$$$$&&$$$$$$X$&$xx++xx+xXXxxXX+++++++++++++++X+++++x$X+++++x$x+++++++;;;;;;;;+x&                                              
           &$$$$X++XXXxX$$xXX$XX$&&X++xx+xx++xXX+Xx++xXXXXx++++++x+++++++++++++++xxxxX$x++;;;;;;;;+$&                                             
            $&$xxX$$$$$$XxXx++xxX$XXx+++x+xx+x+++xXXX$XX$XXXXXXxxx++++xX$&&&&$xxx+++++x$+++;;;;;;;+X&                                             
            &&X+++++++xX+xXxxxXXXXXXX+++xx+x+;;;+XXXXXxXXXXXX$$X++++$&XXX&&$$$$XxXx++;+$x+++;;;;;;+x&                                             
            &&x+xX$Xx++X+XXXXXXXXXXXXx++xxxxxxxxXXXXXxxX$XXXX$XX$xX&&&&$X&$$$$$$XxxX+++$Xx+++;;;;;;x&                                             
            &&xx+++++++XxxXxXXXXXXXXXXXxXxxx++xXXxXXXX$$$$$$X$XXX$X$&&&&&&$$$$$$$xxxX++++x$x+++;;;;x$                                             
            &&x++++++++XXxXXxX$XXXXXXXXXXxXx++xXxXXxxxxxxxxXX$$$$$$&&$X$&&$$$$$$$X+xxX+;;+Xx++++;;;x$&&$$$$$$$$$$$$$$$$$&                         
             &X++++++Xx+XX+X$xX$&XXXXX$$xXX++X$XxXXXX$$&$$$XXXXXXX$&&&&&&$$$$$$$$X+xx$+++x$+++++;;;xXxx++++++++++++++++++X$                       
             &&$XXxx+++++x$xxX&$$$$&$XxX$X++++XXxX$XXX$X$$XX$&$$$$$&&&&&&$$$$$$$&xxxx$+++$x+++++;;;x$XXx+x$$$Xxx$&&&$xX$X++X$                     
              &$x++++++++++x$$XXxXXX$$Xx+xxx++XXxX$X$$$X$$XXX&$XXXX&&&&$$$$$$$$$$xxxXX++++xX++++;;+x& $X+x& &Xx+X&&&$xX$&x++x$&                   
               $X+++++++++++++xxXXxx++++++++xx$Xx$$X$X$X$XXXX&$XXX$&&&&$$$$$$$$$xxxX$++;;++X++++;;+X& Xx+xX$&X++x$&&X++$&&X++x$&                  
               &$+++++;;;;;+++++++++++++++++++xXXX$XXx$X$XXXX&$$$X$&&&$$$$$$$&XxxxX$x+++xxx+++++;;+$&&Xx++X&$X++x$&&X++X&&&X+x$&                  
               &$x;+++;;;;;;;;;;;++;;;;;;;;;+++X$X$$$$$X$X$$$$XXX$&&&&&$$$$$$xxxxX$x++;+X+++++++++x&&&Xx++X&$X++x$&$x++X&&&XxX$                   
                $X;++++;;;;;;;;;;;;;;;;;;;;;;;++X$X$XXXX$$XxxX$$$&X$&&&&$$XxxxX$$X+++;+++X+++++++xX&&$$x+xX$$X++X&&$x++$&&Xx$&                    
                &$+;+++;;;;;;;;;;;;;;;;;;;;;;;;++x$$$$XXxX$&&$X$&x+++X$$$$$$&&Xx++++xXXx++++xxX$&$Xxxx+xxxx+xX$X$XX$X+X&$XX&&                     
                 $X+++++;;;;;;;;;;;;;;;;;;;;;;;;+++X&&&$$XXXX$&$$XXx++++++++++++++xxX$$&&$XXxxxx+++++xxXXXxxxx+++++x$&&&&&&&&                     
                 &$x++++++++++++;;;;;;;;;;;;;;;;;++++x$&&&&&$XXXXxxxxxxxxxxxxxx++++++++++++++++++++++xxxxxxxxxxx+++XXXXXXXX$&&                    
                  &$x+++xxxXXxxx++++++;;;;;;;;;;+++++xXxxxxx+++xXXxxxxx++++++xxxxxxxx+++++++++++++++++++++++++++xXXXXxxxxxxX$&                    
      &&$$&&&$$$$$&&$$$$$XXXXXXXX$$$XXx++++++xXXXXXXXXXXx++++++xxxxxxxx+++++xxxxxx+xxxx++++xxxxxxxxx+++++++++++xXXX$$XxxxX$$XxxxxXX$&             
     &$XX&&&$$$$$$$$$$X$$XXXxXXXXxxxXX$$$$$XXxxxxxxXXxXXX$$Xx+++++++++++++++++++++++++++++xxxxxxxx+++++++xxxxxXXxxXXxxxXXxxXXx++xXX$$&            
   &&$X$$X$$$$$$$$$$$$$$$XXX$&$$$Xxxxxxxxxx+xxxxxxXXxxxxxxXX$$Xx++++++++++++++++++++++++++xx++xxxXXXXXXXxxxxxxxXx+++xXx+++xxxxX$$$XXX$&           
  &&&&&$$XX$$$$$$$$$XXXXXXX$$$$$XxX$$XXXXXXxxxXXXX$$xxxxxxxxxxxXXx+++++++++++++++++++++++xxX$$$XXxXXXXxxxxxxxxxxxxxXx+++++x$$$XXXXxxxX$           
  &$X$&&$XXX$$&&&&&&$$$$$$X$XxxxxX$XXXXXXxxxX$$$$$$$$$xxxxxX$XxxxxXxxxxxxxxxxxXXX$$&&&&$XxxxxX$&&$$$$$$Xxxxxxx++x$$XXx++X$XXX$Xxxxxxxx$&&&$       
  &XxX$XXX$$&&&&&&&&&$$$XXxxXXxxxx++++++XXx+++++++++++x$&$XxXXxxXxxxxxxxxxxxxxxxxxxxxxxxxxxxxX$$$$$$$$$XxxxxxxxxxxxxxxxXXXX$$Xx++X$$Xxx+++xX$$    
  &Xx$$XXX$XXXXXX$$xxxX$XxxxXXxxx++++++xxxxxX$$Xx++xXXXxxxx$&$XxXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX$$$$$XxxXXxxxxxxxxxx+++xxxXxxx$&$XxxXXXxx++X$$$&  
  &$X$XXxX&XXxxxX$Xxxxx$XxxX$XxxXXXXXXXXx+x+xxxXX$$Xx++++xxX$$&&$xxX$$XXXXXXXX+++++++++++++xxxxxxxxx+xxX$XXXXxxxxxxx+++xxxxX$$Xx++++xx++X$$XXXX$& 
  &&&&$$$$&$$$$$$&$XXX$$$$$$XXxX$$$$$$$XxxxxX$XXXXxXXXXXXXXxxxxxxxxXXXXXXXXXXx++++++++++xXXXXXXxx+xxX$&&&&&&&$xxxxxxx++xX$Xxx++++++++x$$$XXXxxxX&$
   &&$&&&&&&&&&&&&$$$$$$$$$$$$$Xxx++++xxXXXX$$XXXxxxXXxxxxxxxxxxxxxxX$$XXxxxxxxxxx++++xx$XXXX$$X+x$&&&&$$&& &&&$XxxxxxxxXXXXXXx++++x$$XXX$&&Xxxx&$
    &$$XX$$$$$&&&&$$$$$$$$&&&$XXXXxx+++++xxxxxXXXXxXXxxxxxxxxxxxxX$&&&$&&Xx+x$$XXXxx+xx$XXXXXXXXX&&&$$$$$&&    &&$XxxxxxxxxxxxX$XX$XXXXx$&$$$xxX&$
      &&&&&$$$$$$$$$$$&&&&&&XXXXxXXXXXxxxxxxx++++x$$$XxxxxX$&$XX$&&$$$$$$&$XxX$XXXxxxxx$$XXXXXX$&$$$$$$$$&&      &&Xxxx$$$$$XxxX$$XXXxxX&&$xxx$&&$
              &$&&       &&$$XXxxxxxxxXXXx+++xX$$XXXXxxxx$&&$X$&&$$$$$$$$$$$Xx$$$XxxxxxX$$$$XxX$$$$$$$$$&&        &&$x$&$$$$$XxxX$XxxxxxXxxx$&&   
                            &&&&XXxxxxxxXX$$XXXXX$$$XxxxxxxXXX&$$$$$$$$$$$&&XxxxxxxxxxxxxxxxxxX&$$$$&&&&&&         &&$X$$$$$$Xxxx$Xxxxx++x$&$     
                               &&&&$XxxxxxxXxxxX$&$$$xxxxxxxxx&$$$$$$&&&&  &$xxxxxxxxxxxxxxx+xX&&&&&                &$XX$$$$$Xxxx$$xxxxX$$$       
                                   &&&$XXxxxxxx$&$$$XxX&&&$$xX&&&&&&&      &$Xxxx++++++xxxxX$$&&                    $$$xxxxxxxxxx$$XXX$$          
                                      &&&$XXXXXX$$XXX$$$$$$$&&&&&           &&$$$$$$&&&&&&&&&                        &$$$XXXXXxxx$$$$$            
                                        &&&&&&&&&&&&&&&&&&                                                                 $&&&&&&&               """
    lines = ascii_art.split('\n')
    for line in lines:
        print(line)
    print("")
    prs("Подходя к хижине Ёжика, Крош замечает как домик его друга пытается разнести эксковатор в щепки.")
    print("")
    print("Как лучше поступить?")
    print("")
    print("1. Ёлки-иголки, надо разнести кабину!")
    print("2. Ёжик справится и без меня, а у меня появились срочные дела!")
    print("")
    choise = input("Выберите ответ (1-2): ")
    if choise == "1":
        krosh.revpoint += 1
        krosh.teams.append(["Ёж"])
        kabinka_penetration()
    else:
        print("")
        print("Куда теперь отправится?")
        print("")
        print("1. Первым делом лучше пойти к Лосяшу, он умный и что-нибуть придумает.")
        print("2. Пин! Наш техник точно смастерит полезную штуковину.")
        print("")
        krosh.kappoint += 1
        choise = input("Выберите ответ (1-2): ")
        if choise == "1":
            home_los()
        else:
            home_pin()

#Бой за Ёжика
def kabinka_penetration():
    os.system('cls')
    krosh.health = 100
    battle = Battle(["менеджер"], home_ezik_prod, ezik_loss)
    battle.start_battle()

#Поражение за Ёжика
def ezik_loss():
    os.system('cls')
    prs("К сожалению, ты не смог помочь ежику. Его домик снесли, а самого Ежика забрали в плен.")
    choise = input("Чёртовы капиталюги! Они еще поплатятся! (Нажмите ENTER)")
    if choise == "1337":
        print("Чит-код активирован! Базовый Урон +10000")
        krosh.attack_power = 10000
        krosh.health = 10000
        print("")
        print("Куда теперь отправится?")
        print("")
        print("1. Первым делом лучше пойти к Лосяшу, он умный и что-нибуть придумает.")
        print("2. Пин! Наш техник точно смастерит полезную штуковину.")
        print("") 
        choise = input("Выберите ответ (1-2): ")
        if choise == "1":
            home_los()
        else:
            home_pin()
    else:
        print("")
        print("Куда теперь отправится?")
        print("")
        print("1. Первым делом лучше пойти к Лосяшу, он умный и что-нибуть придумает.")
        print("2. Пин! Наш техник точно смастерит полезную штуковину.")
        print("")
        choise = input("Выберите ответ (1-2): ")
        if choise == "1":
            home_los()
        else:
            home_pin()

#Дом Ёжика 2 часть
def home_ezik_prod():
    os.system('cls')
    print("")
    prs("Крош смог справиться с целым экскаватором спася колекцию Ёжика от уничтожения.")
    prs("-Крош, спасибо! Ты сохранил мне мои любимые кактусы,- сказал Ёж и поднял пару упавших горшков. -Но я думаю это не все. Они езе раз захотят разрушить мой дом. С этим надо боротся.")
    prs("-Ёлки-иголки, ты прав. Мы обязаны прекратить позволять капиталистам портить наши дома, кактусы и землю. Пойдем и соберем еще наших друзей для этого!")
    print("")
    print("Куда отправимся дальше?")
    print("")
    print("1. Первым делом лучше пойти к Лосяшу, он умный и что-нибуть придумает.")
    print("2. Пин! Наш техник точно смастерит полезную штуковину.")
    print("")
    choise = input("Выберите ответ (1-2): ")
    if choise == "1":
        home_los()
    else:
        home_pin()

#Домик Лосяша
def home_los():
    os.system('cls')
    r = """                                   &&&&              &&&                                            
                                   &$X$&&           &$$&                     &&&                    
                                   &&XxX&&         &$$$&                   &&&&                     
                                    &$xXX$&&      &$$X$&                 &&$$&                      
                                    &&XxXX$&&     &XXX$&                &$XX&&                   &&&
                                     &&xXXXX$&&  &&XXX$&               &$XX$&              &&&&&&&&&
                                      &&XXXXXX$&&&$XXX$&             &&XXXX&&          &&&&$XX$&&   
                                        &XxXXXXXX$XXXx$&            &&XXXXX&       &&&&XXXXX&&&     
                                        &&XxxxxxxxXXXXX&&           &XXXXXX&  &&&&&$XXXXXX&&        
                                         &&$xxxxxxxxXXX$&          &XXXXXXX&&&$$XXXXXXXX&&          
                                           &$xxxxxxxxXX$&         &$XXXxxXXXXXXXXXXXXX$&&           
                                &&&&&&&&&&&&&XxxxxxxxXXX&        &&XXxxxxxxxxxxxxxXX$&&             
                             &&$$XXXXXXXXXXXXxxxxxxxxxXX$&       &XXxxxxxxxxxxxxxXX$&&&&&           
                           &$XXXXXXXXXXXXXXxxxxxxxxxxxXXX$&     &$xxxxxxxxxxxxxXXXXXX$$$$$&&&&&     
                           &&&$$XXXXXXXXxxxxxxxxxxxxxxxXXX$& &&$xxxxxxxxxxxX$&&&&&&&&&&&&&&&$$$$&&&&
                                            &&&&$$xxxxxxXXX$&XxxxxxxxxxxX$& &&&&    &&&         &&&&
                                                  &XxxxxxX$Xxxxxxxxxxxx&&    &&&&    &&             
                                                   &XxxX$Xx+xx++xxxxx$&        &&&  &&&&&&          
                                                    &X$Xx++++++xxxxX&        &&&&&&&&&&&&&&&        
                                                    &Xx+++++++xxxX$        &&&$X$&&&&&&&&$X$&       
                                          &&&&&&&&&$x+++++++xxxx$&         &&&&X&&&&&&&&&&&&&       
                                  &&&&$$$$$$$$$$&$xx+++++++xxxX$$$&        &&&&&&&&&&&$&&&&&&       
                              &&$$XXXX$$$&&$$$$&Xx+x++++++xxx$XXX$$&       &&&&&&&X$XxxXX$&&&       
                          &&$XXXXXXXXXXXX$$$$&Xxxxx+++++xxxXXxXXXXX$&      &&&$&&&&&&&&&&&&&&       
                        &$XXXXXxxxXXXXXX$$$$$Xxxxx++++xxxx$XxxxxxXXX&&&    &&&$$&&&&&&&&&&$$&       
&&&&&&&&              &XxxxxxxxxxxXxx$&$$$&Xxxxx+++++xxx$XXXxxxxxxXXX$$&&  &&&xxx&$&&&&&$xxX$       
&&&&&&&&&          &$XxXxxxxxxxxxXxXXXXX$$Xxxxx+++++xxx$XXX$xxx+xxxXX$$$$$&&&&&&&$$$$$$&&&&&&       
&&&&&&&           $XXXxxxxx+xxxXXXXXXX$$Xxxxxx++++xxxXXXXXxx$x++++xxXX$$$$$&&                       
&xx$&           &$XXxxxxxxxXxxxxxXXX$$$Xxxxxx++++xxx$X$$$$XXx$x++++xxXXX$$$&$&                      
&&&&&          $XXXxxXxxxXxxXxxxXXX$$XXxxxxx+++xxxX$$$$$$XXXxXX+++++xxxxXXXXX$&&                    
 &X$&&       &$XXXXxX$XXx$$XxxXXX$$$Xxxxxx++++xxx$XXXxXXXX$$XxXx+++++xxxxXXXXX$&&                   
  &X&&      &$XXXXxxxXxxxxxxXXX$$$$Xxxxxx++++xxxXXX$$$$$$XxxxX$Xx+++++xxxXXXXXX$&&                  
  &$$&     &$XXxxxxxxxxxxXX$$$$$&XXxxx++++++xx$$X$XXxxxx$XX$$xxX$x++++xxxxXXxXXX$&                  
   &$&&&  &$XXxxxxxxxxxXXX$$$$&$Xxxxx+++++++xXxXX$xxxxxxX$XXX$Xxx$xx+++xxxx$XX$XX$&                 
    &&&&&&&XXXxxXxXxxxXXX$&$$&$Xxxxx+++++++xXxXXX$$$$$$XXXXXXX$XxXXxx+++xxxx$XX$XX$&                
    &&XX$$&$Xxxx$$XxxxX$$$&&&$Xxxx++++++x+$$XXxxxxxxxxxxxxxxXX$$xx$xx+++xxxxXX$XXX$&&               
      &&XXX$XXxxxxxxxX$$$&&&$Xxxxx++xxxxxXxxxxxxXXXXXXxxxxX$X$$$$X$$xx+++xxxxXXXXX$&&               
        &&$$$XXxxxxX$X&&&&&$Xxxx+++xxxxxXxXX$XXXX$xxx+++xxX$X$$&$$Xx$xx+++xxxXXXX$X&&               
        &$&Xx$&&xx&$x$$$&&$Xxxx+++xxxxX&$XxxxXXXX$Xxx+++xxXXXXX$X$Xx$x+++++xxx$XX$$&&               
        &$X$&&&Xx&&&$x$&&XXxxx+++xxxxX&XXxxxxxxXx$Xxx+++xxX&&&&&$$Xx$xx++++xxXx$$$$$&               
        &XxXXXXx+X$$$x$&$Xxxx++++xxxXX$$Xxxxxxxxx$Xxx+++xxX$$&&&&&&&$xxx++xxxXXX$$$$&               
        &X$&&&$x&&&$xx&$Xxxx++++xxx$$xX&XXxxxxxxxx$xxxxxxxxXX$$XxX$X$xxxxxxxxXXX$$$$&               
        &$X&&&xX&&&xx&$Xxxx++++xxxXX$$XX&$xxxxxxXX$$$XxxxxxX$$XXX&$$$XxxxxxxXXXX$&$&&               
        &&xX&&x&&XxX&$Xxxx++++xxxXXX$$&XX&$XXxxxxxX$$$XxxxX$$XX$&XXXXXxxxxxxxXXXX$&&&               
        &&&$xxxxx$&$$XXxx++++xxxXXXXXX$&&XX$&XX$Xx$XxxxX$&$XX$&$XXXXxXXxxxxXXXXXXX&&                
        &&$$$$$$$$$$XXxxx+++xxxXXxXXXXXX$$$XXxXXX$$$$$XXXX$&&$$$$XXXX$$$$$$XXX$XXX$&                
         &$$$$$$$$$$XXxxx+xxxxXXxxxXXXXXXX$$$$$$$$$$$$$$$XXXXXXXxxxxxxXXX$$$$XXXXXX$&               
          &$$$$$$&&XXxxxxxxxxxXxxxX$&&$$$$XXXXxxXX$$$$$xxxxxxXXxxxxxxxxxxxxX$XXXXXX$$               
         &&&&&$$$&XXxxxxxxxxxXxxxxxxxxxxxXXxxxxxxxxxxx$XXXXXXXXXXX$$$$$$$$$$$$$$$$$$&&&&&&&&&&&     
       &&&&$&&&$&$XXxxxxxxxxxXxxxxxxxxxxx$&xxxx+++++x$xxxxxXXXXXXXXXXXXXXXXX$$$$$$$$$$$$$$$$$$&&    
        &&$$$$$&&$&XXXxXXXxX$xxxx$Xxx$xxx$&XX$x+++++xxxxxxxxxxxxxXXX$$$$$$$$$$$&&&&&&$$$$XXX&&&&    
    &&&&&&&$$&&$&&&&&&&$$$X$$$XX$$$X$$X&&&$$$Xxx+++xxxxxxxXXxxxxxxxxxxxxxxxxxxxXXXXXXXXXX$$$&$$$&&& 
     &&&$$$$$$&&$$$$$$$&&$&&$$$$XXXXXXXXXXXX$$$$$$$X$xxXxxXXxxxxxxxxxxxxxxxXXxxxXXXXXXXX$&&$$$$$$&&&
        &&&&    &&&&&&&&$$$$$$$&&XXXXXXXXXXX$$$$$$$$$&&&&&&&&&XX&&&&&&XX&&&&&$&&&&&&&&&&&&&&&&&  &  
                                  &&&&&& &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                         """
    lines = r.split('\n')
    for line in lines:
        print(line)
    if "Пин" in krosh.teams:
        print("")
        prs("Небольшая команда кроша пришла к дому Лосяша. Крош отворил дверь, дома Лосяш сидел за столом и писал или рисоваал каракулм, как минимум кролик так видел все формулы написанные ученым.")
        prs("- Лосяш, вставай ты нам нужен. С твоей помощью мы справимся с врагами коммунизма!")
        prs("Ученый услышав голос кролика поднял голову и посмотрел на вошедших к нему гойстей. - Друзья, а что собственно происходит?- спросил недоуменно Лолсяш.")
        prs("-О майн год, к нам на остров десантировались жадные до ресурсов капиталисты. Их нужно искоренить! ")
        prs("-Господа, а какой у вас план?- сказал ученый и поднялся из за стола.")
        prs("-Сделать оружие, с которым мы сможем уничтожить врагов коммунизма.")
        prs("-Это же никуда не годится! Можно же решить проблему дипломатически. Я за этот вариант,- произнес Лосяш и посмотрел на Кроша.")
        prs("-Друг мой, вам какой вариант больше нравится?")
        print("")
        print("1. Пин прав, нельзя с ними договорится, проблему можно решить только создав оружие.")
        print("2. Прав Лосяш, мы должны попробовать с ними договорится.")
        krosh.revpoint += 1
        krosh.teams.append("Лосяш")
        choise = input("Выберите ответ (1-2):")
        if choise == "1":
            zd_pin()
        else:
            end_los()
    else:
        print("")
        prs("Идя дальше Крош видел все больше новых лиц. Это были Оптимизаторы - работники компании, они были с оружием. Крош понял сразу - лучше им на глаза не попадаться. Вскоре он был уже у дома Лосяша. Было отчетиво слышно как роботы пилили лес, медлить нельзя иначе их Ромашковую долину быстро превратят в руины где когда-то жили люди.")
        prs("Войдя к Лосяшу Крош замечает как тот мирно сидит за столом, словно ничего и не происходило, и рисует каракули, как минимум для кролика это было непонятный набор символов. ")
        prs("")
        prs("-Лосяш, елки-иголки! Они вернулись, люди с большой земли! Нам нужно спасать остров от капиталистов, - произнес кролик пройдя к лосю сидящему за столом.")
        prs("Ученый поднимает голову и только тогда понимает, что на улице творится неладное. - Это феноменально! Как я не заметил, слишком увлекся исследованием. Крош, подскажи что происходит на улице?")
        prs("-Капиталисты, они хотят забрать нашу землю. Мы не можем оставить это так!")
        prs("Отодвинув бумаги Лосяш встал и пошел вместе с Крошем")

        krosh.revpoint += 1
        krosh.teams.append("Лосяш")
    
        print("")
        prs("Выйдя из дома Крош около деревьев видит испуганного Бараша, он сидит на земле и размышляет о своем.")
        print("")
        print("Как вы поступите?")
        print("")
        print("1. Лучше взять Бараша с собой, вместе мы сильнее.")
        print("2. Баран будет только нам мешать, оставим его.")

        choise = input("Выберите ответ (1-2): ")
        if choise == "1":
            krosh.revpoint += 1
            krosh.teams.append("Бараш")
            home_pin()
        else:
            krosh.kappoint += 1
            home_pin() 

#Дом Нюши   
def home_svin():
    os.system('cls')
    e = """                                                   $$$                                              
                                              $&$x+;;;+x$&$         &$$$                            
                                            &$;;;;;;;;;;;;X&    &&&XxxxxxXXX                        
                                          $&x;;;;;;;;;;;;;;x&&  &$$x+$$x$$$$                        
                                          &+;;;;;;;;;;;;;;;;+&   &Xxxxxx++&                         
                                        &&+;;;;;;;;;;;;;;;;;;x&   $XxxxxX$                          
                                       X&+;;;;;;;;;;;;;;;;;;;;X&  XxXXXXx+X                         
                                      $&+;;;;;;;;;x$$X$X+;;;;;;&$Xxxx++++++X                        
                                      &+;;;;;;;;Xxxxxxxxxx;;;;;+&Xxxx++++++X                        
                                    X&;;;;;;;;;$xxx+++x;+Xx;;;;;+&xx+++++++X                        
                                   $&;;;;;;;;;$xx+++x;++x;X;;;;;;+&Xx++++++X                        
                                 X&X;;;;;;;;;$xx++xXXx++x;x+;;;;;;;&Xx+++++X                        
                               &&X;;;;;;;;;;XxX&Xxxxxxx$&XX$;;;;;;;;X&X+++x$                        
                    &&&&&&$$$&x;;;;;;;;;;;;$x&XXX&&&&&$Xxx&XX;;;;;;;;;X&x+$     &&$$$$              
                 &X;;;;;;;;;;;;;;;;;;;;;;;$x&XX&&&&&&&&&$Xx$Xx;;;;;;;;;;;x$&&$x;;;;;;;&$  XXXX$     
               X$;;;;;;;;;;;;;;;;;;;;;;;+$x$$X&&&&&&&&&&&XX$XXX;;;;;;;;;;;;;;;;;;;;;;;+$  X$XX$     
               $x;;;;;;;;;;;;;;;;;;;;;;x$xx$$x&&&&&&&&&&&$X&x+x$+;;;;;;;;;;;;;;;;;;;;;;&xxxXXXX     
               $X;;;;;;;;;;;;;;;;;;;;;XXxx+x&XX&&&&&&&&&&XX&+++xX$+;;;;;;;;;;;;;;;;;;;+$xX $X       
                $+;;;;;;;;;;;;;;;;;;x$xx++++x&Xx$&&&&&&XXX&++x::xxX$+;;;;;;;;;;;;;;;;;&&XXXXX$      
                X&+;;;;;;;;;;;;;;;x$xx+++++++xX&$XXXXXX$&X+x;;++x+xxx$X;;;;;;;;;;;;;+$XXXXX$$       
                  $$$x;;;;;;;+x$$Xxx++++++x+x++xxxXXXXxx++++x;;x;:xx+xxX$$x;;;;;;+X$& $&$$$         
         XxxXx$$$     XXXXXXxxxxxx++++++xx+;;;;x+++++++++++++xxx+x+++++++xx&&&&$$   $$X;;+$$        
          XxxxX$      Xxxxxxxxxxx+++++++x;++xx$$XXxxX$Xxx+++++++++++++++++++&&     $X X$$+;;&&&     
            xxx+X    $xxxxxx+++++++++++++x$+;;;;;;;;;;;;;+&x+++++++++++++++++&X    XX X+;$;;+&&     
            XXxxxx  $xxx++x+++++xX+++++x$;;;;;+$&&&&&$x;;;;;Xx++++++++++++++++$&    XxxXxx;x$$      
              XXXX+$x;;+Xx;;++XX;;&+++$+;;;x&&$$$XXXXX$$&$+;;+$+++++++++++++++X$&   &&Xxx;;+$X      
              XXX+xx;x&&&&&&;++++;&++$;;;+&$XXXXXXXXXXXXXX&X;;+$++++++++++++x:++x&    && &$&&       
              $xXxx+x&&&&&&&&;x++;$+X+;;x&XXXXXXXX:::+XXXXX$&;;x$++x+&&+$&+xx$;;+x&                 
              XxX+;;$&&&&&&&&++;;;$x$;;;&XXXX;:::;;+;;;;+XX$$x;;&+x;x$X;$&&++xXX++$&                
              $x$;;+X&&&&&&&&+x+++$XX;;x&XXXX;::++;;;X:::XXX&Xx;$xX;&&x+&$X;+x++++x&                
             $XXX+;x+&&&&&&&x+x;;xxXX;;+&XXXXX$;;X++xx;xXXX$xxX+&+xx;&+X&$++x+++++x&                
            &XxX&&$xX+x&&&$;+X+;+$++&;;;$XXXX$+:::;;:::XXXX$&$XXX++xXX+++xX+++++++x&                
           $$$& &XxxxxXX++XX+++x$x++XX;;;&$$XXX$&XX&+;XXXXX&+;+$+++++++++++++++++x$&                
           &XX   $xxxxxx+++++++++++++X$;;;x&XXXXXXXXXXXXX&X;;x$++X+++++++++++++xxx&&                
       &&&&&&&&&&&$xxxxxxxxxx+++++++++x&x;;;+X$$XXXXX$&X+;;+&XXXX+xxX$$X++++++xxx$&                 
       &$&&&&&&&&&&Xxxxxxxxxx++++++++++xX&X+;;;;;;;;;;;;+X&XxX+xX$+X&&$$+++$X+x$$&                  
      &&$$XXXXXXXX$&$xxxxxxxx++++++xx++;:;XX&&$xx++xx$&&Xxx++xx+x+$x++$$$$$$$xX$&&                  
      &$$&$$$&$$$&$$$&xxxxxxxx+++++x;+xX;xxx$++++xxxxxx++xXX$+X&+X$+++$$$$$$$$$$$$&                 
      &&$&$$$&$$$&$$  &$xxxxxxxxxxx+X;+XXX$xxxX$$$$&&$$$XXx+Xx&X+&&&&&&$$xxx$$$$$++$                
       &$$$XXXXXXX$$    &$xxxxxxxxxxxxxxxxX;;;;;;;;;;;;;;;;;+&&xX&xx$&&&$+++x$$$&&&&&               
       &$$&$$&$$$&$&      &&XxxxxxxxxxxxxXX++++++++++++++++++$&+X&Xx$&&&&&$&&&&X++X&&               
         &&&&&&$&&$           &&Xxxxxxx$X++;;;;++xxX$$$$$Xx+;;;$&&&&&&&&&&&&&&&$++$&&               
                                   &&&&+;;;;;;;;;;;;;;;;;;;;;;;;$&&&&&&&&&&&&&&&&&&&                
                                      $+;;;;;;;;;;;;;;;;;;;;;;;;$&&&&&&&&&&&&&&&&&&                 
                                      $;;;;;;;;;;;;;;;;;;+++xxxx$$                                  
                                       $                                                            
                                                                                                    """
    lines = e.split('\n')
    for line in lines:
        print(line)
    print("")
    prs("Крош проходит по тропинке прямиком к Нюше. Рядом с её домиком никого не было. это было очень странно.")
    prs("Дойдя до двери кролик отворив её видит как Нюша есть очередное ведро конфет.")
    prs("- Нюша, пойдем. Капиталисты вернулись, они повсюду, они на деревьях!")
    prs("Убрав конфеты Нюша пошла с Крошем. Она был готова помочь своим друзьям. Она вышла из своего дома")
    print("")
    print("Что будете делать?")
    print("")
    print("1. Надо бежать к Ёжидзе, вдруг с ним что-то случилось! Он может быть в опасности!")
    print("2. Первым делом лучше пойти к Лосяшу, он умный и что-нибуть придумает.")
    print("3. Пин! Наш техник точно смастерит полезную штуковину")
    print("4. Нюша, оставила свои конфеты, может взять парочку?")
    krosh.revpoint += 1
    krosh.teams.append(["Нюша"])
    choise = input("Выберите ответ (1-4): ")

    if choise == "1":
        home_ezik()
    elif choise == "2":
        home_los()
    elif choise == "3":
        home_pin()
    else:
        krosh.kappoint += 1
        konfet()

#Конфеты
def konfet():
    os.system('cls')
    prs("Ты поддался соблазну и все-таки забрал нюшины конфеты!")
    prs("+  Конфеты \n Добавлена способность «Лечение»")
    krosh.items.extend(["конфеты"])
    krosh.kappoint += 1
    print("Куда теперь?")
    print("")
    print("1. Надо бежать к Ёжидзе, вдруг с ним что-то случилось! Он может быть в опасности!")
    print("2. Первым делом лучше пойти к Лосяшу, он умный и что-нибуть придумает.")
    print("3. Пин! Наш техник точно смастерит полезную штуковину")
    
    choise = input("Введите ответ (1-3): ")
    if choise == "1":
        home_ezik()
    elif choise == "2":
        home_los()
    elif choise == "3":
        home_pin()
    else:
        home_pin()

#Дом Пина 1 часть
def home_pin():
    os.system('cls')
    t = """                                                                                                    
                                                   &&&&&           $$$$$$ $$$$$$$$$                 
                                        &&$&   &&&&&&$x$     $$$$  $$$$$$$$$$ $$$$$                 
                                        &$$$&  &$xX &&&&    $$$$$$$ $$$    $  $$                    
                                        &&$$$$$&XxX$          $$$ $$$  $$$$$$                       
                                     &&$$$$$$$$&X+X&&               $                               
                                   &&$$$$$$$$$$$x+X$$&&             $                               
                                 &$$$$$$X$&$$$&$++X&$$$$$&&$$&&&&&&&$                               
                               &&$$$$$$$$$$$$$&X++X&$$$$$&$$$$$$XX$$&                               
                   X          &$$$$$XX&$$$$$&$&$xX&X$$$$&$$$$$$XXXX&$&                              
                 $xxX&&      &$$$$$X$$$$$$$$$XX$$Xx&$X&$$$$$&XXXX&$XXX&                             
                &&$$$X&&&     &$$$$&$$$$$$$$$$&Xx&$$$&$$$$&$XXX$&&$&XXX$&                           
                &&  $xxx&&&    &$$&$$$$$X$&$$$$$$$X&$$$$$&XXXX&xxXXX&$XXX&                          
                &&  &$xxxx$&&&  &&&$$$$$&$$$$$$$X$&$$$$&$XXX$X$$$&Xx$$$XXX&&                        
                &&    &Xxxxx&&&&$&$&$$&$$$$$$$$X&$$$$$&XXXX&+&Xxx+x++$$$XXX&                        
                &&     &$xxxxx&$xX&X$$$XX$$&&&&$$$$$$$XXX$X++++X&&$X++$&XX$&&                       
                &&      &&Xxxxx&XXXXXXXXXXXXXX$$&$$$$XXX$x+++x$&X+++++$&&&&&         &&&            
                &&        &&Xx&$XXXX++x$$x+x$$X$X&&XXXX$+++++$$X++++xX$$$$$&&    &&& &&$&&          
                &&       &&X$&XXX&X$X&&&&&$$$$XXXXX$&&&$X+++++x+++++xX$XXXXX$&  &$&&&&$X&&          
               &$&      &&XXXXXXXX++&&&&&&&xxx$XXX&&&$$&X$X+++++++x$X&XXXXXXX&& &&$$$X$&&           
             $$X&$X     &$XXXXXX$$xx$&&&&&&XX$XX$$$&$$&$$&$$$$$$$$$&XXXXXXXXXX&    &&$$&&           
             &$XXX&     &$$&$X$$XX&x++X&$XXxX&X$X&&&&&$$&XXXX$&$$XXXXX+++x$XXX&&&XX$$&$$&&          
               &X&     &&$$$XXXXXXX$&XXxxX&$X$$X&&&&&&$&$XXXXXXXXXXX+&&x&&$X$X$&&&&& &$XXXX&&       
              &x$&&&   &&$$$$XXXXXXXXxXXXXX$XX$$$&&&$$&XXXXXXXX$XXXx&&&XXxxX$X$&    &&$&&&$X&&      
             &$&&XX&   &$$$$$XXXXXXXXXXXXXXXXXXX&&$&&$XXXXXXXXXXXX$x$xXXX&&X$$$&    &$$&$& &&&      
              &XxX&&   &&$$$$XXXXXXXXXXXXXXXXXXXXxXX$&&&&&&&&$$XXXX$x&&&+&$X$$$&      &&&&          
                &&     &&$$&&&&&&&&$XXXXXXXXXXXXX$&$$$$$&&&&$&X&&XXX$$xxxX&$$$$&                    
                        &$&&$&&&&&&&&&&&XXXXXXX$&$$&&&&&&$$&&&&&$&$XXXXXXXX$X$$$X&$                 
                        &&&&$&&&&&&&&&&&XXXXXX$&$$&&&&$$$$$&$$$&&&$&XXXXXX$x$X$x&xX$                
                         &&&$&&&&&&&&&&&XXXXX$&&$&&$$$$$&$$$$$&&&&$&&XXXX$$x&&X&xx&&$               
                         &&&$&&&&&&&&&&&XXXXX&&$&&&$$$&$$$$&&&&&&&&&&XXXX&x$$&X&x$&                 
                          &&$&&&&&&&&&&&XXXX$&&$&&&$$$&$&&$&&$$&&&&$&$XXX&x$$&X&x&&                 
                   &&&$&    &&&&&&&&&&&&XXXX$&&$&&$&$&&&&&&&&&&&&&&$&$XX$$&$&$&&&&&                 
                  &$x+xxxxX&&&&&&&&&&&&&&XXX$&&$$&&$$$&$&$&&&$$$&&&&&$$$$&        &                 
                  &&$$&&$xxX$&$$$&&&&&&&&XXXX$&&$&&&&$&&$$&&&$&&&&$&&$$&&         &                 
                  &&$$$$$$&XX$XXXXX$$$$&&&XXX$$&&$$&&$$&&&&&&&&&&$&&$&&          &&&&&              
                    &$$$$$&$XX$XxxXXXX&$XX&$XX$$&&&$$&&&&&&&&&&$$&&&XXX&        &&  &&&&            
                     &&$$$$&$XXXX$$$XXXX$&$$$$$$$&&&&$&$$$&X&$$&&&&XXxX$        &$$$$$$$&           
                       &&&&$$&&$XXXXX$&$XX$&&&&&$$$$&&&&&&&&&&$&  &$xxx$        &$$$&&&&            
                                   $XXXXXXX$           $XXXXxxx$&&&$$XXX&                           
                                  &Xxxxxxx$&    &&&&&&$XXXXX$xXXxxxxXXXXX&&                         
                                 &$XxxxxX$&&$$XXxxxxxXXXX$$X&x$X$$XXXXXXX&&                         
                                &$XXX$$XxxxXXXxxxXXXXXXXX$$X&x$XXXXXXX$&$&&                         
                                &XXx&XXXXXXXXXXXXXXXXXXXXX$&XxxX&&&&&XXXxx&                         
                               &$XXx&$$XXXXXXXXXXX$&&&&&$XXXxxxX&   &XXxxx$&                        
                              &&XXXx$$$$&&&&&&&&&      &XXXXxxxx&   &$XXxxX&                        
                              &$XXXxxxxx&&             &XXXXxxxx&   &&XXxxxX&                       
                              &XXXXxxxxX&             &&XXXXxxxx$&   &XXXxxx$&                      
                              &XXXXxxxX&              &&XXXXxxxxX&   &&XXxxxX&                      
                             &&XXXXXxx$&              &&XXXXXxxxX&    &$XXxxx$&                     
                              &&$$$$X$&               &&XXXXXXxxx&&   &&XXXXX&&                     
                                                      &&XXXXXXXxxX&    &&&&&&                       
                                                      &&XXXXXXX$&&&                                 
                                                       &&&&&&&&                                     
                                                                                                    """
    lines = t.split('\n')
    for line in lines:
        print(line)
    print("")
    prs("Подходя к дому Пина, Крош замечает несколько роботов, что окружили его дом. Нужно помочь Пину отбится.")
    pin_prod = input("Нужно спасти Пина! (Нажмите ENTER) ")
    
    if pin_prod == "1337":
        print("Чит-код активирован! Базовый Урон +10000")
        krosh.attack_power = 10000
        krosh.health = 10000
        time.sleep(3)
        combat_pin()
    else:
        combat_pin()

#Битва за домик Пина
def combat_pin():
    os.system('cls')
    krosh.teams.append(["Пин"])
    krosh.health = 100
    battle = Battle(["робот", "робот", "робот"], home_pin_prod, home_pin)
    battle.start_battle()
    
    
#Дом Пина 2 часть
def home_pin_prod():
    os.system('cls')
    if "Лосяш" in krosh.teams:
        print("")
        prs("Разобравшись с противниками Крош и его небольшая команда, наконец, может подняться к Пину. Взайдя на платформу под дверью, что была лифтом, они поднялись и постучали в дверь.")
        prs("-О майн год, это вы,- говорил Пин шыре открывая дверь. Он пропустил друзей к себе.")
        prs("-Что вы тут делаете в такое время? Я уже час тут сижу, а под домом эти железяки!")
        prs("-Мы по этому к тебе и пришли. К нам десантировались капиталисты, они почти повсюду. Лосяш подтвердит.")
        prs("-Все так. Дорогой мой друг это чистая правда. Их слишком много и они портят нашу экосистему,- подтвердил Лосяш.")
        prs("-И что будем делать?- спросил Пин.")
        prs("-Я предлагаю все решить мирным путем, дипломатией,- подтвердил ученый.")
        prs("-Найн, как по мне лучше всего сделать оружие против этого врага. Тогда мы сможем избавится от них навсегда!")
        prs("-Друг мой, скажите как вы считаете какой план лучше?- спросил Лосяш Кроша.")
        print("")
        print("1. Пин прав, нельзя с ними договорится, проблему можно решить только создав оружие.")
        print("2. Прав Лосяш, мы должны попробовать с ними договорится.")
        print("")
        krosh.teams.append("Пин")
        krosh.revpoint += 1
        choise = input("Выберите ответ (1-2): ")
        if choise == "1":
            zd_pin()
        else:
            end_los()
    else:
        print("")
        prs("Разобравшись с противниками Крош, наконец, может подняться к Пину. Взайдя на платформу под дверью, что была лифтом, он поднялcя и постучал в дверь.")
        prs("-О майн год, я думал железяки поняли как пользоваться лифтом,- сказав это Крош прошел внутрь дома.")
        prs("-Что происходит? Я тут уже час сижу и выйти не могу. ")
        prs("-Я по этому к тебе и пришел. К нам десантировались капиталисты, они почти повсюду. Мне нужна твоя помощь.")
        prs("-Похоже придется выкинуть этих капиталистов с нашего острова.")
        print("")
        prs("Спустившись на улицу Крош заметил как около гаража Пина прячится Бараш. Увидев, что роботы ушли он стал понемногу выходить из укрытия.")
        print("")
        print("Как вы поступите?")
        print("")
        print("1. Лучше взять Бараша с собой, вместе мы сильнее.")
        print("2. Баран будет только нам мешать, оставим его.")
        choise = input("Выберите ответ (1-2): ")
        krosh.teams.append("Пин")
        if choise == "1":
            krosh.revpoint += 1
            krosh.teams.append(["Бараш"])
            home_los()
        else:
            krosh.kappoint += 1
            home_los()

#Задание Пина
def zd_pin():
    os.system('cls')
    print(" ")
    prs("Пин отправил Кроша в лес, чтобы он сразился там с несколькими работами и раздобыл с них деталей для нового изобретения Пина")
    print(" ")

    def volna1():
        krosh.health = 100
        print("=== ВОЛНА 1 ===")
        battle = Battle(["робот"], volna2, zd_pin)
        battle.start_battle()

    def volna2():
        krosh.health = 100
        print("=== ВОЛНА 2 ===")
        battle = Battle(["робот", "робот"], volna3, zd_pin)
        battle.start_battle()

    def volna3():
        krosh.health = 100
        print("=== ВОЛНА 3 ===")
        battle = Battle(["робот", "робот", "робот"], final_boss, zd_pin)
        battle.start_battle()
    
    volna1()

#Секретная концовка
def end_home():
    os.system('cls')
    print("")
    prs("Крош остался дома. Он не стал выходить на улицу и смотреть, что там происходит. Он снял фуражку и лег на постель. Пока он спал его друзей захватили, а их остров приватизировали себе.\n\nПоздравляем вы открыли секретную концовку!")
    end = input("Нажмите [ENTER] для продолжения")
    time.sleep(3)

#Концовки по Лосяшу
def end_los():
    os.system('cls')
    if krosh.revpoint == 5:
        print("")
        prs("Крош с друзьями собрались у коробля,который стоял в порту. На нем был главнокомандующий всей операцией по захвату острова. Обойдя охрану они смогли пройти к нему, к тому кто все это начал. Лосяш как дипломат начал переговоры с главнокомандующим. По итогу они смогли договорится на хорошие условия. Смешарики остаются на острове и спокойно на нем живут, а люди с острова буду понемногу добывать ресурсы здешних земель. Крош не мог сказать, что рад результату, но это лучше чем ничего.\n\nПоздравляем вы вышли на дипломатическую-нейтральную концовку!")
        end = input("Нажмите [ENTER] для продолжения")
        time.sleep(3)
    elif krosh.revpoint < 5:
        print("")
        prs("Крош с друзьями собрались у коробля,который стоял в порту. На нем был главнокомандующий всей операцией по захвату острова. Обойдя охрану они смогли пройти к нему, к тому кто все это начал. Лосяш как дипломат начал переговоры с главнокомандующим. По итогу переговоров они не смогли договорится и всех захватили. Теперь они были одними из рабочих в городе, а их остров превратили в самое обычное место откуда жадно качают ресурсы. Крош сильно расстроился.\n\nПоздравляем вы вышли на дипломотическую-плохую концовку!")
        end = input("Нажмите [ENTER] для продолжения")
        time.sleep(3)
    elif krosh.kappoint == 3:
        print("")
        prs("Крош с друзьями собрались у коробля,который стоял в порту. На нем был главнокомандующий всей операцией по захвату острова. Крош один прошел к главнокомандующему и сдал своих друзей капиталистам. Он решил поменять сторону, Крош понял, что коммунизм, который устоялся у них на острове ему, не нравится и стоит принять капитализм. Так Крош стал одним из офицерров операции по захвату острова и помог забрать остальных, кто прятался. В городе он получил квартиру за свои заслуги, служа на морском флоте.\n\nПоздравляем вы вышли на капиталистическую концовку!")
        end = input("Нажмите [ENTER] для продолжения")
        time.sleep(3)

#Финальный босс
def final_boss():
    os.system('cls')
    prs("Крош с командой пришли к кораблю капиталистов и вспупились с ними в финальную битву.\n\nЗдоровье возросло до 200, урон до 40.")

    def volna1():
        krosh.health = 250
        krosh.attack_power = 40

        print("=== ВОЛНА 1 ===")
        battle = Battle(["робот"], volna2, final_boss)
        battle.start_battle()
    
    def volna2():
        krosh.health = 250
        krosh.attack_power = 40

        print("=== ВОЛНА 2 ===")
        battle = Battle(["робот", "робот"], volna3, final_boss)
        battle.start_battle()
    
    def volna3():
        krosh.health = 250
        krosh.attack_power = 40

        print("=== ВОЛНА 3 ===")
        battle = Battle(["робот", "робот", "робот"], volna4, final_boss)
        battle.start_battle()
    
    def volna4():
        krosh.health = 250
        krosh.attack_power = 40
        print("=== ВОЛНА 4 ===")
        battle = Battle(["оптимизатор", "оптимизатор"], volna5, final_boss)
        battle.start_battle()
    
    def volna5():
        krosh.health = 250
        krosh.attack_power = 40

        print("=== ФИНАЛЬНАЯ ВОЛНА ===")
        battle = Battle(["оптимизатор", "оптимизатор", "оптимизатор"], end_pin, final_boss)
        battle.start_battle()
    
    volna1()

#Концовки по Пину
def end_pin():
    os.system('cls')
    if krosh.kappoint == 3:
        print("")
        prs("Крош с друзьями собрались у коробля,который стоял в порту. На нем был главнокомандующий всей операцией по захвату острова. Крош один прошел к главнокомандующему и сдал своих друзей капиталистам. Он решил поменять сторону, Крош понял, что коммунизм, который устоялся у них на острове ему, не нравится и стоит принять капитализм. Так Крош стал одним из офицерров операции по захвату острова и помог забрать остальных, кто прятался. В городе он получил квартиру за свои заслуги, служа на морском флоте.\n\nПоздравляем вы вышли на капиталистическую концовку!")
        end = input("Нажмите [ENTER] для продолжения")
        time.sleep(3)
    else:
        print("")
        prs("Крош с друзьями собрались у коробля,который стоял в порту. На нем был главнокомандующий всей операцией по захвату острова. Взяв оружие, что им изготовил Пин, они изничтожили капиталистов, что были на корабле, а те что уже высадились группа вскоре нашла и точно так же искоренила с Ромашковой долины. Теперь к ним не кто не сунется, они могут за себя постоять.\n\nПоздровляем вы вышли на военную концовку! ")
        end = input("Нажмите [ENTER] для продолжения")
        time.sleep(3)

#Главное меню
def main_menu():
    print("")
    print("1. Новая Игра")
    print("2. Краткий гайд по игре")

    zapros = str(input("Введите значение: "))
    if zapros == "1":
        home()
    elif zapros == "2":
        prs("")
        prs("Comradiki (рус. Комрадики) — это классический текстовый квест с разветвленным сюжетом на несколько концовок и увлекательной боевкой")
        prs("От каждого вашего (даже самого незначительного (!) выбора зависит итоговая концовка, поэтому будьте внимательны к принимаемым вашим решениям и их потенциальным последствиям)")
        prs("Суммарное время на прохождение всей игры на все возможные концовки — ~1 час")
        prs("Удачи!")
        prs("")
        prs("©Создатели игры: Якунин Кирилл и Горбов Данил из ПР24-04")
        prs("")
        prs("")
        prs("")
        prs("")
        prs("")
        prs("")
        go_menu = input("Нажмите [ENTER], чтобы вернуться в главное меню ")
        
        if go_menu == "1337":
            print("Ах, да. Читы активируются с помощью кода «1337»")
            time.sleep(3)
            os.system('cls')
            main_menu()
        else:
            os.system('cls')
            main_menu()  
    else:
        home()


main_menu()
