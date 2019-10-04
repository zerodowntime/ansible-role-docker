import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_service_is_runnning(host):
    command = host.command('systemctl status docker')
    assert command.stdout.find('running') > -1, "Docker service is disabled"


def test_docker_storage_driver(host):
    command = host.command('sudo docker info')
    assert command.stdout.find('overlay2') > -1, "Wrong storage driver"


def test_docker_logging_driver(host):
    command = host.command('sudo docker info')
    assert command.stdout.find('json-file') > -1, "Wrong logging driver"
