import matplotlib.pyplot as plt

contest_results={"Quadra":12,"Sally":6,"Frazer":14, "Newton":7, "Tyger":16, "Captain":15}
colors = ['orange', 'green', 'purple', 'red', 'magenta', 'cyan']
plt.bar(contest_results.keys(), contest_results.values(), color=colors)
plt.title("Bug Eating Contest:")
plt.xlabel('Salamanders')
plt.ylabel('Bugs Eaten')
plt.show()
