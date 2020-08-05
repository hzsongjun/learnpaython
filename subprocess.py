import subprocess
res = subprocess.Popen("psql -h 10.20.2.60 -p 1921 -U lisbase -d lisdb -f c:\doc\1.sql",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
err = res.stderr.read()

if err:
    cmd_res = err
else:
    cmd_res = res.stdout.read()
print(cmd_res)
 #if cmd_res:
 #   cmd_res = "执行成功！".encode("GBK")