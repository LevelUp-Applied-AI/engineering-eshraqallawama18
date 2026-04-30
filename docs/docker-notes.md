# Docker Notes — Day 9

## Docker Version
``` bash
docker verion 
```
Client:
 Version:           29.4.1
 API version:       1.54
 Go version:        go1.26.2
 Git commit:        055a478
 Built:             Mon Apr 20 16:35:45 2026
 OS/Arch:           windows/amd64
 Context:           desktop-linux

Server: Docker Desktop 4.71.0 (225177)
 Engine:
  Version:          29.4.1
  API version:      1.54 (minimum version 1.40)
  Go version:       go1.26.2
  Git commit:       6c91b92
  Built:            Mon Apr 20 16:32:41 2026
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v2.2.3
  GitCommit:        77c84241c7cbdd9b4eca2591793e3d4f4317c590
 runc:
  Version:          1.3.5
  GitCommit:        v1.3.5-0-g488fc13e
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0



## Hello World Test

```bash  
docker run hello-world
```  
Hello from Docker!
This message shows that your installation appears to be working correctly.

## Postgres Container
``` bash
docker run -d \
  --name pg-prework \
  -e POSTGRES_PASSWORD=prework \
  -P 5432:5432 \
  postgres:15-lapine

```

35dbda422d16e95b0eb460ccaf929a1eba5d4a871621d239cc5593aa2f4b9df2


## Startup Logs

```bash
docker logs pg-prework
```

The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... UTC
creating configuration files ... ok
running bootstrap script ... ok
sh: locale: not found
2026-04-30 09:35:50.204 UTC [35] WARNING:  no usable system locales were found
performing post-bootstrap initialization ... ok
initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
syncing data to disk ... ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

waiting for server to start....2026-04-30 09:35:51.016 UTC [41] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-04-30 09:35:51.024 UTC [41] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-04-30 09:35:51.049 UTC [44] LOG:  database system was shut down at 2026-04-30 09:35:50 UTC
2026-04-30 09:35:51.067 UTC [41] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

waiting for server to shut down....2026-04-30 09:35:51.116 UTC [41] LOG:  received fast shutdown request
2026-04-30 09:35:51.123 UTC [41] LOG:  aborting any active transactions
2026-04-30 09:35:51.126 UTC [41] LOG:  background worker "logical replication launcher" (PID 47) exited with exit code 1
2026-04-30 09:35:51.126 UTC [42] LOG:  shutting down
2026-04-30 09:35:51.133 UTC [42] LOG:  checkpoint starting: shutdown immediate
2026-04-30 09:35:51.181 UTC [42] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.013 s, sync=0.007 s, total=0.056 s; sync files=2, longest=0.004 s, average=0.004 s; distance=0 kB, estimate=0 kB
2026-04-30 09:35:51.193 UTC [41] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2026-04-30 09:35:51.264 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-04-30 09:35:51.264 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-04-30 09:35:51.264 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-04-30 09:35:51.278 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-04-30 09:35:51.293 UTC [55] LOG:  database system was shut down at 2026-04-30 09:35:51 UTC
2026-04-30 09:35:51.305 UTC [1] LOG:  database system is ready to accept connections

## Stop and Restart

### stop

```bash
docker stop pg-prework
pg-prework
```
pg-prework

### restart

```bash
docker restart pg-prework
pg-prework
```
pg-prework

### logs

```bash
docker logs pg-prework
```

The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... UTC
creating configuration files ... ok
running bootstrap script ... ok
sh: locale: not found
2026-04-30 09:35:50.204 UTC [35] WARNING:  no usable system locales were found
performing post-bootstrap initialization ... ok
initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
syncing data to disk ... ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

waiting for server to start....2026-04-30 09:35:51.016 UTC [41] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-04-30 09:35:51.024 UTC [41] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-04-30 09:35:51.049 UTC [44] LOG:  database system was shut down at 2026-04-30 09:35:50 UTC
2026-04-30 09:35:51.067 UTC [41] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

