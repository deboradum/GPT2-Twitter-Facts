from asyncore import write
import json

# https://github.com/woluxwolu/twint/tree/woluxwolu-update0308
# Twint command:
#twint -u USERNAME -o OUTPUTFILE --json

# Filters links and only tweet prop from json file.
def filter(fileName):
    data = []
    print("Parsing JSON objects...")
    with open(fileName) as f:
        for line in f:
            data.append(json.loads(line))
    print("Data parsed.")
    writebackFile = open("tweets.txt", "a")

    # Iterates over every object in the file.
    print("Writing back tweets...")
    for tweet in data:
        # Filters links to websites (sponsored posts)
        if "https://" not in tweet["tweet"]:
            if "http://" not in tweet["tweet"]:
                if "@" not in tweet["tweet"]:
                    writebackFile.write(tweet["tweet"] + "\n")
                    writebackFile.write("<|endoftext|>\n")
    print("Written tweets back to tweets.txt.")

    print("Closing file...")
    writebackFile.close()
    print("File closed.")

print("starting on FactPoint.json")
filter("FactPoint.json")
