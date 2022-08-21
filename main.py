import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

five_data = pd.read_excel('full_data/5.xlsx')
six_data = pd.read_excel('full_data/6.xlsx')

five_data_pd = pd.DataFrame(five_data)
six_data_pd = pd.DataFrame(six_data)

five_tracker_input = five_data.loc[:, "phantom movements (input movements)"]
six_tracker_input = six_data.loc[:, "phantom movements (input movements)"]

five_times_seconds = five_data.loc[:,"Time_Relative(S)"]
five_tracker_pos = five_data.loc[:,"Tracter"]
five_tracker_vel = five_data.loc[:,"velocity"]
five_tracker_accel = five_data.loc[:,"acceleration"]

six_times_seconds = six_data.loc[:,"Time_Relative(S)"]
six_tracker_pos = six_data.loc[:,"Tracter"]
six_tracker_vel = six_data.loc[:,"velocity"]
six_tracker_accel = six_data.loc[:,"acceleration"]

five_tracker_pos_difference = five_tracker_input.subtract(five_tracker_pos)
six_tracker_pos_difference = six_tracker_input.subtract(six_tracker_pos)

print("...data read success")
fig1, axs1 = plt.subplots(2)
fig1.suptitle('Phantom Input Position - Tracker Position')
n, bins, patches = axs1[0].hist(five_tracker_pos_difference, 50, density=True, facecolor='r')
n, bins, patches = axs1[1].hist(six_tracker_pos_difference, 50, density=True, facecolor='r')
for ax in axs1.flat:
    ax.set(xlabel='times (s)', ylabel='difference (mm)')
plt.show()

fig2, axs2 = plt.subplots(2)
fig2.suptitle('Tracker Position vs Phantom Input Position')
axs2[0].scatter(five_tracker_pos, five_tracker_input)
axs2[1].scatter(six_tracker_pos, six_tracker_input)
a1, b1 = np.polyfit(five_tracker_pos.to_numpy(), five_tracker_input.to_numpy(), 1)
axs2[0].plot(five_tracker_pos.to_numpy(), a1*five_tracker_pos.to_numpy()+b1)
a2, b2 = np.polyfit(six_tracker_pos.to_numpy(), six_tracker_input.to_numpy(), 1)
axs2[1].plot(six_tracker_pos.to_numpy(), a2*six_tracker_pos.to_numpy()+b2)
for ax in axs2.flat:
    ax.set(xlabel='tracker position (mm)', ylabel='input position (mm)')
five_r_pos_v_input_correlation_matrix = np.corrcoef(five_tracker_pos.to_numpy(), five_tracker_input.to_numpy())
five_r_pos_v_input = five_r_pos_v_input_correlation_matrix[0][1]
axs2[0].text(1, 1, 'r:  ' + str(five_r_pos_v_input), fontsize=12, color='r')

six_r_pos_v_input_correlation_matrix = np.corrcoef(six_tracker_pos.to_numpy(), six_tracker_input.to_numpy())
six_r_pos_v_input = six_r_pos_v_input_correlation_matrix[0][1]
axs2[1].text(1, 1, 'r:  ' + str(six_r_pos_v_input), fontsize=12, color='r')

five_MSE = np.square(np.subtract(five_tracker_pos, five_tracker_input)).mean()
five_RMSE = math.sqrt(five_MSE)
axs2[0].text(-1, -1, 'RSME:  ' + str(five_RMSE), fontsize=12, color='r')
six_MSE = np.square(np.subtract(six_tracker_pos, six_tracker_input)).mean()
six_RMSE = math.sqrt(six_MSE)
axs2[1].text(-1, -1, 'RSME:  ' + str(six_RMSE), fontsize=12, color='r')
plt.show()


fig3, axs3 = plt.subplots(2)
fig3.suptitle('Phantom Input Position vs Tracker Position - Input Displacement')
axs3[0].scatter(five_tracker_input, five_tracker_pos_difference)
axs3[1].scatter(six_tracker_input, six_tracker_pos_difference)
a3, b3 = np.polyfit(five_tracker_input.to_numpy(), five_tracker_pos_difference.to_numpy(), 1)
axs3[0].plot(five_tracker_input.to_numpy(), a3*five_tracker_pos_difference.to_numpy()+b3)
a4, b4 = np.polyfit(six_tracker_input.to_numpy(), six_tracker_pos_difference.to_numpy(), 1)
axs3[1].plot(six_tracker_input.to_numpy(), a4*six_tracker_pos_difference.to_numpy()+b4)
for ax in axs3.flat:
    ax.set(xlabel='input displacement (mm)', ylabel='difference (mm)')
five_r_input_v_diff_correlation_matrix = np.corrcoef(five_tracker_pos.to_numpy(), five_tracker_pos_difference.to_numpy())
five_r_input_v_diff = five_r_input_v_diff_correlation_matrix[0][1]
axs3[0].text(1, 1, 'r:  ' + str(five_r_input_v_diff), fontsize=12, color='r')

six_r_input_v_diff_correlation_matrix = np.corrcoef(six_tracker_pos.to_numpy(), six_tracker_pos_difference.to_numpy())
six_r_input_v_diff = six_r_input_v_diff_correlation_matrix[0][1]
axs3[1].text(1, 1, 'r:  ' + str(six_r_input_v_diff), fontsize=12, color='r')
plt.show()
