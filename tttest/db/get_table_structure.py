# -*- coding: utf-8 -*-
# @Time : 2024/1/9 10:52
# from tttest.config.db_config import db
from tttest.config.db_config import init_db


def get_table_structure(table_name, db_config_path):
    # columns = db.get_columns(table_name)
    # for column in columns:
    #     print(f'字段名：{column.name}  字段类型：{column.data_type} ')
    # 如果是表名，获取表结构，如果是all，获取所有表结构,多个表用，分隔
    if table_name == 'all':
        query = "SHOW TABLES"
        cursor = init_db(db_config_path).execute_sql(query)
        tables = cursor.fetchall()
        return [[table[0], get_table_columns(table[0], db_config_path)] for table in tables]

    else:
        return [[x, get_table_columns(x, db_config_path)] for x in table_name.split(',') if x]


def get_table_columns(table_name, project):
    print(f'获取表名：{table_name}')
    query = """
            SELECT COLUMN_NAME, DATA_TYPE,COLUMN_COMMENT
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = %s AND table_schema = DATABASE()
                ORDER BY ordinal_position
            """
    cursor = init_db(project).execute_sql(query, (table_name,))
    columns = cursor.fetchall()
    print(columns)
    return columns
