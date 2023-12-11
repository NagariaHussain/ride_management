# Copyright (c) 2023, Hussain Nagaria and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{"fieldtype": "Data", "label": "Make", "fieldname": "make", "width": 300},
		{
			"fieldtype": "Currency",
			"label": "Total Revenue",
			"fieldname": "total_revenue",
			"width": 200,
		},
	]

	data = frappe.get_all(
		"Ride Booking",
		fields=["SUM(total_amount) AS total_revenue", "vehicle.make"],
		filters={"docstatus": 1},
		group_by="make",
	)

	# remove the rows with 0 total revenue
	data = [row for row in data if row.total_revenue > 0]
	
	chart = {
		"type": "pie",
		"data": {
			"labels": [row.make for row in data],
			"datasets": [
				{
					"values": [row.total_revenue for row in data]  
				}
			]
		}
	}

	total_revenue = sum(row.total_revenue for row in data)

	report_summary = [
		{
			"value": total_revenue,
			"indicator": "green" if total_revenue > 0 else "red",
			"label": "Total Revenue",
			"datatype": "Currency",
		},

		{
			"value": len(data),
			"label": "Total Money Making Makes",
			"datatype": "Int",
		}
	]
		
	

	# return columns, data
	return columns, data, "Third value in return tuple", chart, report_summary

