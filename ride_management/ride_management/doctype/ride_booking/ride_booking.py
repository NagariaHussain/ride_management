# Copyright (c) 2023, Hussain Nagaria and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def before_save(self):
		self.set_item_amounts()
		self.set_total_amount()

	def set_item_amounts(self):
		# iterate over all the items
		# calculate `amount = price_per_km * distance_in_km`
		# default_price_per_km = frappe.db.get_single_value("Ride App Settings", "price_per_km")
		for item in self.items:
			item.amount = self.price_per_km * item.distance_in_km
	
	def set_total_amount(self):
		self.total_amount = sum(i.amount for i in self.items)