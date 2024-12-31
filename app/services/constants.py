from datetime import datetime

from app.core.config import settings


class Constants:
    SHEET_VERSION = 'v4'
    FORMAT = "%Y/%m/%d %H:%M:%S.%f"
    now_date_time = datetime.now().strftime(FORMAT)
    SHEET_ID = 0
    SHEET_TITLE = 'Лист1'
    ROWS_COUNT = 100
    COLUMN_COUNT = 11
    SPREADSHEET_BODY = {'properties': {'title': f'Отчёт от {now_date_time}',
                                       'locale': 'ru_RU'},
                        'sheets': [{'properties': {'sheetType': 'GRID',
                                                   'sheetId': SHEET_ID,
                                                   'title': SHEET_TITLE,
                                                   'gridProperties': {
                                                       'rowCount': ROWS_COUNT,
                                                       'columnCount':
                                                           COLUMN_COUNT}}}]}
    DRIVE_VERSION = 'v3'
    PERMISSION_BODY = {'type': 'user',
                       'role': 'writer',
                       'emailAddress': settings.email}
    TABLE_VALUES = [
        ['Отчёт от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    UPDATE_BODY = {
        'majorDimension': 'ROWS',
        'values': TABLE_VALUES
    }