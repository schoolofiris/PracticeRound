import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]|[A-Z]{2,}"
    regex2 = r"[A-Z]{2,}"
    result = re.search(regex, log_line)
    result2 = re.search(regex2, log_line)
    if result2 is None:
        return None
    else:
        return "{}".format(result2[0])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)