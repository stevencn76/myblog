from pathlib import Path


def get_file_name_parts(filename: str):
    pos = filename.rfind('.')
    if pos == -1:
        return filename, ''

    return filename[:pos], filename[pos+1:]


def get_save_filepath(file_path: Path, filename: str):
    save_file = file_path.joinpath(filename)
    if not save_file.exists():
        return save_file

    name, ext = get_file_name_parts(filename)
    for index in range(1, 100):
        save_file = file_path.joinpath(f'{name}_{index}.{ext}')
        if not save_file.exists():
            return save_file

    return file_path.joinpath(f'{name}_override.{ext}')
