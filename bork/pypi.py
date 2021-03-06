from twine.cli import dispatch as twine_upload

from .asset_manager import download_assets
from .filesystem import find_files
from .pypi_api import get_download_info


class PypiHandler:
    def __init__(self, repo_url):
        self.repo_url = repo_url

    def upload(self, *globs, dry_run=False):
        files = find_files(globs, 'PyPI')

        if dry_run:
            print('NOTE: Skipping PyPI upload step since this is a dry run.')
        else:
            twine_upload(['upload', '--repository-url', self.repo_url, *files])

    def download(self, package, release, file_pattern, directory):
        asset_list = get_download_info(self.repo_url, package, release, file_pattern)
        download_assets(asset_list, directory)


PRODUCTION = PypiHandler('https://pypi.org/simple')
TESTING = PypiHandler('https://test.pypi.org/simple')
