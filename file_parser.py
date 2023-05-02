import argparse
def file_parser(input_file,out_put_file = ''):
    print(f'Processing {input_file}')
    print('Finished processing')
    if out_put_file:
        print(f'Creating {out_put_file}')




def main():
    parser = argparse.ArgumentParser('File parser',description='PyParse - The File Processor',
     epilog='Thank you for using PyParser')
    parser.add_argument('---infile',help='Input file for conversion')
    parser.add_argument('---out',help=' Converted Output file')
    args  = parser.parse_args()
    if args.infile:
        file_parser(args.infile,args.out)
    

if __name__ == '__main__':
    main()
