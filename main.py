import pandas as pd
import numpy as np
def main():
    test_data = pd.read_csv("data/test.csv")
    train_data = pd.read_csv("data/train.csv")
    train_data.dropna(how="all")
    


if __name__ == "__main__":
    main()