// Copyright (c) 2023, Hussain Nagaria and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
       frm.add_custom_button("Change Rate", () => {
        frappe.prompt({
            fieldname: "rate",
            label: "Rate",
            fieldtype: "Float",
            reqd: 1,
        }, (data) => {
            frm.set_value("price_per_km", data.rate)
            frm.save()
        })
       })
	},
    price_per_km(frm) {
        console.log("price per km changed");
        for(let item of frm.doc.items) {
            const amount = frm.doc.price_per_km * item.distance_in_km;
            item.amount = amount;
        }

        frm.refresh_field("items");
    },
    
});


frappe.ui.form.on("Ride Booking Item", {
    distance_in_km(frm, cdt, cdn) {
        // which row?
        const row = frappe.get_doc(cdt, cdn)

        // update the amount for that row
        row.amount = row.distance_in_km * frm.doc.price_per_km;

        frm.refresh_field("items");
    }
})