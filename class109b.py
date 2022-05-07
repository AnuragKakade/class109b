import csv
import pandas as pd
import statistics
df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

height_std_deviation=statistics.stdev(height_list)
height_std_deviation=statistics.stdev(weight_list)

height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation
height_second_std_deviation_start,height_second_std_deviation_end=height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_third_std_deviation_start,height_third_std_deviation_end=height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)
    
height_list_of_data_within_1_std_deviation=[result for result in height_list if result>height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation=[result for result in height_list if result>height_second_std_deviation_start and result<height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation=[result for result in height_list if result>height_third_std_deviation_start and result<height_third_std_deviation_end]

print("mean,median,mode is {},{},{} and {}".format(height_mean ,height_median,height_mode,height_std_deviation))
print("mean,median,mode is {},{} and {}".format(weight_mean ,weight_median,weight_mode))

print("{} of datal;lies within one std_deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{} of datal;lies within two std_deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{} of datal;lies within three std_deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

