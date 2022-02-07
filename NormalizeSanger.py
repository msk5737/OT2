from opentrons import protocol_api
import csv
import numpy

# metadata
metadata = {
    'protocolName': 'PoolEquimolar',
    'author': 'J Bisanz, jordan.bisanz@gmail.com',
    'description': 'Cherry picking protocol to generate equimolar pools of amplicon libraries. All volumes are transferred to a single 1.5mL Eppendorf tube',
    'apiLevel': '2.7'
}


#fix disposing first tip, and protocol comment instead of print, add tip touch on both sides?

# The data below is taken from a CSV wherein the first column defines the plate number, the second is the well from an indexing plate (biorad 96 well) and the third column is the volume (in µL) to transfer.
# Note: Ensure that total volumes to be transferred do not exceed 1.4mL!!!!! If so, program will pause and ask you to replace the tube when it is full. After run merge all tubes.
# Lines 17-114 are to be replaced with the users data taken from the loadings.csv of the tracking sheet.
loadings = '''
oldplate,oldwell,newplate,newwell,volume_water,volume_dna

'''
loadings_parsed = loadings.splitlines()[1:] # Discard the blank first line.


def run(protocol: protocol_api.ProtocolContext):

    # define labware, only load the plates that are specified in the csv file
    OldPlate1 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '1')
    OldPlate2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2')
   
    NewPlate1 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '4')
    NewPlate2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5')

    epitube = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '7') # eppendorf microcentrifuge tube in rack on position 3
    tips1 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10') # 20ul filter tips on deck position 1
    tips2 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '11') # 20ul filter tips on deck position 1


    # define pipettes
    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips1, tips2])

    #start by primer
    left_pipette.pick_up_tip()
    for transfer in csv.DictReader(loadings_parsed):
            left_pipette.aspirate(10, epitube['A2'])
            left_pipette.dispense(10, eval(transfer['newplate'])[transfer['newwell']])
    left_pipette.drop_tip()

    #start by adding water
    left_pipette.pick_up_tip()
    for transfer in csv.DictReader(loadings_parsed):
        if float(transfer['volume_water']) > 0:
            left_pipette.aspirate(float(transfer['volume_water']), epitube['A1'])
            left_pipette.dispense(float(transfer['volume_water']), eval(transfer['newplate'])[transfer['newwell']])
    left_pipette.drop_tip()
   
    #now add DNA
    for transfer in csv.DictReader(loadings_parsed):
        left_pipette.pick_up_tip()
        left_pipette.aspirate(float(transfer['volume_dna']), eval(transfer['oldplate'])[transfer['oldwell']])
        left_pipette.dispense(float(transfer['volume_dna']), eval(transfer['newplate'])[transfer['newwell']])
        left_pipette.drop_tip()
    
