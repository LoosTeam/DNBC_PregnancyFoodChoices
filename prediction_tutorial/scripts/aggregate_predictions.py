import pandas as pd
from pathlib import Path
import sys

if len(sys.argv) > 1:
    predictions_dir = Path(sys.argv[1]) / "foodcateg_output"
else:
    predictions_dir = Path("predictions_output/foodcateg_output")

if not predictions_dir.exists():
    print(f"Error: Directory not found: {predictions_dir}")
    print("Usage: python aggregate_predictions.py [predictions_output_folder]")
    sys.exit(1)

categories = [d.name for d in predictions_dir.iterdir() if d.is_dir()]

all_predictions = {}

for category in sorted(categories):
    csv_path = predictions_dir / category / "predictions.csv"
    df = pd.read_csv(csv_path)

    df['prediction'] = (df['1'] > df['0']).astype(int)
    df['confidence'] = df['1'] - df['0']

    for _, row in df.iterrows():
        sample_id = row['ID']
        if sample_id not in all_predictions:
            all_predictions[sample_id] = {}
        all_predictions[sample_id][category] = {
            'predicted': row['prediction'],
            'confidence': row['confidence']
        }

for sample_id in sorted(all_predictions.keys()):
    print(f"\n{sample_id}:")
    predictions = all_predictions[sample_id]

    positive_predictions = [(cat, info['confidence'])
                           for cat, info in predictions.items()
                           if info['predicted'] == 1]

    positive_predictions.sort(key=lambda x: x[1], reverse=True)

    print(f"  Predicted categories ({len(positive_predictions)}):")
    for cat, conf in positive_predictions:
        print(f"    - {cat}: {conf:.2f}")
