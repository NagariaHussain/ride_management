// Copyright (c) 2023, Hussain Nagaria and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue by Make"] = {
	"filters": [
		
	],
	onload(report) {
		report.page.add_button("My Other Report", () => {
			frappe.set_route("query-report", "My Other Report")
		})
	}
};
