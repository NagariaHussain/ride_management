import frappe

@frappe.whitelist()
def get_emoji():
    return "🚗"