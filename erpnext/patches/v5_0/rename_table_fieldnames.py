# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe.model import rename_field
from frappe.modules import scrub, get_doctype_module

rename_map = {
	# "Opportunity": [
	# 	["enquiry_details", "items"]
	# ],
	# "Quotation": [
	# 	["quotation_details", "items"],
	# 	["other_charges", "taxes"]
	# ],
	# "Sales Order": [
	# 	["sales_order_details", "items"],
	# 	["other_charges", "taxes"],
	# 	["packing_details", "packed_items"]
	# ],
	# "Delivery Note": [
	# 	["delivery_note_details", "items"],
	# 	["other_charges", "taxes"],
	# 	["packing_details", "packed_items"]
	# ],
	"Sales Invoice": [
		["entries", "items"],
		# ["other_charges", "taxes"],
		# ["packing_details", "packed_items"],
		# ["advance_adjustment_details", "advances"]
	],
	# "Material Request": [
	# 	["indent_details", "items"]
	# ],
	# "Supplier Quotation": [
	# 	["quotation_items", "items"],
	# 	["other_charges", "taxes"]
	# ],
	# "Purchase Order": [
	# 	["po_details", "items"],
	# 	["other_charges", "taxes"],
	# 	["po_raw_material_details", "supplied_items"]
	# ],
	# "Purchase Receipt": [
	# 	["purchase_receipt_details", "items"],
	# 	["other_charges", "taxes"],
	# 	["pr_raw_material_details", "supplied_items"]
	# ],
	"Purchase Invoice": [
		["entries", "items"],
		# ["other_charges", "taxes"],
		# ["advance_allocation_details", "advances"]
	],
	# "Production Order": [
	# 	["production_order_operations", "operations"]
	# ],
	# "BOM": [
	# 	["bom_operations", "operations"],
	# 	["bom_materials", "items"],
	# 	["flat_bom_details", "exploded_items"]
	# ],
	# "Payment Reconciliation": [
	# 	["payment_reconciliation_payments", "payments"],
	# 	["payment_reconciliation_invoices", "invoices"]
	# ],
	# "Sales Taxes and Charges Master": [
	# 	["other_charges", "taxes"],
	# 	["valid_for_territories", "territories"]
	# ],
	# "Purchase Taxes and Charges Master": [
	# 	["other_charges", "taxes"]
	# ],
	# "Shipping Rule": [
	# 	["shipping_rule_conditions", "conditions"],
	# 	["valid_for_territories", "territories"]
	# ],
	# "Price List": [
	# 	["valid_for_territories", "territories"]
	# ],
	# "Appraisal": [
	# 	["appraisal_details", "goals"]
	# ],
	# "Appraisal Template": [
	# 	["kra_sheet", "goals"]
	# ],
	"Bank Reconciliation": [
		["entries", "journal_entries"]
	],
	# "Cost Center": [
	# 	["budget_details", "budgets"]
	# ],
	# "C-Form": [
	# 	["invoice_details", "invoices"]
	# ],
	# "Customize Form": [
	# 	["customize_form_fields", "fields"]
	# ],
	# "Email Alert": [
	# 	["email_alert_recipients", "recipients"]
	# ],
	# "Employee": [
	# 	["employee_leave_approvers", "leave_approvers"],
	# 	["educational_qualification_details", "educational_qualifications"],
	# 	["previous_experience_details", "external_work_experiences"],
	# 	["experience_in_company_details", "internal_work_experiences"]
	# ],
	# "Event": [
	# 	["event_individuals", "users"],
	# 	["event_roles", "roles"]
	# ],
	# "Expense Claim": [
	# 	["expense_voucher_details", "expenses"]
	# ],
	# "Fiscal Year": [
	# 	["fiscal_year_companies", "companies"]
	# ],
	# "Holiday List": [
	# 	["holiday_list_details", "holidays"]
	# ],
	# "Installation Note": [
	# 	["installed_item_details", "items"]
	# ],
	# "Item": [
	# 	["item_variants", "variants"],
	# 	["item_reorder", "reorder_levels"],
	# 	["uom_conversion_details", "uoms"],
	# 	["item_supplier_details", "supplier_item_codes"],
	# 	["item_customer_details", "customer_item_codes"],
	# 	["item_tax", "taxes"],
	# 	["item_specification_details", "quality_parameters"],
	# 	["item_website_specifications", "website_specifications"]
	# ],
	# "Item Group": [
	# 	["item_website_specifications", "website_specifications"]
	# ],
	# "Landed Cost Voucher": [
	# 	["landed_cost_purchase_receipts", "purchase_receipts"],
	# 	["landed_cost_items", "items"],
	# 	["landed_cost_taxes_and_charges", "taxes"]
	# ],
	# "Maintenance Schedule": [
	# 	["item_maintenance_detail", "items"],
	# 	["maintenance_schedule_detail", "schedules"]
	# ],
	# "Maintenance Visit": [
	# 	["maintenance_visit_details", "purposes"]
	# ],
	# "Packing Slip": [
	# 	["item_details", "items"]
	# ],
	# "Customer": [
	# 	["party_accounts", "accounts"]
	# ],
	# "Customer Group": [
	# 	["party_accounts", "accounts"]
	# ],
	# "Supplier": [
	# 	["party_accounts", "accounts"]
	# ],
	# "Supplier Type": [
	# 	["party_accounts", "accounts"]
	# ],
	# "Payment Tool": [
	# 	["payment_tool_details", "against_vouchers"]
	# ],
	# "Production Planning Tool": [
	# 	["pp_so_details", "sales_orders"],
	# 	["pp_details", "items"]
	# ],
	# "Project": [
	# 	["project_milestones", "milestones"]
	# ],
	# "Quality Inspection": [
	# 	["qa_specification_details", "readings"]
	# ],
	# "Salary Slip": [
	# 	["earning_details", "earnings"],
	# 	["deduction_details", "deductions"]
	# ],
	# "Salary Structure": [
	# 	["earning_details", "earnings"],
	# 	["deduction_details", "deductions"]
	# ],
	# "Sales BOM": [
	# 	["sales_bom_items", "items"]
	# ],
	# "SMS Settings": [
	# 	["static_parameter_details", "static_parameters"]
	# ],
	# "Stock Entry": [
	# 	["mtn_details", "items"]
	# ],
	# "Sales Partner": [
	# 	["partner_target_details", "targets"]
	# ],
	# "Sales Person": [
	# 	["target_details", "targets"]
	# ],
	# "Territory": [
	# 	["target_details", "targets"]
	# ],
	# "Time Log Batch": [
	# 	["time_log_batch_details", "time_logs"]
	# ],
	# "Workflow": [
	# 	["workflow_document_states", "document_states"],
	# 	["workflow_transitions", "transitions"]
	# ],
	# "Workstation": [
	# 	["workstation_operation_hours", "working_hours"]
	# ],
}

def execute():
	#rename table fieldnames
	for dn in rename_map:
		frappe.reload_doc(get_doctype_module(dn), "doctype", scrub(dn))

	for dt, field_list in rename_map.items():
		for field in field_list:
			rename_field(dt, field[0], field[1])

	# rename doctypes
	tables = frappe.db.sql_list("show tables")
	for old_dt, new_dt in [["Journal Voucher Detail", "Journal Entry Account"],
		["Journal Voucher", "Journal Entry"],
		["Budget Distribution Detail", "Monthly Distribution Percentage"],
		["Budget Distribution", "Monthly Distribution"]]:
			if "tab"+old_dt not in tables:
				frappe.rename_doc("DocType", old_dt, new_dt, force=True)