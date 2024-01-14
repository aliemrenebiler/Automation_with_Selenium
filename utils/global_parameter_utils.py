"Global Parameter Utils"

from common.constants.config_schemas import GLOBAL_PARAMETERS_CONFIG_SCHEMA
from common.constants.file_and_folder_paths import GLOBAL_PARAMETERS_CONFIG_FILE_PATH
from models.global_parameters import GlobalParameters
from services.config_service import ConfigService


global_parameters = GlobalParameters()


def get_global_parameters():
    "Returns global parameters"

    return global_parameters


def set_global_parameters():
    "Sets global parameters from configuration file"

    config_service = ConfigService()

    configs = config_service.get_configs_from_file(
        GLOBAL_PARAMETERS_CONFIG_FILE_PATH,
        GLOBAL_PARAMETERS_CONFIG_SCHEMA,
    )

    global_parameters.timeout = configs["timeout"]
    global_parameters.login_timeout = configs["login_timeout"]
