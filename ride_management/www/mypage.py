import frappe

def get_context(context):
    context.my_secret_message = "Secret message from context/mypage.py"
    context.drivers = frappe.db.get_all("Driver", fields=["first_name", "last_name"])