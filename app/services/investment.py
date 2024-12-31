from datetime import datetime

from app.models import CharityProject, Donation


def invest_donations(
    target: CharityProject,
    sources: list[Donation]
) -> list[Donation]:
    target.invested_amount = target.invested_amount or 0
    target.full_amount = target.full_amount or 0
    required_project_amount = target.full_amount - target.invested_amount
    for donation in sources:
        donation_amount = donation.full_amount - donation.invested_amount
        if required_project_amount <= 0:
            break
        invest_amount = min(donation_amount, required_project_amount)
        donation.invested_amount += invest_amount
        target.invested_amount += invest_amount
        required_project_amount -= invest_amount
        if (donation.invested_amount == donation.full_amount and
                not donation.close_date):
            donation.fully_invested = True
            donation.close_date = datetime.now()
        if (target.invested_amount == target.full_amount and
                not target.close_date):
            target.fully_invested = True
            target.close_date = datetime.now()
    return sources
