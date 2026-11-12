"""Download the public Hugging Face QA datasets without transforming records."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent / "raw"
DATASETS = [
    ("rajpurkar/squad_v2", "squad_v2", "squad_v2"),
    ("UCLNLP/adversarial_qa", "adversarialQA", "adversarial_qa/adversarialQA"),
    ("UCLNLP/adversarial_qa", "dbert", "adversarial_qa/dbert"),
    ("UCLNLP/adversarial_qa", "dbidaf", "adversarial_qa/dbidaf"),
    ("UCLNLP/adversarial_qa", "droberta", "adversarial_qa/droberta"),
]


def parquet_metadata(dataset: str) -> dict:
    url = f"https://datasets-server.huggingface.co/parquet?dataset={quote(dataset)}"
    response = subprocess.check_output(["curl", "-fsSL", url])
    return json.loads(response)


def download(url: str, destination: Path, expected_size: int) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.stat().st_size == expected_size:
        print(f"verified existing {destination}")
        return
    partial = destination.with_name(destination.name + ".part")
    subprocess.run(
        ["curl", "-fL", "-C", "-", "--retry", "3", "-o", str(partial), url],
        check=True,
    )
    actual_size = partial.stat().st_size
    if actual_size != expected_size:
        raise RuntimeError(
            f"integrity check failed for {destination}: "
            f"{actual_size} bytes, expected {expected_size}"
        )
    os.replace(partial, destination)
    print(f"verified {destination}")


def main() -> None:
    for dataset, config, folder in DATASETS:
        metadata = parquet_metadata(dataset)
        for parquet in metadata["parquet_files"]:
            if parquet["config"] != config:
                continue
            destination = ROOT / folder / parquet["split"] / "0000.parquet"
            download(parquet["url"], destination, parquet["size"])


if __name__ == "__main__":
    main()
