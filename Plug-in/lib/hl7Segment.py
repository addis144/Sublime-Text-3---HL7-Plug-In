# Handles the definition of the HL7 segments
class hl7Segment(object):
	def __init__(self, code, description):
		self.code = code
		self.description = description

	# Gets a segment object based on his code. If no object is found in the segmentList with the following code None is returned.
	def getSegmentByCode(self, code, segmentList):
		for listItem in segmentList:
			if (listItem.code == code):
				return listItem
		return None

	# Loads the entire segment list
	def loadSegmentList(self):
		hl7SegmentList = []

		hl7SegmentList.append(hl7Segment("ABS", "Abstract"))
		hl7SegmentList.append(hl7Segment("ACC", "Accident"))
		hl7SegmentList.append(hl7Segment("ADD", "Addendum"))
		hl7SegmentList.append(hl7Segment("ADJ", "Adjustment"))
		hl7SegmentList.append(hl7Segment("AFF", "Professional Affiliation"))
		hl7SegmentList.append(hl7Segment("AIG", "Appointment Information - General Resource"))
		hl7SegmentList.append(hl7Segment("AIL", "Appointment Information - Location Resource"))
		hl7SegmentList.append(hl7Segment("AIP", "Appointment Information - Personnel Resource"))
		hl7SegmentList.append(hl7Segment("AIS", "Appointment Information"))
		hl7SegmentList.append(hl7Segment("AL1", "Patient Allergy Information"))
		hl7SegmentList.append(hl7Segment("APR", "Appointment Preferences"))
		hl7SegmentList.append(hl7Segment("ARQ", "Appointment Request"))
		hl7SegmentList.append(hl7Segment("ARV", "Access Restriction"))
		hl7SegmentList.append(hl7Segment("AUT", "Authorization Information"))
		hl7SegmentList.append(hl7Segment("BHS", "Batch Header"))
		hl7SegmentList.append(hl7Segment("BLC", "Blood Code"))
		hl7SegmentList.append(hl7Segment("BLG", "Billing"))
		hl7SegmentList.append(hl7Segment("BPO", "Blood product order"))
		hl7SegmentList.append(hl7Segment("BPX", "Blood product dispense status"))
		hl7SegmentList.append(hl7Segment("BTS", "Batch Trailer"))
		hl7SegmentList.append(hl7Segment("BTX", "Blood Product Transfusion/Disposition"))
		hl7SegmentList.append(hl7Segment("BUI", "Blood Unit Information"))
		hl7SegmentList.append(hl7Segment("CDM", "Charge Description Master"))
		hl7SegmentList.append(hl7Segment("CDO", "Cumulative Dosage"))
		hl7SegmentList.append(hl7Segment("CER", "Certificate Detail"))
		hl7SegmentList.append(hl7Segment("CM0", "Clinical Study Master"))
		hl7SegmentList.append(hl7Segment("CM1", "Clinical Study Phase Master"))
		hl7SegmentList.append(hl7Segment("CM2", "Clinical Study Schedule Master"))
		hl7SegmentList.append(hl7Segment("CNS", "Clear Notification"))
		hl7SegmentList.append(hl7Segment("CON", "Consent Segment"))
		hl7SegmentList.append(hl7Segment("CSP", "Clinical Study Phase"))
		hl7SegmentList.append(hl7Segment("CSR", "Clinical Study Registration"))
		hl7SegmentList.append(hl7Segment("CSS", "Clinical Study Data Schedule Segment"))
		hl7SegmentList.append(hl7Segment("CTD", "Contact Data"))
		hl7SegmentList.append(hl7Segment("CTI", "Clinical Trial Identification"))
		hl7SegmentList.append(hl7Segment("DB1", "Disability"))
		hl7SegmentList.append(hl7Segment("DG1", "Diagnosis"))
		hl7SegmentList.append(hl7Segment("DMI", "DRG Master File Information"))
		hl7SegmentList.append(hl7Segment("DON", "Donation"))
		hl7SegmentList.append(hl7Segment("DRG", "Diagnosis Related Group"))
		hl7SegmentList.append(hl7Segment("DSC", "Continuation Pointer"))
		hl7SegmentList.append(hl7Segment("DSP", "Display Data"))
		hl7SegmentList.append(hl7Segment("ECD", "Equipment Command"))
		hl7SegmentList.append(hl7Segment("ECR", "Equipment Command Response"))
		hl7SegmentList.append(hl7Segment("EDU", "Educational Detail"))
		hl7SegmentList.append(hl7Segment("EQP", "Equipment/log Service"))
		hl7SegmentList.append(hl7Segment("EQU", "Equipment Detail"))
		hl7SegmentList.append(hl7Segment("ERR", "Error"))
		hl7SegmentList.append(hl7Segment("EVN", "Event Type"))
		hl7SegmentList.append(hl7Segment("FAC", "Facility"))
		hl7SegmentList.append(hl7Segment("FHS", "File Header"))
		hl7SegmentList.append(hl7Segment("FT1", "Financial Transaction"))
		hl7SegmentList.append(hl7Segment("FTS", "File Trailer"))
		hl7SegmentList.append(hl7Segment("GOL", "Goal Detail"))
		hl7SegmentList.append(hl7Segment("GP1", "Grouping/Reimbursement - Visit"))
		hl7SegmentList.append(hl7Segment("GP2", "Grouping/Reimbursement - Procedure Line Item"))
		hl7SegmentList.append(hl7Segment("GT1", "Guarantor"))
		hl7SegmentList.append(hl7Segment("Hxx", "any HL7 segment"))
		hl7SegmentList.append(hl7Segment("IAM", "Patient Adverse Reaction Information"))
		hl7SegmentList.append(hl7Segment("IAR", "Allergy Reaction"))
		hl7SegmentList.append(hl7Segment("IIM", "Inventory Item Master"))
		hl7SegmentList.append(hl7Segment("ILT", "Material Lot"))
		hl7SegmentList.append(hl7Segment("IN1", "Insurance"))
		hl7SegmentList.append(hl7Segment("IN2", "Insurance Additional Information"))
		hl7SegmentList.append(hl7Segment("IN3", "Insurance Additional Information, Certification"))
		hl7SegmentList.append(hl7Segment("INV", "Inventory Detail"))
		hl7SegmentList.append(hl7Segment("IPC", "Imaging Procedure Control Segment"))
		hl7SegmentList.append(hl7Segment("IPR", "Invoice Processing Results"))
		hl7SegmentList.append(hl7Segment("ISD", "Interaction Status Detail"))
		hl7SegmentList.append(hl7Segment("ITM", "Material Item"))
		hl7SegmentList.append(hl7Segment("IVC", "Invoice Segment"))
		hl7SegmentList.append(hl7Segment("IVT", "Material Location"))
		hl7SegmentList.append(hl7Segment("LAN", "Language Detail"))
		hl7SegmentList.append(hl7Segment("LCC", "Location Charge Code"))
		hl7SegmentList.append(hl7Segment("LCH", "Location Characteristic"))
		hl7SegmentList.append(hl7Segment("LDP", "Location Department"))
		hl7SegmentList.append(hl7Segment("LOC", "Location Identification"))
		hl7SegmentList.append(hl7Segment("LRL", "Location Relationship"))
		hl7SegmentList.append(hl7Segment("MFA", "Master File Acknowledgment"))
		hl7SegmentList.append(hl7Segment("MFE", "Master File Entry"))
		hl7SegmentList.append(hl7Segment("MFI", "Master File Identification"))
		hl7SegmentList.append(hl7Segment("MRG", "Merge Patient Information"))
		hl7SegmentList.append(hl7Segment("MSA", "Message Acknowledgment"))
		hl7SegmentList.append(hl7Segment("MSH", "Message Header"))
		hl7SegmentList.append(hl7Segment("NCK", "System Clock"))
		hl7SegmentList.append(hl7Segment("NDS", "Notification Detail"))
		hl7SegmentList.append(hl7Segment("NK1", "Next of Kin / Associated Parties"))
		hl7SegmentList.append(hl7Segment("NPU", "Bed Status Update"))
		hl7SegmentList.append(hl7Segment("NSC", "Application Status Change"))
		hl7SegmentList.append(hl7Segment("NST", "Application control level statistics"))
		hl7SegmentList.append(hl7Segment("NTE", "Notes and Comments"))
		hl7SegmentList.append(hl7Segment("OBR", "Observation Request"))
		hl7SegmentList.append(hl7Segment("OBX", "Observation/Result"))
		hl7SegmentList.append(hl7Segment("ODS", "Dietary Orders, Supplements, and Preferences"))
		hl7SegmentList.append(hl7Segment("ODT", "Diet Tray Instructions"))
		hl7SegmentList.append(hl7Segment("OM1", "General Segment"))
		hl7SegmentList.append(hl7Segment("OM2", "Numeric Observation"))
		hl7SegmentList.append(hl7Segment("OM3", "Categorical Service/Test/Observation"))
		hl7SegmentList.append(hl7Segment("OM4", "Observations that Require Specimens"))
		hl7SegmentList.append(hl7Segment("OM5", "Observation Batteries (Sets)"))
		hl7SegmentList.append(hl7Segment("OM6", "Observations that are Calculated from Other Observations"))
		hl7SegmentList.append(hl7Segment("OM7", "Additional Basic Attributes"))
		hl7SegmentList.append(hl7Segment("OMC", "Supporting Clinical Information Segment"))
		hl7SegmentList.append(hl7Segment("OMP", "Pharmacy/Treatment Order Message"))
		hl7SegmentList.append(hl7Segment("ORC", "Common Order"))
		hl7SegmentList.append(hl7Segment("ORG", "Practitioner Organization Unit"))
		hl7SegmentList.append(hl7Segment("ORP", "Pharmacy/Treatment Order Acknowledgment"))
		hl7SegmentList.append(hl7Segment("OVR", "Override Segment"))
		hl7SegmentList.append(hl7Segment("PAC", "Shipment Package"))
		hl7SegmentList.append(hl7Segment("PCE", "Patient Charge Cost Center Exceptions"))
		hl7SegmentList.append(hl7Segment("PCR", "Possible Causal Relationship"))
		hl7SegmentList.append(hl7Segment("PD1", "Patient Additional Demographic"))
		hl7SegmentList.append(hl7Segment("PDA", "Patient Death and Autopsy"))
		hl7SegmentList.append(hl7Segment("PDC", "Product Detail Country"))
		hl7SegmentList.append(hl7Segment("PEO", "Product Experience Observation"))
		hl7SegmentList.append(hl7Segment("PES", "Product Experience Sender"))
		hl7SegmentList.append(hl7Segment("PID", "Patient Identification"))
		hl7SegmentList.append(hl7Segment("PKG", "Item Packaging"))
		hl7SegmentList.append(hl7Segment("PM1", "Payer Master File Segment"))
		hl7SegmentList.append(hl7Segment("PMT", "Payment Information"))
		hl7SegmentList.append(hl7Segment("PR1", "Procedures"))
		hl7SegmentList.append(hl7Segment("PRA", "Practitioner Detail"))
		hl7SegmentList.append(hl7Segment("PRB", "Problem Details"))
		hl7SegmentList.append(hl7Segment("PRC", "Pricing"))
		hl7SegmentList.append(hl7Segment("PRD", "Provider Data"))
		hl7SegmentList.append(hl7Segment("PRT", "Participation Information"))
		hl7SegmentList.append(hl7Segment("PSG", "Product/Service Group"))
		hl7SegmentList.append(hl7Segment("PSH", "Product Summary Header"))
		hl7SegmentList.append(hl7Segment("PSL", "Product/Service Line Item"))
		hl7SegmentList.append(hl7Segment("PSS", "Product/Service Section"))
		hl7SegmentList.append(hl7Segment("PTH", "Pathway"))
		hl7SegmentList.append(hl7Segment("PV1", "Patient Visit"))
		hl7SegmentList.append(hl7Segment("PV2", "Patient Visit - Additional Information"))
		hl7SegmentList.append(hl7Segment("PYE", "Payee Information"))
		hl7SegmentList.append(hl7Segment("QAK", "Query Acknowledgment"))
		hl7SegmentList.append(hl7Segment("QID", "Query Identification"))
		hl7SegmentList.append(hl7Segment("QPD", "Query Parameter Definition"))
		hl7SegmentList.append(hl7Segment("QRD", "withdrawn"))
		hl7SegmentList.append(hl7Segment("QRF", "withdrawn"))
		hl7SegmentList.append(hl7Segment("QRI", "Query Response Instance"))
		hl7SegmentList.append(hl7Segment("RCP", "Response Control Parameter"))
		hl7SegmentList.append(hl7Segment("RDF", "Table Row Definition"))
		hl7SegmentList.append(hl7Segment("RDT", "Table Row Data"))
		hl7SegmentList.append(hl7Segment("REL", "Clinical Relationship Segment"))
		hl7SegmentList.append(hl7Segment("RF1", "Referral Information"))
		hl7SegmentList.append(hl7Segment("RFI", "Request for Information"))
		hl7SegmentList.append(hl7Segment("RGS", "Resource Group"))
		hl7SegmentList.append(hl7Segment("RMI", "Risk Management Incident"))
		hl7SegmentList.append(hl7Segment("ROL", "Role"))
		hl7SegmentList.append(hl7Segment("RQ1", "Requisition Detail-1"))
		hl7SegmentList.append(hl7Segment("RQD", "Requisition Detail"))
		hl7SegmentList.append(hl7Segment("RRD", "Pharmacy/Treatment Dispense Acknowledgement"))
		hl7SegmentList.append(hl7Segment("RXA", "Pharmacy/Treatment Administration"))
		hl7SegmentList.append(hl7Segment("RXC", "Pharmacy/Treatment Component Order"))
		hl7SegmentList.append(hl7Segment("RXD", "Pharmacy/Treatment Dispense"))
		hl7SegmentList.append(hl7Segment("RXE", "Pharmacy/Treatment Encoded Order"))
		hl7SegmentList.append(hl7Segment("RXG", "Pharmacy/Treatment Give"))
		hl7SegmentList.append(hl7Segment("RXO", "Pharmacy/Treatment Order"))
		hl7SegmentList.append(hl7Segment("RXR", "Pharmacy/Treatment Route"))
		hl7SegmentList.append(hl7Segment("RXV", "Pharmacy/Treatment Infusion"))
		hl7SegmentList.append(hl7Segment("SAC", "Specimen Container detail"))
		hl7SegmentList.append(hl7Segment("SCD", "Anti-Microbial Cycle Data"))
		hl7SegmentList.append(hl7Segment("SCH", "Scheduling Activity Information"))
		hl7SegmentList.append(hl7Segment("SCP", "Sterilizer Configuration (Anti-Microbial Devices)"))
		hl7SegmentList.append(hl7Segment("SDD", "Sterilization Device Data"))
		hl7SegmentList.append(hl7Segment("SFT", "Software Segment"))
		hl7SegmentList.append(hl7Segment("SGH", "Segment Group Header"))
		hl7SegmentList.append(hl7Segment("SGT", "Segment Group Trailer"))
		hl7SegmentList.append(hl7Segment("SHP", "Shipment"))
		hl7SegmentList.append(hl7Segment("SID", "Substance Identifier"))
		hl7SegmentList.append(hl7Segment("SLT", "Sterilization Lot"))
		hl7SegmentList.append(hl7Segment("SPM", "Specimen"))
		hl7SegmentList.append(hl7Segment("STF", "Staff Identification"))
		hl7SegmentList.append(hl7Segment("STZ", "Sterilization Parameter"))
		hl7SegmentList.append(hl7Segment("TCC", "Test Code Configuration"))
		hl7SegmentList.append(hl7Segment("TCD", "Test Code Detail"))
		hl7SegmentList.append(hl7Segment("TQ1", "Timing/Quantity"))
		hl7SegmentList.append(hl7Segment("TQ2", "Timing/Quantity Relationship"))
		hl7SegmentList.append(hl7Segment("TXA", "Transcription Document Header"))
		hl7SegmentList.append(hl7Segment("UAC", "User Authentication Credential Segment"))
		hl7SegmentList.append(hl7Segment("UB1", "UB82 Data"))
		hl7SegmentList.append(hl7Segment("UB2", "Uniform Billing Data"))
		hl7SegmentList.append(hl7Segment("URD", "withdrawn"))
		hl7SegmentList.append(hl7Segment("URS", "withdrawn"))
		hl7SegmentList.append(hl7Segment("VAR", "Variance"))
		hl7SegmentList.append(hl7Segment("VND", "Purchasing Vendor"))
		hl7SegmentList.append(hl7Segment("ZL7", "(proposed example only)"))
		hl7SegmentList.append(hl7Segment("Zxx", "any Z-Segment"))

		return hl7SegmentList