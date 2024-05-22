import pandas as pd
import numpy as np

basename = "results_13032024_bytecode"

# combine results of multi-contract analysis: considered insecure only if both contracts are detected as reentrant
if __name__ == "__main__":
    df = pd.read_csv(basename + ".csv", sep=";")
    # type == CreateBasedReentrancy or type == DelegatedReentrancy
    df.drop("name", axis=1)
    df.drop("filename", axis=1)

    aggregation_functions = {"insecure": "sum", "error": "sum", "ground_truth": "first"}
    df_new = df.groupby(["tool", "sol_version", "analysis", "type", "subtype"], as_index=False).aggregate(aggregation_functions)


    df_new["insecure"] = np.where(
        (((df_new["type"] == "CreateBasedReentrancy") | (df_new["type"] == "DelegatedReentrancy")) & df_new["analysis"] == "bytecode")
        & (df_new["insecure"] == 1), 0, df_new["insecure"]
    )
    df_new["insecure"] = np.where(((df_new["type"] == "CreateBasedReentrancy") | (df_new["type"] == "DelegatedReentrancy")) & (df_new["insecure"] == 2), 1, df_new["insecure"])
    df_new["insecure"] = df_new["insecure"].astype(int)
    df_new["error"] = np.where(df_new["error"] > 0, 1, 0)
    df_new["insecure"] = np.where(df_new["error"] == 1, "", df_new["insecure"])

    df_new.to_csv(basename + "_agg.csv", sep=";")
