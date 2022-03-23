class Config:
    db_dsn = "hive;"
    hs6_dir = "./hs6_des/"


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass


config = {"DEV": DevConfig,
          "PROD": ProdConfig}
