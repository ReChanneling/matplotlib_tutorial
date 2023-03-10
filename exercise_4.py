from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

minutes = [1,2,3,4,5,6,7,8,9]

player1 = [1,2,3,3,4,4,4,4,5]
player2 = [1,1,1,1,2,2,2,3,4]
player3 = [1,1,1,2,2,2,3,3,3]

dev1 = [8,6,5,5,4,2,1,1,0]
dev2 = [0,1,2,2,2,4,4,4,4]
dev3 = [0,1,1,1,2,2,3,3,4]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

#plt.pie([1,1,1], labels=["Player1", "Player2", "Player3"])
plt.stackplot(minutes, dev1, dev2, dev3, labels=labels, colors = colors)

plt.legend(loc='lower left')

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()