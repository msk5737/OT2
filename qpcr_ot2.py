from opentrons import protocol_api

# tweakable settings
wells_to_load = [1,2,3,4,5,6,7,8,9,10,11,12] # the range of columns to load from the 96 well plate
mm_well = 'A1' # which well of 12-well reservoir is the mastermix in?
loadmastermix = True #if mastermix is to be loaded from 12-well reservoir or if it has been manually pipetted True/False
volume_mastermix = 8 # 8ul requires a total of 312 reactions which should be 340 to be safe (340 10x mix, 680 water, 1700 MM).
volume_template = 2 

#The layout of the recipient plate will be as follows:
#A1	A1	A1	A2	A2	A2	A3	A3	A3	A4	A4	A4	A5	A5	A5	A6	A6	A6	A7	A7	A7	A8	A8	A8
#A9	A9	A9	A10	A10	A10	A11	A11	A11	A12	A12	A12	empty	empty	empty	empty	empty	empty	empty	empty	empty	STD1	STD1	STD1
#B1	B1	B1	B2	B2	B2	B3	B3	B3	B4	B4	B4	B5	B5	B5	B6	B6	B6	B7	B7	B7	B8	B8	B8
#B9	B9	B9	B10	B10	B10	B11	B11	B11	B12	B12	B12	empty	empty	empty	empty	empty	empty	empty	empty	empty	STD2	STD2	STD2
#C1	C1	C1	C2	C2	C2	C3	C3	C3	C4	C4	C4	C5	C5	C5	C6	C6	C6	C7	C7	C7	C8	C8	C8
#C9	C9	C9	C10	C10	C10	C11	C11	C11	C12	C12	C12	empty	empty	empty	empty	empty	empty	empty	empty	empty	STD3	STD3	STD3
#D1	D1	D1	D2	D2	D2	D3	D3	D3	D4	D4	D4	D5	D5	D5	D6	D6	D6	D7	D7	D7	D8	D8	D8
#D9	D9	D9	D10	D10	D10	D11	D11	D11	D12	D12	D12	empty	empty	empty	empty	empty	empty	empty	empty	empty	STD4	STD4	STD4
#E1	E1	E1	E2	E2	E2	E3	E3	E3	E4	E4	E4	E5	E5	E5	E6	E6	E6	E7	E7	E7	E8	E8	E8
#E9	E9	E9	E10	E10	E10	E11	E11	E11	E12	E12	E12	empty	empty	empty	empty	empty	empty	empty	empty	empty	STD5	STD5	STD5
#F1	F1	F1	F2	F2	F2	F3	F3	F3	F4	F4	F4	F5	F5	F5	F6	F6	F6	F7	F7	F7	F8	F8	F8
#F9	F9	F9	F10	F10	F10	F11	F11	F11	F12	F12	F12	empty	empty	empty	empty	empty	empty	empty	empty	empty	STD6	STD6	STD6
#G1	G1	G1	G2	G2	G2	G3	G3	G3	G4	G4	G4	G5	G5	G5	G6	G6	G6	G7	G7	G7	G8	G8	G8
#G9	G9	G9	G10	G10	G10	G11	G11	G11	G12	G12	G12	empty	empty	empty	empty	empty	empty	empty	empty	empty	STD7	STD7	STD7
#H1	H1	H1	H2	H2	H2	H3	H3	H3	H4	H4	H4	H5	H5	H5	H6	H6	H6	H7	H7	H7	H8	H8	H8
#H9	H9	H9	H10	H10	H10	H11	H11	H11	H12	H12	H12	empty	empty	empty	empty	empty	empty	empty	empty	empty	NTC	NTC	NTC

# a dictionary to map the first well of each
lookup = {
	"1": ['A', 1],
	"2": ['A', 4],
	"3": ['A', 7],
	"4": ['A', 10],
	"5": ['A', 13],
	"6": ['A', 16],
	"7": ['A', 19],
	"8": ['A', 22],
	"9": ['B', 1],
	"10": ['B', 4],
	"11": ['B', 7],
	"12": ['B', 10]
	}

# metadata
metadata = {
	'protocolName': 'qPCR', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Set up a 384 well qPCR plate from templates in a 96 well working by columns',
	'apiLevel': '2.7'
}

def run(protocol: protocol_api.ProtocolContext):

	# define labware and locations
	if loadmastermix: reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2') # 12 well reservoir with pcr mastermix in A1
	qpcr_plate = protocol.load_labware('biorad384pcrplate_384_wellplate_40ul', '1') # skirted 384 well plate of amplicons
	template_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '4') # skirted 96 well plate containing extracted DNA
	tips1 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '3')
	tips2 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '6')

	# define pipettes
	#p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips4, tips7])
	mp20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips1, tips2])

	if loadmastermix:
		mp20.pick_up_tip() # only using a single set of tips to load mastermix as is same in every well.
		#Standard Curve Wells
		mp20.aspirate(volume_mastermix, reservoir[mm_well])
		mp20.dispense(volume_mastermix, qpcr_plate['B22'])
		mp20.aspirate(volume_mastermix, reservoir[mm_well])
		mp20.dispense(volume_mastermix, qpcr_plate['B23'])
		mp20.aspirate(volume_mastermix, reservoir[mm_well])
		mp20.dispense(volume_mastermix, qpcr_plate['B24'])
		
		for i in wells_to_load:			
			mp20.aspirate(volume_mastermix, reservoir[mm_well])
			mp20.dispense(volume_mastermix, qpcr_plate[lookup[str(i)][0]+str(lookup[str(i)][1])])
			mp20.aspirate(volume_mastermix, reservoir[mm_well])
			mp20.dispense(volume_mastermix, qpcr_plate[lookup[str(i)][0]+str(lookup[str(i)][1]+1)])
			mp20.aspirate(volume_mastermix, reservoir[mm_well])
			mp20.dispense(volume_mastermix, qpcr_plate[lookup[str(i)][0]+str(lookup[str(i)][1]+2)])
		mp20.drop_tip()

	# add the templates and do dilution series
	for i in wells_to_load: 
		mp20.pick_up_tip()
		mp20.aspirate(volume_template*3.2, template_plate['A'+str(i)])
		mp20.dispense(volume_template, qpcr_plate[lookup[str(i)][0]+str(lookup[str(i)][1])])
		mp20.dispense(volume_template, qpcr_plate[lookup[str(i)][0]+str(lookup[str(i)][1]+1)])
		mp20.dispense(volume_template, qpcr_plate[lookup[str(i)][0]+str(lookup[str(i)][1]+2)])
		mp20.drop_tip() 
