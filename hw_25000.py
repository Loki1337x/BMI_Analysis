import pandas as pd
import matplotlib.pyplot as plt

name = 'hw_25000.csv'
file = pd.read_csv(name)

file = file.dropna()

file["Height(Meters)"] = file[' "Height(Inches)"'] * 0.0254

file["Weight(Kilograms)"] = file[' "Weight(Pounds)"'] * 0.453592

file = file[["Height(Meters)", "Weight(Kilograms)"]]

file["BMI"] = file["Weight(Kilograms)"] / (file["Height(Meters)"] ** 2)

file["Height(Meters)"].plot.hist(label='Height in meters', bins=25)

plt.axvline(file["Height(Meters)"].mean(), color='red', linestyle='--', label=f"Average({round(file['Height(Meters)'].mean(), 5)})")
plt.ylabel("Quantity")
plt.xlabel("Height in meters")
plt.title("Height in a group of 25 thousand people")
plt.legend()
plt.show()


good = (18.5 , 24.9)
file["BMI"].plot.hist(bins=25)
plt.axvline(good[0], color='green', linestyle='--', label='Correct weight from')
plt.axvline(good[1], color='green', linestyle='--', label='Correct weight to')
plt.ylabel("Quantity")
plt.xlabel("BMI (Weight to Height)")
plt.title("BMI chart")
plt.legend()
plt.show()

