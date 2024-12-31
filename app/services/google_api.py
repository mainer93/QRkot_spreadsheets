from aiogoogle import Aiogoogle

from app.services.constants import Constants


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
    for project in projects:
        new_row = [str(project.name),
                   str(project.close_date - project.create_date),
                   str(project.description)]
        Constants.TABLE_VALUES.append(new_row)

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=Constants.UPDATE_BODY
        )
    )
