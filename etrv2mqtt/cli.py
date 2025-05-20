import sys

from loguru import logger

from etrv2mqtt.config import Config
from etrv2mqtt.devices import DeviceManager, TRVDevice
import pkg_resources  # part of setuptools

def main(config_file: str):
    try:
        config = Config(config_file)
    except Exception as e:
        logger.error(e)
        sys.exit(1)
    # https://stackoverflow.com/questions/2058802/how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package
    logger.info('Starting etrv2mqtt V' + pkg_resources.get_distribution(__package__).version)
    deviceManager = DeviceManager(config, TRVDevice)
    deviceManager.poll_forever()


@logger.catch
def entrypoint():
    if len(sys.argv) < 2:
        logger.error('Usage: '+sys.argv[0]+' configfile.json')
        sys.exit(1)

    try:
        logger.info(sys.argv[0] + ' is starting')
        main(sys.argv[1])
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    entrypoint()
