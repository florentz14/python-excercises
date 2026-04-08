import numpy as np
import pandas as pd


nframe = pd.DataFrame(np.arange(25).reshape(5, 5))
sampler = np.random.permutation(5)
shuffled_frame = nframe.take(sampler)

print("Original frame:")
print(nframe)
print("\nShuffled frame:")
print(shuffled_frame)
