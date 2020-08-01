import os
from pattoo_shared.installation import configure, shared
from pattoo_shared import files


def install():
    """Start configuration process.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    if os.environ.get('PATTOO_CONFIGDIR') is None:
        os.environ['PATTOO_CONFIGDIR'] = '{0}etc{0}pattoo'.format(os.sep)
    config_directory = os.environ.get('PATTOO_CONFIGDIR')

    opcua_agent_dict = {
            'polling_interval': 300,
    }

    # Attempt to create configuration directory
    files.mkdir(config_directory)

    # Create the pattoo user and group
    configure.create_user('pattoo', '/nonexistent', ' /bin/false', True)

    # Attempt to change the ownership of the configuration directory
    shared.chown(config_directory)

    config_file = configure.pattoo_config(
                                        'pattoo_agent_opcuad',
                                        config_directory,
                                        opcua_agent_dict)

    configure.check_config(config_file, opcua_agent_dict)
