import yaml
import json
from configparser import ConfigParser
from common.logger import logger


class MyConfigParser(ConfigParser):
    """
    Custom ConfigParser class that overrides the optionxform function
    to prevent converting option keys to lowercase in .ini files.
    """

    def __init__(self, defaults=None):
        """
        Initialize the MyConfigParser class.

        Args:
            defaults (Optional[dict]): Default values for the parser.
        """
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        """
        Override the optionxform function to return the option key as is.

        Args:
            optionstr (str): The option key.

        Returns:
            str: The option key.
        """
        return optionstr


class ReadFileData():
    """
    Class for reading data from different file formats.
    """

    def __init__(self):
        """
        Initialize the ReadFileData class.
        """
        pass

    def load_yaml(self, file_path):
        """
        Load data from a YAML file.

        Args:
            file_path (str): The path to the YAML file.

        Returns:
            dict: The loaded data.
        """
        logger.info("Loading {} file...".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("Data loaded: {}".format(data))
        return data

    def load_json(self, file_path):
        """
        Load data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The loaded data.
        """
        logger.info("Loading {} file...".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("Data loaded: {}".format(data))
        return data

    def load_ini(self, file_path):
        """
        Load data from an INI file.

        Args:
            file_path (str): The path to the INI file.

        Returns:
            dict: The loaded data.
        """
        logger.info("Loading {} file...".format(file_path))      #使用日志记录方式输出正在加载的文件路径信息。file_path 是要加载的 INI 文件的路径。
        config = MyConfigParser()        #创建一个 MyConfigParser 类的实例，该类用于解析 INI 配置文件。
        config.read(file_path, encoding="UTF-8")    #调用 read 方法读取指定的 INI 文件，并指定编码为 UTF-8。read 方法将会解析文件内容并加载到 config 对象中。
        data = dict(config._sections)    #将 config 对象的数据转换为字典格式。config._sections 是一个私有属性，它包含了解析后的配置文件中的所有节（sections）和对应的键值对。
        return data


data = ReadFileData()
