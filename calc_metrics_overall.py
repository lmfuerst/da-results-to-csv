from datetime import datetime
import pandas as pd
import numpy as np
import csv
import time

basename = "results_2025_agg"

if __name__ == "__main__":
    time_milli = round(time.time() * 1000)
    cur_time = datetime.fromtimestamp(time_milli / 1000.0)
    df = pd.read_csv(basename + ".csv", sep=";")
    # Accuracy = (tp + tn) / (tp + tn + fn + fp)
    # Precision = tp / (tp + fp)
    # Recall = tp / (tp + fn)
    # Specificity = tn / (tn + fp)
    tools = ["ethor-2023", "mythril-0.23.15", "oyente", "sailfish"]
    print(len(df))

    df["error"] = np.where(df["insecure"] == "", 1, df["error"])

    df["tp"] = np.where((df["ground_truth"] == 1) & (df["insecure"] == 1), 1, 0)
    df["fp"] = np.where((df["ground_truth"] == 0) & (df["insecure"] == 1), 1, 0)
    df["tn"] = np.where((df["ground_truth"] == 0) & (df["insecure"] == 0), 1, 0)
    df["fn"] = np.where((df["ground_truth"] == 1) & (df["insecure"] == 0), 1, 0)

    # ignore rows where error==1
    df["tp"] = np.where(df["error"] == 1, 0, df["tp"])
    df["fp"] = np.where(df["error"] == 1, 0, df["fp"])
    df["tn"] = np.where(df["error"] == 1, 0, df["tn"])
    df["fn"] = np.where(df["error"] == 1, 0, df["fn"])

    df["tp"] = df["tp"].fillna(0)
    df["fp"] = df["fp"].fillna(0)
    df["tn"] = df["tn"].fillna(0)
    df["fn"] = df["fn"].fillna(0)

    count_tp = df["tp"].astype(int).sum()
    count_fp = df["fp"].astype(int).sum()
    count_tn = df["tn"].astype(int).sum()
    count_fn = df["fn"].astype(int).sum()
    count_error = df["error"].sum()
    count_total = count_tp + count_tn + count_fp + count_fn + count_error
    print(count_total)

    count_total_wo_error = count_tp + count_tn + count_fp + count_fn
    count_total_w_error = count_total_wo_error + count_error

    accuracy_wo_error = (count_tp + count_tn) / count_total_wo_error
    accuracy_w_error = (count_tp + count_tn) / count_total_w_error
    precision = count_tp / (count_tp + count_fp)
    recall = count_tp / (count_tp + count_fn)
    specificity = count_tn / (count_tn + count_fp)
    error_rate = count_error / count_total

    with open(basename + "_metrics.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';',
                                fieldnames=["time", "type", "Accuracy w/o error", "Accuracy w/ error", "Precision", "Recall",
                                            "Specificity", "Error rate", "TP", "FP", "TN", "FN", "Error", "Total"])
        writer.writeheader()
        writer.writerow({"time": cur_time, "type": "total", "Accuracy w/o error": accuracy_wo_error, "Accuracy w/ error": accuracy_w_error,
                         "Precision": precision, "Recall": recall, "Specificity": specificity, "Error rate": error_rate,
                         "TP": count_tp, "FP": count_fp, "TN": count_tn, "FN": count_fn, "Error": count_error, "Total": count_total})

    for tool in tools:
        print(tool)
        data = df[df["tool"] == tool]
        print(len(data))
        data = data.copy()

        data["tp"] = np.where((data["ground_truth"] == 1) & (data["insecure"] == 1), 1, 0)
        data["fp"] = np.where((data["ground_truth"] == 0) & (data["insecure"] == 1), 1, 0)
        data["tn"] = np.where((data["ground_truth"] == 0) & (data["insecure"] == 0), 1, 0)
        data["fn"] = np.where((data["ground_truth"] == 1) & (data["insecure"] == 0), 1, 0)

        data["tp"] = np.where(data["error"] == 1, 0, data["tp"])
        data["fp"] = np.where(data["error"] == 1, 0, data["fp"])
        data["tn"] = np.where(data["error"] == 1, 0, data["tn"])
        data["fn"] = np.where(data["error"] == 1, 0, data["fn"])

        data["tp"] = data["tp"].fillna(0)
        data["fp"] = data["fp"].fillna(0)
        data["tn"] = data["tn"].fillna(0)
        data["fn"] = data["fn"].fillna(0)

        count_tp = data["tp"].astype(int).sum()
        count_fp = data["fp"].astype(int).sum()
        count_tn = data["tn"].astype(int).sum()
        count_fn = data["fn"].astype(int).sum()
        count_error = data["error"].sum()
        count_total = count_tp + count_tn + count_fp + count_fn + count_error

        print(count_tp)
        print(count_tn)
        print(count_fp)
        print(count_fn)
        print(count_error)

        count_total_wo_error = count_tp + count_tn + count_fp + count_fn

        accuracy_wo_error = (count_tp + count_tn) / count_total_wo_error
        accuracy_w_error = (count_tp + count_tn) / count_total
        precision = count_tp / (count_tp + count_fp)
        recall = count_tp / (count_tp + count_fn)
        specificity = count_tn / (count_tn + count_fp)
        error_rate = count_error / count_total

        with open(basename + "_metrics.csv", 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';',
                                    fieldnames=["time", "type", "Accuracy w/o error", "Accuracy w/ error", "Precision", "Recall",
                                                "Specificity", "Error rate", "TP", "FP", "TN", "FN", "Error", "Total"])
            writer.writerow({"time": cur_time, "type": tool, "Accuracy w/o error": accuracy_wo_error, "Accuracy w/ error": accuracy_w_error,
                             "Precision": precision, "Recall": recall, "Specificity": specificity, "Error rate": error_rate,
                             "TP": count_tp, "FP": count_fp, "TN": count_tn, "FN": count_fn, "Error": count_error, "Total": count_total})