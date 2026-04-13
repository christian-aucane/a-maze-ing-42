from .common import Config


def parse_config_file(config_file_path: str) -> Config | None:
    list_parse: 
    config: dict = {}
    with open(config_file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=")
            config[key] = value

    config = Config.read_file(config_file_path)
    if config is None:
        print(f"Config file '{config_file_path}' doesn't exist...")
    return config
