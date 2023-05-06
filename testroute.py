import subprocess


output = subprocess.check_output('route print', stderr=subprocess.STDOUT, text=True)
text1 = output.index("Persistent Routes:")  # index() throw error if the string is not found
text2 = output.index("=", text1)

print(output[text1: text2])