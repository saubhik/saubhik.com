# Start jupyter notebook server as service on boot

I am working in Fedora 28, so the instructions are according to this platform.

This might work on any Linux distribution using `systemd` as its process manager.

Steps:
1. Create the systemd unit file as root: `sudo vim /usr/lib/systemd/system/jupyter-notebook.service`

2. Write the following into it:

```shell
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

```shell
sudo useradd ipynb
``` 

Set password using `sudo passwd ipynb` and login as `ipynb` & do `mkdir notebooks`.

4. Start the jupyter notebook service.

```shell
sudo systemctl daemon-reload
sudo systemctl enable jupyter-notebook
sudo systemctl start jupyter-notebook
```

To check the status one can do `sudo systemctl status jupyter-notebook`.

To stop the service one can do `sudo systemctl stop jupyter-notebook`.

## Start jupyterhub as a system service

The process is very similar:
1. `sudo vim /usr/lib/systemd/system/jupyter.service`
2. Write the following:

```shell
[Unit]
Description=jupyterhub

[Service]
Type=simple
PIDFile=/var/run/jupyterhub.pid
ExecStart=/usr/local/bin/jupyterhub --port 8000

[Install]
WantedBy=multi-user.target
```
3. Do the following

```shell
sudo chmod +x /usr/lib/systemd/system/jupyter.service
sudo systemctl daemon reload
sudo systemctl enable jupyter.service
sudo systemctl start jupyter.service
```

And we are done!
I did not find any SELinux problems while doing the above 3 steps in our linux box. To check if there could be issues with SELinux, then type `ls -l` and see if the permissions end with a `.` (SELinux enforced) or not.