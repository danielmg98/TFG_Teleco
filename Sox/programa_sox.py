import os, sys, pysox
sample_rate = sox.file_info.sample_rate('./prueba.wav')
n_samples = sox.file_info.num_samples('./prueba.wav')
print(sample_rate)
print(n_samples)
