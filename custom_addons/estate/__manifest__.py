# this file must describe module and cannot remain empty.
# only required field is the "name"


{
    "name": "Real Estate",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml",
    ],
    "installable": True,
}
