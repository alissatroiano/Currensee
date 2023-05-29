import matplotlib.pyplot as plt
import csv


def plotData():

    x = []
    y = []
  
    with open('../static/data/bitcoin.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))
    
    plt.plot(x, y, color = 'g', linestyle = 'dashed',
            marker = 'o',label = "Bitcoin Data")
    
    plt.xticks(rotation = 25)
    plt.xlabel('Dates')
    plt.ylabel('Prediction($)')
    plt.title('Bitcoin Predictions', fontsize = 20)
    plt.grid()
    plt.legend()
    plt.show()
    plt.savefig('../static/images/bitcoin.png')

# call the function
plotData()

