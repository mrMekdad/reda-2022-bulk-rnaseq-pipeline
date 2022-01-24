"""Core workflow for Bulk RNAseq Pipeline by Red@."""

PROJECT_NAME = "Bulk RNAseq Pipeline"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
