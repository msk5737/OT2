# Normalize 16S rRNA Amplicons for Sanger Sequencing
Before Sanger Sequencing, it is important to normalize each sample in order for it to be sequenced at the proper concentration. GeneWiz requests that <48 samples are sent in strip tubes, and >48 samples are sent in 96 well plates. GeneWiz requests that each sample is 5 μL at a concentration of 10 ng/μL. In order to dilute samples to 10 ng/μL, nuclease free water must be added to samples that have a concentration of over 10 ng/μL. Per sequencing reaction, there should be 5 μL of 10 ng/μL product as well as 10 μL of 2 μM 8F primer.
## Background
Sanger sequencing is also known as the "chain termination method" which determines the nucleotide sequence of DNA. Our goal with Sanger 16S rRNA sequencing is to obtain every possible length of DNA up to the full length of the target DNA. Sanger sequencing is performed in an automated way through three steps: PCR with fluorescent chain-terminating ddNTPs, size separation by capillary gel electrophoresis, and laser excitation and detection by sequencing machine. 
## Materials
- [ ] Cleaned up amplicons 
- [ ] Nuclease free water
- [ ] 2 μM 8F primer (5-AGAGTTTGATCCTGGCTCAG-3)
- [ ] Bio-Rad 96 well plate
- [ ] Opentrons 20 uL single channel pipette (on the left side)
- [ ] Opentrons 20 uL pipette tips
- [ ] Opentrons tube rack
- [ ] Two Eppendorf tubes (one for nuclease free water & one for 8F primer)
## Instructions
- [ ] Obtain your plate(s) of cleaned up amplicons from the freezer and thaw. Briefly centrifuge before opening!
- [ ] Download a copy of NormalizeSanger_jp.py and copy and paste your loadings into it.
- [ ] Set up the OT-2 as in Figure 1. Note: you can manually load the 10 μL of the 8F primer to the new 96 well plate to save time.
- [ ] Load the python script on the OT-2.
- [ ] Calibrate all deck positions.
- [ ] Run script (Estimated run time per 96 well plate = ~55 minutes).
- [ ] After completion, send plates to GeneWiz or store plates at -20°C for short-term storage.


![Screen Shot 2022-01-31 at 5 38 52 PM](https://user-images.githubusercontent.com/94933503/151884827-07808348-a599-420e-9b41-f2e1ec04bbed.png)

**Figure 1. OT-2 set up for normalizing 16S rRNA amplicons. Positions 1,2:** Cleaned up amplicons (old plates). **Positions 4,5:** New Bio-Rad 96 well plates. **Positions 7,8:** OT-2 20 μL filter tip racks. **Position 10:** Opentrons 24 tube rack with two Eppendorf tubes. The tube in position A1 contains nuclease free water, and the tube in position A2 contains 2 μM 8F primer.
