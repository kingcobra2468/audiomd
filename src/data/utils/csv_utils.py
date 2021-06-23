from config import METADATA_SCRAPPERS
from collections import Counter


def gen_uniq_meta_labels(metadata_scrappers):

    labels = [label for ms in metadata_scrappers for label in ms.LABELS]
    labels_freq = Counter(labels)
    labels_unique = []

    for label, freq in labels_freq.items():
        if freq > 1:
            labels_unique += [f'{label}_{i}' for i in range(freq)]
        else:
            labels_unique.append(label)

    return labels_unique
