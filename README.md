# check_truenas_scale

check_truenas_scale.py – A Python script for monitoring TrueNAS Scale alerts via the REST API.
It retrieves active alerts, categorizes them as CRITICAL or WARNING, and outputs a corresponding Nagios-compatible status. 
Designed for automation and monitoring integration, the script requires a hostname and API token for authentication.

## Usage
```bash
usage: check_truenas_scale.py [-h] -H HOSTNAME -t TOKEN

Check TrueNAS scale alerts via RestAPI

options:
  -h, --help            show this help message and exit
  -H, --hostname HOSTNAME
                        Host name or IP Address
  -t, --token TOKEN     API token

Send email to tsvetan@gerov.eu if you have questions regarding use of this software.
```

Example Usage:
```bash
[root@icinga ~]# ./check_truenas_scale -H truenas.example.local -t <TOKEN>
[WARNING] (1) 'boot-pool' is consuming USB devices 'sdf' which is not recommended.
```

## License

This script is licensed under the GPL-3.0 License. For more details, see LICENSE file.
