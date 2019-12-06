# docker

Install docker

## Requirements

- Ansible >= 2.8

### Supported platforms

```yml
- EL
  - 7
- Ubuntu
  - bionic
  - xenial
```

## Default role variables

| Name                            | Description                                                                      |  Type  |          Default           |
| ------------------------------- | -------------------------------------------------------------------------------- | :----: | :------------------------: |
| docker__package_state           | Package state `present`,`latest`                                                 | string |         `present`          |
| docker__storage_driver          | Docker storage driver                                                            | string |         `overlay2`         |
| docker__package_name            | Package name to be installed                                                     | string |        `docker-ce`         |
| docker__package_version         | Package version to be installed                                                  | string |          required          |
| docker__debug                   | Enable debug mode                                                                |  bool  |          required          |
| docker__ip_masq                 | Enable IP masquerading                                                           |  bool  |           `True`           |
| docker__iptables                | Enable addition of iptables rules                                                |  bool  |           `True`           |
| docker__log_driver              | Default driver for container logs                                                | string |        `json-file`         |
| docker__log_driver_opts         | Log options                                                                      |  dict  |          required          |
| docker__graph                   | Path to directory to store persistent data and resource configuration            | string |          required          |
| docker__hosts                   | List of docker listen interfaces                                                 |  list  |          `fd://`           |
| docker__log_level               | Specifies the maxmimum libdm log level that will be forwarded to the dockerd log | string |           `info`           |
| docker__swarm                   | is docker swarm                                                                  |  bool  |          required          |
| docker__swarm_advertise_addr    | swarm advertise address                                                          | string |          required          |
| docker__swarm_init              | Socek swarm init                                                                 |  bool  |          required          |
| docker__swarm_join_addr         | list of swarm join addresses                                                     |  list  |            `[]`            |
| docker__swarm_join_token        | swarm join token for Manager or Worker                                           | string |          required          |
| docker__insecure_registries     | list of docker insecure registry                                                 | list,  |            `[]`            |
| docker__availability            | docker availability mode                                                         | string |          required          |
| docker__swarm_node_labels       | docker swarm - labels of the node                                                |  list  |            `{}`            |
| docker__swarm_node_name         | docker swarm - name of node                                                      |  list  |      `{{ hostname }}`      |
| docker__networks                | docker networks                                                                  |  list  |            `[]`            |
| docker__delegate_to_master_host | docker swarm - swarm master to execute master exclusive tasks                    |  list  | `{{ inventory_hostname }}` |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

This section describes static variables implemented in the role.

### Main variables

| Name                 | Description                  |  Type  | Default  |
| -------------------- | ---------------------------- | :----: | :------: |
| docker__service_name | Service name to be installed | string | `docker` |

**All static main variables are described in [vars/main.yml](vars/main.yml) file.**

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.
