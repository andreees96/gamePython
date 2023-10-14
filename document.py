import random

###INGRESO DE OPCIONES###
def choose_option():
    options = ('piedra','papel','tijera','salir')
    
    while True:
        try:
            user_option = input("Elige Piedra, Papel o Tijera => ")
            user_option = user_option.lower()
            
            if not user_option in options:
                raise ValueError("Opción inálida\n")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    
    computer_option = random.choice(options)
    
    print("\n·Tu elección =>", user_option)
    print("·Elección de la máquina =>", computer_option)
    return user_option, computer_option

###LOGICA DEL JUEGO###
def rules(user_option, computer_option, user_win, computer_win):
    win = "\n¡¡Haz ganado!!"
    loose = "\n¡¡Haz perdido!!"
    tie = "\n¡¡Empate!!"
    
    results_map = {
        ("tijera", "papel") : win,
        ("papel", "piedra") : win,
        ("piedra", "tijera"): win,
        ("piedra","peidra") : tie, 
        ("papel", "papel")  : tie, 
        ("tijera","tijera") : tie
    }
    
    result = results_map.get((user_option,computer_option))
    
    if result == win or result == tie:
        print(result)
        if result == win:
            user_win += 1
    else:
        print(loose)
        computer_win +=1
    
    return user_win, computer_win

###EJECUCION DEL JUEGO###
def rungame():
    user_win = 0
    computer_win = 0
    round = 1
    
    while round <= 5:
        print(f"\n******\nRonda {round}")
        print(f"******\nMarcador: Usuario {user_win} - {computer_win} Computadora")

        #llamado a las funciones
        user_option, computer_option = choose_option()
        
        if user_option.lower() == "salir":
            break
        
        user_win, computer_win = rules(user_option,computer_option,user_win,computer_win)
        round += 1

    #comprueba el ganador
    if user_win >= computer_win:
        print(f"******\nCampeón: Usario con {user_win} puntos")
    elif user_win == computer_win:
        print("******\nEmpate")
    else:
        print(f"******\nCampeón: Computadora con {computer_win} puntos")



        
if __name__ == "__main__":
    rungame()