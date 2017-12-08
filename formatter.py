import json


def main():

    outfile = open('tweets.output', 'w')

    with open('tweets.json') as f:
        read_data = f.read()
    test_dict = json.loads(read_data)
    for x in test_dict:
        outfile.write('{}\n'.format(x['text']))


if __name__ == "__main__":
    main()