waiting for server to shut down....2026-04-30 09:35:51.116 UTC [41] LOG:  received fast shutdown request
2026-04-30 09:35:51.123 UTC [41] LOG:  aborting any active transactions
2026-04-30 09:35:51.126 UTC [41] LOG:  background worker "logical replication launcher" (PID 47) exited with exit code 1
2026-04-30 09:35:51.126 UTC [42] LOG:  shutting down
2026-04-30 09:35:51.133 UTC [42] LOG:  checkpoint starting: shutdown immediate
2026-04-30 09:35:51.181 UTC [42] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.013 s, sync=0.007 s, total=0.056 s; sync files=2, longest=0.004 s, average=0.004 s; distance=0 kB, estimate=0 kB
2026-04-30 09:35:51.193 UTC [41] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2026-04-30 09:35:51.264 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-04-30 09:35:51.264 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-04-30 09:35:51.264 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-04-30 09:35:51.278 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-04-30 09:35:51.293 UTC [55] LOG:  database system was shut down at 2026-04-30 09:35:51 UTC
2026-04-30 09:35:51.305 UTC [1] LOG:  database system is ready to accept connections
2026-04-30 09:38:15.740 UTC [1] LOG:  received fast shutdown request
2026-04-30 09:38:15.746 UTC [1] LOG:  aborting any active transactions
2026-04-30 09:38:15.748 UTC [1] LOG:  background worker "logical replication launcher" (PID 58) exited with exit code 1
2026-04-30 09:38:15.749 UTC [53] LOG:  shutting down
2026-04-30 09:38:15.755 UTC [53] LOG:  checkpoint starting: shutdown immediate
2026-04-30 09:38:15.803 UTC [53] LOG:  checkpoint complete: wrote 43 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.013 s, sync=0.015 s, total=0.054 s; sync files=11, longest=0.007 s, average=0.002 s; distance=252 kB, estimate=252 kB
2026-04-30 09:38:15.807 UTC [1] LOG:  database system is shut down

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-04-30 09:38:46.222 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-04-30 09:38:46.223 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-04-30 09:38:46.223 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-04-30 09:38:46.235 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-04-30 09:38:46.256 UTC [29] LOG:  database system was shut down at 2026-04-30 09:38:15 UTC
2026-04-30 09:38:46.276 UTC [1] LOG:  database system is ready to accept connections
2026-04-30 09:38:51.117 UTC [1] LOG:  received fast shutdown request
2026-04-30 09:38:51.123 UTC [1] LOG:  aborting any active transactions
2026-04-30 09:38:51.126 UTC [1] LOG:  background worker "logical replication launcher" (PID 32) exited with exit code 1
2026-04-30 09:38:51.126 UTC [27] LOG:  shutting down
2026-04-30 09:38:51.132 UTC [27] LOG:  checkpoint starting: shutdown immediate
2026-04-30 09:38:51.176 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.012 s, sync=0.006 s, total=0.050 s; sync files=2, longest=0.003 s, average=0.003 s; distance=0 kB, estimate=0 kB
2026-04-30 09:38:51.180 UTC [1] LOG:  database system is shut down

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-04-30 09:39:13.593 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-04-30 09:39:13.594 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-04-30 09:39:13.594 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-04-30 09:39:13.606 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-04-30 09:39:13.620 UTC [29] LOG:  database system was shut down at 2026-04-30 09:38:51 UTC
2026-04-30 09:39:13.629 UTC [1] LOG:  database system is ready to accept connections
2026-04-30 09:44:25.665 UTC [27] LOG:  checkpoint starting: time
2026-04-30 09:44:25.713 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.015 s, sync=0.007 s, total=0.049 s; sync files=2, longest=0.004 s, average=0.004 s; distance=0 kB, estimate=0 kB
2026-04-30 09:48:35.754 UTC [1] LOG:  received fast shutdown request
2026-04-30 09:48:35.761 UTC [1] LOG:  aborting any active transactions
2026-04-30 09:48:35.763 UTC [1] LOG:  background worker "logical replication launcher" (PID 32) exited with exit code 1
2026-04-30 09:48:35.764 UTC [27] LOG:  shutting down
2026-04-30 09:48:35.770 UTC [27] LOG:  checkpoint starting: shutdown immediate
2026-04-30 09:48:35.792 UTC [27] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s, sync=0.001 s, total=0.029 s; sync files=0, longest=0.000 s, average=0.000 s; distance=0 kB, estimate=0 kB
2026-04-30 09:48:35.797 UTC [1] LOG:  database system is shut down

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-04-30 09:50:24.479 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-04-30 09:50:24.479 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-04-30 09:50:24.479 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-04-30 09:50:24.496 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-04-30 09:50:24.510 UTC [29] LOG:  database system was shut down at 2026-04-30 09:48:35 UTC
2026-04-30 09:50:24.520 UTC [1] LOG:  database system is ready to accept connections


## Issues Encountered

- At first, I faced an issue while setting up Docker because I didn’t have administrator privileges, and Windows blocked the installation.

- After multiple attempts, I switched to using PowerShell as administrator.

- Finally, I managed to fix the issue and successfully set up Docker 😄



