import json
import sys

def main():

    twitterhandle = sys.argv[1]

    outfile = open(twitterhandle + '.txt', 'w')
    outfile.truncate()
    with open(twitterhandle + '.json') as f:
        read_data = f.read()

    test_dict = json.loads(read_data)
    for x in test_dict:

        if x['text'].strip():
            tweet = x['text'].replace('\n', ' ')
            outfile.write('{}\n'.format(tweet))


if __name__ == "__main__":
    main()
