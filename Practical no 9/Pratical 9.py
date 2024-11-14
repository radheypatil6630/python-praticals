import numpy as np
import pandas as pd


arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([[11, 22, 23], [14, 35, 16], [7, 28, 9]])


df = pd.DataFrame({
    'A': [5, 6, 7, 8, 9],
    'B': [11, 12, 13, 14, 15],
    'C': [10, 20, 30, 40, 50]
})


print("1D Array:\n", arr_1d)
print("\n2D Array:\n", arr_2d)
print("\nDataFrame:\n", df)


print("\nAddition:\n", arr_1d + 10)
print("\nSubtraction:\n", arr_1d - 2)
print("\nMultiplication:\n", arr_1d * 3)
print("\nDivision:\n", arr_1d / 2)


print("\nDataFrame Addition:\n", df + 10)
print("\nDataFrame Subtraction:\n", df - 2)
print("\nDataFrame Multiplication:\n", df * 3)
print("\nDataFrame Division:\n", df / 2)


print("\nElement at index 2 of 1D Array:", arr_1d[2])
print("Element at row 1, column 2 of 2D Array:", arr_2d[1, 2])


print("\nElement at row 2, column 'B' of DataFrame:", df.loc[2, 'B'])
print("Element at row 3, column 'C' of DataFrame:", df.iloc[3, 2])


print("\nSlicing DataFrame (rows 1 to 3, columns 'A' and 'C'):\n", df.loc[1:3, ['A', 'C']])
print("Slicing DataFrame (rows 0 to 2, columns 0 to 1):\n", df.iloc[0:3, 0:2])


reshaped_arr = arr_2d.reshape(1, 9)
print("\nReshaped 2D Array to 1D:\n", reshaped_arr)


transposed_arr = arr_2d.T
print("\nTransposed 2D Array:\n", transposed_arr)


sorted_arr = np.sort(arr_1d)
print("\nSorted 1D Array:\n", sorted_arr)

df_sorted = df.sort_values(by='B', ascending=False)
print("\nSorted DataFrame by column 'B':\n", df_sorted)