from data_harvesting.record_pool import RecordPool
import os


def read_url_file(file_path):
    """Parses a file containing urls and optional additional data

    Args:
        file_path (str): Path to file to be read

    Raises:
        ValueError: Raised if file does not exist

    Returns:
        list(str): List of urls 
    """

    if not os.path.isfile(file_path):
        raise ValueError(f'URL File {file_path} doesnt exist.')

    with open(file_path, 'r') as fd:

        input_file_data = fd.readlines()
        return input_file_data


def preprocess_deezer_title(raw_urls):
    """Preprocesses the optional Deezer title

    Args:
        raw_urls (list): Raw list of urls

    Returns:
        list(tuple): List of tuples with (url, deezer_title|None) 
    """
    url_input = []

    for url_line in raw_urls:

        if ',' in url_line:  # Deezer title exists
            url_input.append(url_line.split(','))
        else:  # Treat YT video title as title
            url_input.append((url_line, None))

    return url_input


if __name__ == "__main__":

    import argparse

    urls = []
    parser = argparse.ArgumentParser(description='MP3 Data Farm')

    parser.add_argument('--file', '-f', dest='file',
                        help='Path to file containing URL\'s')
    parser.add_argument('--url', '-u', dest='urls', action='append',
                        help='Youtube URL to by downloaded and parsed')

    cli_data = parser.parse_args()

    if cli_data.file:
        urls = read_url_file(cli_data.file)
    else:
        urls = cli_data.urls

    urls = preprocess_deezer_title(urls)
    print(urls)
    record_pool = RecordPool(urls)
    record_pool.start_job()
    record_pool.dump_data()
