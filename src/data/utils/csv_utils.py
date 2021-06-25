from collections import Counter


def gen_uniq_meta_labels(metadata_scrappers):
    """Generate a set of unique labels for the multiset of labels. Thus, for example
    if the label with name "genre" appears in multiple metadata srappers, then
    genre will be prefixed with "genre_1" and "genre_2".

    Args:
        metadata_scrappers (list): List of instances of type metadata_scrappers.

    Returns:
        list(str): The set of unique labels. 
    """
    labels = [label for ms in metadata_scrappers for label in ms.LABELS]
    labels_freq = Counter(labels)
    labels_unique = []

    for label, freq in labels_freq.items():
        if freq > 1:  # label appears more than once so adds suffix to each occurance.
            labels_unique += [f'{label}_{i}' for i in range(freq)]
        else:
            labels_unique.append(label)

    return labels_unique
