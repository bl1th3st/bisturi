from subprocess import call

out_buffer = None
value = call(['nmap'], stdout=out_buffer)

print(out_buffer)
