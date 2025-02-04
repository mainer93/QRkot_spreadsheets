from app.core.config import settings


class Constants:
    SHEET_VERSION = 'v4'
    FORMAT = "%Y/%m/%d %H:%M:%S.%f"
    SHEET_ID = 0
    SHEET_TITLE = 'Лист1'
    ROWS_COUNT = 100
    COLUMN_COUNT = 11
    SPREADSHEET_BODY = {
        'properties': {
            'title': 'Отчёт',
            'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': SHEET_ID,
                                   'title': SHEET_TITLE}}]}
    TABLE_VALUES = [
        ['Отчёт от', '{now_date_time}'],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    DRIVE_VERSION = 'v3'
    PERMISSION_BODY = {'type': 'user',
                       'role': 'writer',
                       'emailAddress': settings.email}
    ROWS_EXCEED_LIMIT = (
        'Количество строк в переданных данных '
        '({current_rows_numbers}) превышает максимально '
        'допустимое количество строк в таблице'
    )
    COLUMNS_EXCEED_LIMIT = (
        'Количество столбцов в переданных данных '
        '({current_columns_numbers}) превышает максимально '
        'допустимое количество столбцов в таблице'
    )
    RANGE_TEMPLATE = 'R1C1:R{rows}C{columns}'
