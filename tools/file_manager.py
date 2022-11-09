import shutil
import os


def save_file(global_file_path, person_id, file_name):
    path = os.path.join(os.getcwd(), "persons_data", person_id)
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    shutil.copy(global_file_path, os.path.join(path, file_name))


def get_file_path(person_id, file_name):
    return os.path.join(os.getcwd(), "persons_data", person_id, file_name)
