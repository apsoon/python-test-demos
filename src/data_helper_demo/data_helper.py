def get_role_id():
    role_name = _get_name("role_controller", "Addrole001", "new_role")
    # 剩下的就不写了


def get_dept_id():
    role_name = _get_name("role_controller", "Adddept001", "new_dept")
    # 剩下的就不写了


def _get_name(yaml_name, key_first, key_second):
    return read_yaml(yaml_name + ".yaml")[key_first][key_second]


def read_yaml(yaml_nam):
    # 具体就不写了
    return {}
