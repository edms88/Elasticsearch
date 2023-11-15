import pandas as pd
from pathlib import Path


# You can use pathlib to declare folder
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

dataset = current_dir / "dataset" / "wiki_movie_plots_deduped.csv"

df = (
    pd.read_csv(dataset)
    .dropna()
    .sample(5000, random_state=42)
    .reset_index(drop=True)
)



with open(dataset, mode="r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            doc = {
                "title": row["title"],
                "ethnicity": row["ethnicity"],
                "director": row["director"],
                "cast": row["cast"],
                "plot": row["plot"] or None,
                "year": row["year"],
                "wiki_page": row["wiki_page"]
            }

            #where if have null data example
            # lat = row["country"]
            # lon = row["age"]
            # if lat not in ("", "0") and lon not in ("", "0"):
            #     doc["country"] = {"lat": float(lat), "lon": float(lon)}
            yield doc


