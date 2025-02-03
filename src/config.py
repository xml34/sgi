from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "My SGI Project"
    oauth_token_secret: str = "my_dev_secret"
    model_config = SettingsConfigDict(env_file="./secrets/pg.ini")


settings = Settings()
