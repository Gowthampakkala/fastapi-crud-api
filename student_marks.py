import numpy as np
marks = np.array([78,45,89,92,67,55,81,38,74,95])
print("higiest:",np.max(marks))
print("lowest:",np.min(marks))
print("top scorer:",np.max(marks))
print("avg:",np.mean(marks))
print("passed:",np.sum(marks>=40))
print("failed:",np.sum(marks<40))
print("ascending order:",np.sort(marks))