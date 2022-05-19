# Copyright 2022 AGEPoly
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class AccountBankStatement(models.Model):

    _inherit = "account.bank.statement"

    def reconciliation_widget_preprocess(self):
        return super(
            AccountBankStatement, self.with_context(no_reassign_empty_name=True)
        ).reconciliation_widget_preprocess()

class AccountBankStatementLine(models.Model):

    _inherit = "account.bank.statement.line"

    # we add this field to have the time of the transaction
    # to be able to have filter multiple attribution on the same day
    complete_date = fields.Datetime('Date and time of transaction', required=False)

