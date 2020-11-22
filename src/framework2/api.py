from src.framework2.common import DbUtil


def api_save_company():
    tag_id = _get_tag_id()


def _get_tag_id():
    # tag_name = ""
    tag_name = _get_tag_name()
    sql = "SELECT * FROM t_address WHERE del_tag=0 AND name = '%s'" % (tag_name)
    return DbUtil.execute(sql)[0]


def _get_tag_name():
    # 具体的获取tag name的方法
    pass
