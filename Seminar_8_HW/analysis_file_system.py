import os
import json
import csv
import pickle


def get_dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({
                'Path': path,
                'Type': 'File',
                'Size': size
            })

        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({
                'Path': path,
                'Type': 'Directory',
                'Size': size
            })

    return results


def save_results_to_json(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)


def save_results_to_csv(results, output_file):
    fieldnames = ['Path', 'Type', 'Size']
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as f:
        pickle.dump(results, f)


def main(directory, json_file, csv_file, pickle_file):
    results = traverse_directory(directory)
    save_results_to_json(results, json_file)
    save_results_to_csv(results, csv_file)
    save_results_to_pickle(results, pickle_file)