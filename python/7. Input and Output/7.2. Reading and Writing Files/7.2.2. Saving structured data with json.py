import json


def json_():
    x = [1, 'simple', 'list']
    print(json.dumps(x))


def read_string():
    io = open("in.json", "r", encoding="utf-8")
    string = io.read()
    dictionary = json.loads(string)  # json.loads() requires string
    print(dictionary)
    io.close()


def read_dictionary():
    io = open("in.json", "r", encoding="utf-8")
    dictionary = json.load(io)  # the json.load() requires file descriptor
    print(dictionary)


def dumps_string():
    d = {'alpha': 1, 'beta': 2}
    s = json.dumps(d)
    open("out.json", "w").write(s)


def dump_dictionary():
    d = {'alpha': 1, 'beta': 2}
    json.dump(d, open("out.json", "w"))


json_()
read_string()
read_dictionary()
dumps_string()
dump_dictionary()


def read_write_example():
    # https://www.bogotobogo.com/python/python-json-dumps-loads-file-read-write.php
    # Four Fundamental Forces with JSON
    d = {}

    d["gravity"] = {
        "mediator": "gravitons",
        "relative strength": "1",
        "range": "infinity"
    }
    d["weak"] = {
        "mediator": "W/Z bosons",
        "relative strength": "10^25",
        "range": "10^-18"
    }
    d["electromagnetic"] = {
        "mediator": "photons",
        "relative strength": "10^36",
        "range": "infinity"
    }
    d["strong"] = {
        "mediator": "gluons",
        "relative strength": "10^38",
        "range": "10^-15"
    }

    def working_with_string(dicti):
        # encoding to JSON
        data = json.dumps(dicti)

        # write to a file
        with open("4forces.json", "w") as f:
            f.write(data)

        # reads it back
        with open("4forces.json", "r") as f:
            data = f.read()

        # decoding the JSON to dictionay
        res = json.loads(data)

        print(res)

    def working_with_files(dicti):
        # write to a file
        with open("4forces.json", "w") as f:
            json.dump(dicti, f)

        # reads it back
        with open("4forces.json", "r") as f:
            res = json.load(f)

        print(res)

    working_with_string(d)
    working_with_files(d)


def dump_load():
    # Here is another example (json.dump()/json.load())
    # in.json file - {"alpha":1, "beta":2}
    with open("in.json", "r") as fr:
        out_dict = json.load(fr)
    print(out_dict)

    in_dict = {"a": 1, "b": 2}
    with open("out.json", "w") as fw:
        json.dump(in_dict, fw)
    # out.json file - {"a":1,"b":2}


read_write_example()
dump_load()