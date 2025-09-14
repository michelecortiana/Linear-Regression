import pandas as pd
import matplotlib.pyplot as plt

#Funzione di errore (Mean Squared Error)
def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].studytime   #Valore di x (tempo di studio)
        y = points.iloc[i].score       #Valore di y (punteggio)
        #Calcolo dell'errore quadratico per ogni punto rispetto alla retta y = mx + b
        total_error += (y - (m * x + b)) ** 2
    #Restituzione dell'errore medio
    return total_error / float(len(points))

#Algoritmo di gradient_descent per l’aggiornamento dei parametri m e b
def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)  #Numero di punti nel dataset

    for i in range(n):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        #Calcolo del gradiente (derivata parziale della funzione di errore)
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    #Aggiornamento dei parametri sulla base del gradiente calcolato
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

def main():
    #Lettura del dataset da un file CSV che contiene almeno due colonne:
    #"studytime" (tempo di studio) e "score" (punteggio)
    data = pd.read_csv('data.csv')

    #Parametri iniziali
    m = 0   #Coefficiente angolare della retta
    b = 0   #Intercetta della retta
    L = 0.0001   #Learning rate (ampiezza del passo di aggiornamento)
    epochs = 300 #Numero di iterazioni

    #Esecuzione della discesa del gradiente per più epoche
    for i in range(epochs):
        if i % 50 == 0:
            # Stato della funzione di errore ogni 50 epoche
            print(f"Epoch: {i}, Errore: {loss_function(m, b, data):.2f}")
        m, b = gradient_descent(m, b, data, L)

    #Parametri finali della retta
    print("Valori finali:", m, b)

    #Visualizzazione dei dati originali (punti neri) e della retta stimata (rossa)
    plt.scatter(data.studytime, data.score, color="black")  # dati reali
    plt.plot(list(range(20, 80)), [m*x + b for x in range(20, 80)], color="red")  # retta stimata
    plt.xlabel("Tempo di studio")
    plt.ylabel("Punteggio")
    plt.title("Risultato della Regressione Lineare")
    plt.show()

if __name__ == "__main__":
    main()