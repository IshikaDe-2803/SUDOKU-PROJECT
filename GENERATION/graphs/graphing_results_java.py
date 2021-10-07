
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

#JAVA
# EASY = [0.0259, 18.2688]
# MEDIUM = [0.2556, 65.0726]
# HARD = [0.3961, 83.3507]

#C++
# EASY = [30.9598, 41.8319]
# MEDIUM = [66.8602, 253.8408]
# HARD = [175.5002, 6520.2295]
EASY = [0.0230, 1.1129]
MEDIUM = [0.0795, 21.4268]
HARD = [0.2391, 48.8923]


#PYTHON
# EASY = [30.9598, 41.8319]
# MEDIUM = [66.8602, 253.8408]
# HARD = [175.5002, 6520.2295]
 


# Set position of bar on X axis
bar_easy = np.arange(len(EASY))
bar_medium = [x + barWidth for x in bar_easy]
bar_hard = [x + barWidth for x in bar_medium]
 
# Make the plot
plt.bar(bar_easy, EASY, color ='aquamarine', width = barWidth,
        edgecolor ='grey', label ='EASY')
plt.bar(bar_medium, MEDIUM, color ='turquoise', width = barWidth,
        edgecolor ='grey', label ='MEDIUM')
plt.bar(bar_hard, HARD, color ='lightseagreen', width = barWidth,
        edgecolor ='grey', label ='HARD')
 
# Adding Xticks
plt.title("AVERAGE TIME TO SOLVE A SUDOKU (C++)")
plt.xlabel('Algorithms', fontweight ='bold', fontsize = 15)
plt.ylabel('Time Taken (milliseconts)', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(EASY))],
        ['Backtracking', 'Brute-Force'])
 
plt.legend()
plt.show()

# 23011.11111
# 79527.77778
# 783750
