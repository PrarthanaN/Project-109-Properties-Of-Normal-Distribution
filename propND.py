import pandas as pd
import statistics
import csv
import plotly.figure_factory as pff

df = pd.read_csv("StudentsPerformance.csv")
ms_list = df["math score"].to_list()
rs_list = df["reading score"].to_list()
ws_list = df["writing score"].to_list()

ms_mean = statistics.mean(ms_list)
rs_mean = statistics.mean(rs_list)
ws_mean = statistics.mean(ws_list)

ms_median = statistics.median(ms_list)
rs_median = statistics.median(rs_list)
ws_median = statistics.median(ws_list)

ms_mode = statistics.mode(ms_list)
rs_mode = statistics.mode(rs_list)
ws_mode = statistics.mode(ws_list)

print("Mean, Median and Mode of Math Score is {}, {} and {} respectively".format(ms_mean, ms_median, ms_mode))
print("Mean, Median and Mode of Reading Score is {}, {} and {} respectively".format(rs_mean, rs_median, rs_mode))
print("Mean, Median and Mode of Writinging Score is {}, {} and {} respectively".format(ws_mean, ws_median, ws_mode))

ms_st_dev = statistics.stdev(ms_list)
rs_st_dev = statistics.stdev(rs_list)
ws_st_dev = statistics.stdev(ws_list)

ms_f_std_dev_st, ms_f_std_dev_end = ms_mean-ms_st_dev, ms_mean+ms_st_dev
ms_s_std_dev_st, ms_s_std_dev_end = ms_mean-(2*ms_mean-ms_st_dev), ms_mean+(2*ms_mean+ms_st_dev)
ms_t_std_dev_st, ms_t_std_dev_end = ms_mean-(3*ms_mean-ms_st_dev), ms_mean+(3*ms_mean+ms_st_dev)

rs_f_std_dev_st, rs_f_std_dev_end = rs_mean-rs_st_dev, rs_mean+rs_st_dev
rs_s_std_dev_st, rs_s_std_dev_end = rs_mean-(2*rs_mean-rs_st_dev), rs_mean+(2*rs_mean+rs_st_dev)
rs_t_std_dev_st, rs_t_std_dev_end = rs_mean-(3*rs_mean-rs_st_dev), rs_mean+(3*rs_mean+rs_st_dev)

ws_f_std_dev_st, ws_f_std_dev_end = ws_mean-ws_st_dev, ws_mean+ws_st_dev
ws_s_std_dev_st, ws_s_std_dev_end = ws_mean-(2*ws_mean-ws_st_dev), ws_mean+(2*ws_mean+ws_st_dev)
ws_t_std_dev_st, ws_t_std_dev_end = ws_mean-(3*ws_mean-ws_st_dev), ws_mean+(3*ws_mean+ws_st_dev)

ms_list_of_data_wt_1_std_dev = [result for result in ms_list if result > ms_f_std_dev_st and result < ms_f_std_dev_end]
ms_list_of_data_wt_2_std_dev = [result for result in ms_list if result > ms_s_std_dev_st and result < ms_s_std_dev_end]
ms_list_of_data_wt_3_std_dev = [result for result in ms_list if result > ms_t_std_dev_st and result < ms_t_std_dev_end]

rs_list_of_data_wt_1_std_dev = [result for result in rs_list if result > rs_f_std_dev_st and result < rs_f_std_dev_end]
rs_list_of_data_wt_2_std_dev = [result for result in rs_list if result > rs_s_std_dev_st and result < rs_s_std_dev_end]
rs_list_of_data_wt_3_std_dev = [result for result in rs_list if result > rs_t_std_dev_st and result < rs_t_std_dev_end]

ws_list_of_data_wt_1_std_dev = [result for result in ws_list if result > ws_f_std_dev_st and result < ws_f_std_dev_end]
ws_list_of_data_wt_2_std_dev = [result for result in ws_list if result > ws_s_std_dev_st and result < ws_s_std_dev_end]
ws_list_of_data_wt_3_std_dev = [result for result in ws_list if result > ws_t_std_dev_st and result < ws_t_std_dev_end]


print("{}% of data for Math Score lies within 1 standard deviation".format(len(ms_list_of_data_wt_1_std_dev)*100.0/len(ms_list)))
print("{}% of data for Math Score lies within 2 standard deviation".format(len(ms_list_of_data_wt_2_std_dev)*100.0/len(ms_list)))
print("{}% of data for Math Score lies within 3 standard deviation".format(len(ms_list_of_data_wt_3_std_dev)*100.0/len(ms_list)))

print("{}% of data for reading Score lies within 1 standard deviation".format(len(rs_list_of_data_wt_1_std_dev)*100.0/len(rs_list)))
print("{}% of data for reading Score lies within 2 standard deviation".format(len(rs_list_of_data_wt_2_std_dev)*100.0/len(rs_list)))
print("{}% of data for reading Score lies within 3 standard deviation".format(len(rs_list_of_data_wt_3_std_dev)*100.0/len(rs_list)))

print("{}% of data for Writing Score lies within 1 standard deviation".format(len(ws_list_of_data_wt_1_std_dev)*100.0/len(ws_list)))
print("{}% of data for Writing Score lies within 2 standard deviation".format(len(ws_list_of_data_wt_2_std_dev)*100.0/len(ws_list)))
print("{}% of data for Writing Score lies within 3 standard deviation".format(len(ws_list_of_data_wt_3_std_dev)*100.0/len(ws_list)))

fig = pff.create_distplot([df["reading score"].tolist()],["Reading score"],show_hist = False)
fig.show()