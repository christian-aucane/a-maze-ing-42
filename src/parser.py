from .common import Config


def parse_config_file(config_file_path: str) -> Config | None:
    config = Config.read_file(config_file_path)
    if config is None:
        print(f"Config file '{config_file_path}' doesn't exist...")
    return config
