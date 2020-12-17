from src.get_id_from_api import api_funcs


def get_address_id():
    return api_funcs.get_address_list()["data"][0]["id"]
