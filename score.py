import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import pandas as pd

data = pd.read_csv(r"C:\Users\bhuvi\Google Drive\Code\Python\Project 109 - Normal Distribution\data.csv")
score = data["reading score"].tolist()

mean_score = sum(score) / len(score)
median_score = statistics.median(score)
mode_score = statistics.mode(score)
std_score = statistics.stdev(score)

print("Mean is {}".format(mean_score))
print("Median is {}".format(median_score))
print("Mode is {}".format(mode_score))
print("Standard Deviation is {}".format(std_score))

first_start_score = mean_score - std_score
first_end_score = mean_score + std_score
second_start_score = mean_score - (2*std_score)
second_end_score = mean_score + (2*std_score)
third_start_score = mean_score - (3*std_score)
third_end_score = mean_score + (3*std_score)

first_score = [score for score in score if score > first_start_score and score < first_end_score]
second_score = [score for score in score if score > second_start_score and score < second_end_score]
third_score = [score for score in score if score > third_start_score and score < third_end_score]

print(" ")
print("Score that lies in the first standard deviation = {} %".format((len(first_score)*100)/len(score)))
print("Score that lies in the second standard deviation = {} %".format((len(second_score)*100)/len(score)))
print("Score that lies in the third standard deviation = {} %".format((len(third_score)*100)/len(score)))