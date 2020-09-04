import yaml


def read_data():
    with open("../mydata/data.yaml", encoding='utf-8') as f:
        ds = yaml.safe_load(f)
        return ds
