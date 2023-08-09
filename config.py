from dataclasses import dataclass
from environs import Env


@dataclass
class YaDisk:
    token: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    ya_disk: YaDisk


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('TG_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                  ya_disk=YaDisk(token=env('YA_TOKEN')))
