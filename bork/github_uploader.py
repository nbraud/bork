# from . import file_finder


def upload(dry_run=False, *globs):
    files = file_finder.find_files(globs, 'GitHub')

    # if dry_run:
    #     print('NOTE: Skipping GitHub upload step since this is a dry run.')
    # else:
    #     pass

    raise NotImplementedError('github_uploader.upload()')
