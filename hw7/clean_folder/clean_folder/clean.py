import sys, os, shutil

GLOBAL_PATH = ''


def traversing_folders(path, next_level=0):

    file_list = []

    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            traversing_folders(os.path.join(path, file), next_level + 1)
        else:
            file_list.append(file)

    transfer_file(file_list, path, next_level)


def normalize(*args):

    trans_dict = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y',
                  ord('і'): 'i', ord('ї'): 'yi', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
                  ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ю'): 'yu',
                  ord('я'): 'ya', ord('ы'): 'y', ord('э'): 'e', ord('ё'): 'yo', ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E',
                  ord('Є'): 'Ye', ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y', ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M',
                  ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh', ord('Ц'): 'Ts',
                  ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ю'): 'Yu', ord('Я'): 'Ya', ord('Ы'): 'Y', ord('Э'): 'E', ord('Ё'): 'Yo'}

    string = []
    normalize_name = ''

    for el in args:
        if not el.isalpha() and not el.isdigit():
            el = '_'
            string.append(el)
        else:
            el = el.translate(trans_dict)
            string.append(el)

    return normalize_name.join(string)


def create_folders():

    new_folders = ['images', 'documents', 'videos', 'audios', 'archives']
    for name in new_folders:
        directory = os.path.join(GLOBAL_PATH, name)
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)


def move_file(split_file):

    create_folders()

    info = split_file.split(";")
    src = os.path.join(info[1], info[2]+info[3])
    dest = os.path.join(GLOBAL_PATH, info[0], normalize(info[2])+info[3])

    if info[0] == 'archives':
        shutil.unpack_archive(shutil.move(src, dest), os.path.join(GLOBAL_PATH, info[0]))
        os.remove(dest)
    else:
        shutil.move(src, dest)
    try:
        os.rmdir(info[1])
    except OSError:
        pass


def transfer_file(file_list, path, next_level):

    images_extension = ['.jpg', '.png', '.jpeg']
    video_extension = ['.avi', '.mp4', '.mov']
    doc_extension = ['.pdf', '.docx', '.txt', '.xlsx']
    music_extension = ['.mp3', '.ogg', '.wav', '.amr']
    arhive_extension = ['.zip', '.7zip', '.gz', '.tar']

    for file in file_list:

        file_name, file_extension = os.path.splitext(file)

        if file_extension in images_extension:
            move_file(f'images;{path};{file_name};{file_extension}')

        elif file_extension in video_extension:
            move_file(f'videos;{path};{file_name};{file_extension}')

        elif file_extension in doc_extension:
            move_file(f'documents;{path};{file_name};{file_extension}')

        elif file_extension in music_extension:
            move_file(f'audios;{path};{file_name};{file_extension}')

        elif file_extension in arhive_extension:
            move_file(f'archives;{path};{file_name};{file_extension}')


def clean():
    global GLOBAL_PATH
    if len(sys.argv) == 1:
        GLOBAL_PATH = os.getcwd()
        traversing_folders(GLOBAL_PATH)
    else:
        GLOBAL_PATH = sys.argv[1]
        traversing_folders(GLOBAL_PATH)

def main():

    # 'C:\Users\vdunk\Desktop\NewFolder' sys.argv[1]
    traversing_folders(r'C:/Users/vdunk/Desktop/NewFolder/')


if __name__ == '__main__':
    main()