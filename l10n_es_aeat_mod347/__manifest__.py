# Copyright 2004-2011 - Pexego Sistemas Informáticos. (http://pexego.es)
# Copyright 2012 - NaN·Tic  (http://www.nan-tic.com)
# Copyright 2013 - Acysos (http://www.acysos.com)
# Copyright 2013 - Joaquín Pedrosa Gutierrez (http://gutierrezweb.es)
# Copyright 2016 - Tecnativa - Antonio Espinosa
# Copyright 2016 - Tecnativa - Angel Moya <odoo@tecnativa.com>
# Copyright 2014-2017 - Tecnativa - Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2018 - PESOL - Angel Moya <info@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "AEAT modelo 347",
    'version': "11.0.1.0.0",
    'author': "Pexego,"
              "ASR-OSS,"
              "NaN·tic,"
              "Acysos,"
              "Tecnativa,"
              "PESOL,"
              "Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/l10n-spain",
    'category': "Localisation/Accounting",
    'license': "AGPL-3",
    'depends': [
        "base_vat",
        "l10n_es_aeat",
        "account_tax_balance",
    ],
    'data': [
        "data/aeat_export_mod347_partner_data.xml",
        "data/aeat_export_mod347_real_state_data.xml",
        "data/aeat_export_mod347_data.xml",
        "data/tax_code_map_mod347_data.xml",
        "security/ir.model.access.csv",
        "security/mod_347_security.xml",
        "views/account_invoice_view.xml",
        "views/account_move_view.xml",
        "views/res_partner_view.xml",
        "views/mod347_view.xml",
        "views/report_347_partner.xml",
        "data/mail_template_data.xml",
        "wizards/l10n_es_aeat_mod347_send_mail_view.xml"
    ],
    'installable': True,
    'images': [
        'images/l10n_es_aeat_mod347.png',
    ],
}
