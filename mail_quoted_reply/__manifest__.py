# Copyright 2021 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Mail Message Reply",
    "summary": """
        Make a reply using a message""",
    "version": "16.0.1.0.3",
    "license": "AGPL-3",
    "author": "Creu Blanca,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/social",
    "depends": ["mail"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "/mail_quoted_reply/static/src/models/*.js",
        ],
    },
}
