from datetime import datetime

from aiogoogle import Aiogoogle

from app.services.constants import Constants
from app.services.exceptions import TableLimitError


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    service = await wrapper_services.discover('sheets',
                                              Constants.SHEET_VERSION)
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=Constants.SPREADSHEET_BODY)
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('drive',
                                              Constants.DRIVE_VERSION)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=Constants.PERMISSION_BODY,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('sheets',
                                              Constants.SHEET_VERSION)
    now_date_time = datetime.now().strftime(Constants.FORMAT)
    table_values = [
        ['Отчёт от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    for project in projects:
        new_row = [str(project.name),
                   str(project.close_date - project.create_date),
                   str(project.description)]
        table_values.append(new_row)
    current_rows_numbers = len(table_values)
    current_columns_numbers = max(len(row) for row in table_values)
    if current_rows_numbers > Constants.ROWS_COUNT:
        raise TableLimitError(
            Constants.ROWS_EXCEED_LIMIT.format(
                current_rows_numbers=current_rows_numbers))
    if current_columns_numbers > Constants.COLUMN_COUNT:
        raise TableLimitError(
            Constants.COLUMNS_EXCEED_LIMIT.format(
                current_columns_numbers=current_columns_numbers))
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range=Constants.RANGE_TEMPLATE.format(
                rows=current_rows_numbers,
                columns=current_columns_numbers),
            valueInputOption='USER_ENTERED',
            json=update_body))
