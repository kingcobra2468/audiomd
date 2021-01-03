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

        urls = fd.readlines()
        urls = [url.strip() for url in urls]

        return urls


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

    print(urls)
    record_pool = RecordPool(urls)
    record_pool.start_job()
    record_pool.dump_data()
