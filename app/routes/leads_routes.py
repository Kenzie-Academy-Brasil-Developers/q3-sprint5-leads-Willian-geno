from flask import Blueprint
from app.controllers import leads_controllers

bp=Blueprint("leads", __name__, url_prefix=("/leads"))

bp.post("")(leads_controllers.create_leads)
bp.get("")(leads_controllers.retrive_leads)
bp.patch("")(leads_controllers.retrive_leads_by_email)
bp.delete("")(leads_controllers.delete_leads_by_email)
