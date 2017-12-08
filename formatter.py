import json


def main():
    with open('quotes.json') as f:
        read_data = f.read()
    test_dict = json.loads(read_data)
    for x in test_dict:
        print(x['text'])


if __name__ == "__main__":
    main()
