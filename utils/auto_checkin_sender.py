import os


def formatted_logs():
    luansiqi_log = ""
    chenannan_log = ""
    lines = []
    splits = []
    log_path = 'genshin/AutoMihoyoBBS/logs/logging.log'
    with open(os.path.join(os.path.expanduser('~'), log_path), encoding='utf-8') as f:
        for line1 in f:
            lines.append(line1)
    for x in lines:
        if "正在执行:" in x:
            splits.append(lines.index(x))

    for s in range(0, len(splits)):
        if 'luansiqi' in lines[splits[s]]:
            if s + 1 != len(splits):
                for x in lines[splits[s]:splits[s + 1]]:
                    luansiqi_log += x
            else:
                for x in lines[splits[s]:]:
                    luansiqi_log += x
        if 'chenannan' in lines[splits[s]]:
            if s + 1 != len(splits):
                for x in lines[splits[s]:splits[s + 1]]:
                    chenannan_log += x
            else:
                for x in lines[splits[s]:]:
                    chenannan_log += x
    return {
        "luansiqi": luansiqi_log,
        "chenannan": chenannan_log
    }


if __name__ == '__main__':
    print(formatted_logs())
