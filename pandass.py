import matplotlib.pyplot as plot # pyright: ignore[reportMissingModuleSource]
import pandas as pd

data = pd.read_json("/home/anubhav/tasklog.json")
data.plot()
plot.show()