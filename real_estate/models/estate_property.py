from odoo import models, fields
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):

    _name = "estate.property"
    _description = "A module to manage real estate properties"

    active = fields.Boolean(default=True)

    state = fields.Selection(
        required=True,
        copy=False,
        default="new",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer", "Offer"),
            ("accepted", "Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
    )

    name = fields.Char(string="Title", default="House", required=True)
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date(
        string="Available From",
        copy=False,
        default=fields.Date.today() + relativedelta(months=3),
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ]
    )

    property_type_id = fields.Many2one(comodel_name="estate.property.type")
    buyer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Buyer",
        copy=False,
    )
    seller_id = fields.Many2one(
        comodel_name="res.users",
        string="Salesperson",
        index=True,
        default=lambda self: self.env.user,
        domain=[("share", "=", False)],
    )
