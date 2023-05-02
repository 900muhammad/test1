import argparse
import pathlib
def search_folder(path,extension,file_size = None):
    " " " Search folder for files" " "
    folder = pathlib.Path(path)
    files  = list(folder.rglob(f'*. {extension}'))
    if not files:
        print(f'No files found with {extension=}')
    if file_size is not None:
        files = [ f for f in files
                 if f.stat().st_size >= file_size ]
        print(f'{len(files)} *.{extension} files found')
        for file_path in files:
            print(file_path)
def main():
    parser = argparse.ArgumentParser('PySearch',description='PyParse - The search Processor',
     epilog='Thank you for using PyParser')
    parser.add_argument('-p','--path', 
                        help='The path to search for files',
                        required=True,
                        dest='path')
    parser.add_argument('-e','--ext',
                        help='The Extension To search for',
                        required=True,
                        dest='extension')
    parser.add_argument('-s','--size',
                        help='The File size to filter in bytes',
                        type=int,
                        dest='size',
                        default=None)
    args = parser.parse_args()
    search_folder(args.path,args.extension,args.size)

    
if __name__ == '__main__':
    main()


    
