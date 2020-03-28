def format_duration(seconds):
    d = ['second', 'minute', 'hour', 'day', 'year']
    if seconds == 0:
        return "now"
    output = []
    cur = seconds
    while cur != 0:
        if len(output) == 2:
            output.append(cur % 24)
            cur = cur // 24
        elif len(output) == 3:
            output.append(cur % 365)
            cur = cur // 365
        else:
            output.append(cur % 60)
            cur = cur // 60
    out_string = ""
    for i, v in enumerate(output):
        con_str = ""
        if v > 0:
            con_str += f"{v} {d[i]}"
            if v > 1:
                con_str += "s"
            if len(out_string) > 0:
                if "and" in out_string:
                    con_str += ", "
                else:
                    con_str += " and "
        out_string = con_str + out_string
    return out_string
