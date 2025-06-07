import os

from datasets import load_dataset

SAVE_DIR = "./data"

os.makedirs(SAVE_DIR, exist_ok=True)

dataset = load_dataset("mteb/amazon_reviews_multi", "all_languages")

for split_name, split_dataset in dataset.items():
    file_path = os.path.join(SAVE_DIR, f"{split_name}.csv")
    split_dataset.to_csv(file_path)
