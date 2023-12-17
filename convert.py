#!/opt/homebrew/bin/python3

import sys

from pandas import read_csv

def main():
    script, input_file, output_file = sys.argv
    if not input_file.endswith('csv') and not output_file.endswith('json'):
        print(f'Usage: {script} input.csv output.json')

    df = read_csv(input_file, names = ('front', 'back', 'description', 'id'))
    df = df.drop(['description', 'id'], axis=1)
    df['tags'] = [('Korean',) for i in range(len(df))]
    df.to_json(output_file, force_ascii=False, indent=2, orient="records")

if __name__ == '__main__':
    main()
