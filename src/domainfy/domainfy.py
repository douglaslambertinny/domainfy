#!/usr/bin/env python
from .notify_mac import notify
from urllib3 import PoolManager
from typing import Mapping
import time

AVALIABLE = 0
AVALIABLE_DOMAIN_WITH_TICKETS = 1
REGISTERED_DOMAIN = 2
UNAVALIABLE_DOMAIN = 3
INVALID_DOMAIN = 4
WAITING_DOMAIN = 5
WAITING_DOMAIN_WITH_TICKETS = 6
ERROR = 8
COMPETITIVE_DOMAIN = 9
UNKNOWN = 10

class RegistroBR:

    messages = {
        AVALIABLE: "Avaliable",
        AVALIABLE_DOMAIN_WITH_TICKETS: "Avaliable with tickets",
        REGISTERED_DOMAIN: "Registered",
        UNAVALIABLE_DOMAIN: "Unavaliable",
        INVALID_DOMAIN: "Invalid",
        WAITING_DOMAIN: "Waiting",
        WAITING_DOMAIN_WITH_TICKETS: "Waiting with tickets",
        ERROR: "Error",
        COMPETITIVE_DOMAIN: "Competitive",
        UNKNOWN: "Unknown",
    }

    def __init__(self, domain):
        self.domain = domain

    def check_domain(self):
        http = PoolManager()
        r = http.request(
            "GET", f"https://brasilapi.com.br/api/registrobr/v1/{self.domain}"
        )
        if r.status == 200:
            data = r.json()
            if data.get("status_code") == AVALIABLE:
                notify(
                    f"{self.domain} is {self.messages[data.get('status_code')]}",
                    f"Expires at {data.get('expires_at')}",
                )
            if data.get("status_code") == REGISTERED_DOMAIN:
                notify(
                    f"{self.domain} is {self.messages[data.get('status_code')]}",
                    f"Expires at {data.get('expires_at')}",
                )
            elif data.get("status_code") == AVALIABLE_DOMAIN_WITH_TICKETS:
                notify(
                    f"{self.domain} is {self.messages[data.get('status_code')]}",
                    f"Expires at {data.get('expires_at')}",
                )
            elif data.get("status_code") == WAITING_DOMAIN_WITH_TICKETS:
                notify(
                    f"{self.domain} is {self.messages[data.get('status_code')]}",
                    f"Expires at {data.get('expires_at')}",
                )


class IntervalRunner:
    def __init__(self, interval, callback):
        self.interval = interval
        self.callback = callback

    def run(self):
        while True:
            self.callback()
            time.sleep(self.interval)

class Domainfy(Mapping):
    def __init__(self, domains):
        self.domains = domains

    def __getitem__(self, key):
        return self.domains[key]

    def __iter__(self):
        return iter(self.domains)

    def __len__(self):
        return len(self.domains)

    def check_domains(self):
        for domain in self.domains:
            RegistroBR(domain).check_domain()

