def get_num():
    """
    Demande à l'utilisateur de saisir des nombres un par un jusqu'à ce que 'stop' soit entré.

    Retourne:
        liste: Une liste des nombres saisis par l'utilisateur.
    """
    Values_list = []
    values = input("Entrer la première valeur ou tapez 'stop' pour arreter ou 'exit' pour sortir : ").strip()
    count = 1
    while values.lower() != "stop":
        if values.lower() == "exit":
            print("Bye !")
            exit()
        try:
            values = float(values)
            Values_list.append(values)
            count+=1

            values=input(f"Entrer la {count}éme valeur ou tapez 'stop' pour arreter : ").strip()
        except ValueError:
            print("Entrée invalide")
            values=input(f"Entrer la {count}éme valeur ou tapez 'stop' pour arreter : ").strip()

    return Values_list
def operation():
    """
    Demande à l'utilisateur de choisir une opération parmi les suivantes : +, -, *, /, ou 'exit' pour quitter.

    Retourne:
        str: L'opération choisie par l'utilisateur.
    """
    operation_list = ["+","-","*","/"]
    while True:
        oper = input("Opération : (+, -, *, /) ").strip()
        if oper in operation_list:
            return oper
        elif oper.lower() == "exit":
            print("Bye !")
            exit()
        else:
            print("Opération invalide. Veuillez entrer +, -, *, / ou 'exit' pour sortir")

def calcul(x,y):
    """
    Effectue le calcul en fonction des nombres donnés et de l'opération choisie.

    Args:
        x (list): Liste des nombres sur lesquels l'opération sera effectuée.
        y (str): L'opération choisie par l'utilisateur.

    Retourne:
        float ou str: Le résultat du calcul ou un message d'erreur si la division par zéro est tentée.
    """
    if not x:
        return "no numbers entered"
    result = x[0]
    for num in x[1:]:
        if y == "+":
            result += num
        elif y == "-":
            result -= num
        elif y == "*":
            result *= num
        elif y == "/":
            try:
                result /= num
            except ZeroDivisionError:
                return "Erreur: division par 0 impossible"
    return result
def main():
    """
    Fonction principale qui demande à l'utilisateur les nombres et l'opération, effectue le calcul et affiche le résultat.
    """
    x = get_num()
    y = operation()
    result= calcul(x,y)
    print("resultat = ", result)
main()
