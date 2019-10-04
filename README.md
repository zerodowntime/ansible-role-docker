# docker

Install docker

## Requirements

- Ansible >= 2.7

### Supported platforms

```yml
- EL
  - 7
- Ubuntu
  - bionic
  - xenial
```

## Default role variables

| Name                         | Description                                                                      |  Type  |   Default   | Required |
| ---------------------------- | -------------------------------------------------------------------------------- |:------:|:-----------:|:--------:|
| docker__package_state        | Package state `present`,`latest`                                                 | string |  `present`  |   True   |
| docker__storage_driver       | Docker storage driver                                                            | string | `overlay2`  |   True   |
| docker__package_name         | Package name to be installed                                                     | string | `docker-ce` |   True   |
| docker__package_version      | Package version to be installed                                                  | string |   `None`    |   True   |
| docker__debug                | Enable debug mode                                                                |  bool  |   `False`   |   True   |
| docker__log_driver           | Default driver for container logs                                                | string | `json-file` |   True   |
| docker__log_driver_opts      | Log options                                                                      |  dict  |   `None`    |   True   |
| docker__graph                | Path to directory to store persistent data and resource configuration            | string |   `None`    |   True   |
| docker__hosts                | List of docker listen interfaces                                                 |  list  |   `fd://`   |   True   |
| docker__log_level            | Specifies the maxmimum libdm log level that will be forwarded to the dockerd log | string |   `info`    |   True   |
| docker__swarm                | is docker swarm                                                                  |  bool  |   `False`   |   True   |
| docker__swarm_advertise_addr | swarm advertise address                                                          | string |   `None`    |   True   |
| docker__swarm_init           | Socek swarm init                                                                 |  bool  |   `False`   |   True   |
| docker__swarm_join_addr      | list of swarm join addresses                                                     |  list  |    `[]`     |   True   |
| docker__swarm_join_token     | swarm join token for Manager or Worker                                           | string |   `None`    |   True   |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

This section describes static variables implemented in the role.

### Main variables

| Name | Description | Type | Default |
| -----| ----------- | :--: | :-----: |
| docker__service_name | Service name to be installed | string | `docker` |

**All static main variables are described in [vars/main.yml](vars/main.yml) file.**

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.
