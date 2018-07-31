# python cointoss.py
import random
def coin():
    game_str = ''
    game_str += "Starting the program..."
    x = "tails!"
    y = "heads!"
    x_counter = 0
    y_counter = 0
    toss =  str(random.choice([x, y]))
    
    for value in range(1,101):
        game_str += "Attempt #"+str(value)+": Throwing a coin... It's a "+toss
        if toss == x:
            x_counter += 1
            game_str += "... Got "+str(x_counter)+" tail(s) so far and "+str(y_counter)+" head(s) so far\n"
        else:
            y_counter += 1
            game_str += "... Got "+str(y_counter)+" head(s) so far and "+str(x_counter)+" tail(s) so far\n"
    
    game_str += "Ending the program, thank you!"

    print game_str
coin()
