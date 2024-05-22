from datetime import datetime
import pandas as pd
import numpy as np
import csv
import time

basename = "results_13032024_agg"

if __name__ == "__main__":
    time_milli = round(time.time() * 1000)
    cur_time = datetime.fromtimestamp(time_milli / 1000.0)
    df = pd.read_csv(basename + ".csv", sep=";")
    # Accuracy = (tp + tn) / (tp + tn + fn + fp)
    # Precision = tp / (tp + fp)
    # Recall = tp / (tp + fn)
    # Specificity = tn / (tn + fn)
    versions = ["v4", "v5", "v6", "v7", "v8"]
    tools = ["ethor-2023", "mythril-0.23.15", "oyente", "sailfish"]
    print(len(df))

    df["error"] = np.where(df["insecure"] == "", 1, df["error"])

    with open(basename + "_version_metrics.csv", 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';',
                                fieldnames=["Time", "Type", "Tool", "Accuracy w/o error", "Accuracy w/ error",
                                            "Precision", "Recall",
                                            "Specificity", "Error rate", "TP", "FP", "TN", "FN", "Error", "Total"])
        writer.writeheader()

    for version in versions:
        print(version)
        data = df[df["sol_version"] == version]
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
        specificity = count_tn / (count_tn + count_fn)
        error_rate = count_error / count_total

        with open(basename + "_version_metrics.csv", 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';',
                                    fieldnames=["Time", "Type", "Tool", "Accuracy w/o error", "Accuracy w/ error", "Precision", "Recall",
                                                "Specificity", "Error rate", "TP", "FP", "TN", "FN", "Error", "Total"])
            writer.writerow({"Time": cur_time, "Type": version, "Tool": "-", "Accuracy w/o error": accuracy_wo_error, "Accuracy w/ error": accuracy_w_error,
                             "Precision": precision, "Recall": recall, "Specificity": specificity, "Error rate": error_rate,
                             "TP": count_tp, "FP": count_fp, "TN": count_tn, "FN": count_fn, "Error": count_error, "Total": count_total})

        for tool in tools:
            print(tool)
            data2 = data[data["tool"] == tool]
            data2 = data2.copy()

            data2["tp"] = np.where((data2["ground_truth"] == 1) & (data2["insecure"] == 1), 1, 0)
            data2["fp"] = np.where((data2["ground_truth"] == 0) & (data2["insecure"] == 1), 1, 0)
            data2["tn"] = np.where((data2["ground_truth"] == 0) & (data2["insecure"] == 0), 1, 0)
            data2["fn"] = np.where((data2["ground_truth"] == 1) & (data2["insecure"] == 0), 1, 0)

            data2["tp"] = np.where(data2["error"] == 1, 0, data2["tp"])
            data2["fp"] = np.where(data2["error"] == 1, 0, data2["fp"])
            data2["tn"] = np.where(data2["error"] == 1, 0, data2["tn"])
            data2["fn"] = np.where(data2["error"] == 1, 0, data2["fn"])

            data2["tp"] = data2["tp"].fillna(0)
            data2["fp"] = data2["fp"].fillna(0)
            data2["tn"] = data2["tn"].fillna(0)
            data2["fn"] = data2["fn"].fillna(0)

            count_tp = data2["tp"].astype(int).sum()
            count_fp = data2["fp"].astype(int).sum()
            count_tn = data2["tn"].astype(int).sum()
            count_fn = data2["fn"].astype(int).sum()
            count_error = data2["error"].sum()
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
            specificity = count_tn / (count_tn + count_fn)
            error_rate = count_error / count_total

            with open(basename + "_version_metrics.csv", 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=';',
                                        fieldnames=["Time", "Type", "Tool", "Accuracy w/o error", "Accuracy w/ error",
                                                    "Precision", "Recall",
                                                    "Specificity", "Error rate", "TP", "FP", "TN", "FN", "Error",
                                                    "Total"])
                writer.writerow({"Time": cur_time, "Type": version, "Tool": tool, "Accuracy w/o error": accuracy_wo_error,
                                 "Accuracy w/ error": accuracy_w_error,
                                 "Precision": precision, "Recall": recall, "Specificity": specificity,
                                 "Error rate": error_rate,
                                 "TP": count_tp, "FP": count_fp, "TN": count_tn, "FN": count_fn, "Error": count_error,
                                 "Total": count_total})
