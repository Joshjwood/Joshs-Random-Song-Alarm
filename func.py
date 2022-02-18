def minute(now):
    if len(str(now.minute)) == 1:
        return f"0{now.minute}"
    else:
        return now.minute