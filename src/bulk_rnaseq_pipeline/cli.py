import argparse
from bulk_rnaseq_pipeline.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Repository for bulk RNAseq orchestration, naming rules, and reporting artifacts.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
