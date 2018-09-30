# Start jupyter notebook server as service on boot

I am working in Fedora 28, so the instructions are according to this platform.

This might work on any Linux distribution using `systemd` as its process manager.

Steps:
1. Create the systemd unit file as root: `sudo vim /usr/lib/systemd/system/jupyter-notebook.service`

2. Write the following into it:

```
[Unit]
Description=jupyter notebook

[Service]
Type=simple
PIDFile=/var/run/jupyter-notebook.pid
ExecStart=/py3env/bin/jupyter-notebook --no-browser --port=8000
User=ipynb
Group=ipynb
WorkingDirectory=/home/ipynb/notebooks

[Install]
WantedBy=multi-user.target
```

3. Create the user `ipynb`:

```
sudo useradd ipynb
``` 

Set password using `sudo passwd ipynb` and login as `ipynb` & do `mkdir notebooks`.

4. Start the jupyter notebook service.

```
sudo systemctl daemon-reload
sudo systemctl enable jupyter-notebook
sudo systemctl start jupyter-notebook
```

To check the status one can do `sudo systemctl status jupyter-notebook`.

To stop the service one can do `sudo systemctl stop jupyter-notebook`.