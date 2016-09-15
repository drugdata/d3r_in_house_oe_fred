CELPP Weekly Pose Prediction Challenge
======================================

Celpprunner version: 1.5.0
Week: XX
Year: XXXX

This tar file contains the CELPP weekly pose prediction challenge dataset.

Within this readme.txt is a description of the data in this tar file as well as
a summary of the Blastnfilter run which generated these candidates.

Tsv files downloaded from
=========================

http://www.wwpdb.org/files/new_release_structure_sequence.tsv
http://www.wwpdb.org/files/new_release_structure_nonpolymer.tsv
http://www.wwpdb.org/files/new_release_crystallization_pH.tsv

Structure of data overview
==========================

This tar file contains a set of directories set to the name of Targets. Targets
are proteins which have primary sequence released, but not 3D coordinates.

Within each directory are a set of Candidates.  Candiates are proteins with
similar structure to the Target that also have known 3D coordinates which can
be used for pose prediction.

For more information visit:

https://github.com/drugdata/D3R
              or
https://drugdesigndata.org/about/celpp


Structure of data
=================

Below is a definition of the files and directories within this tar file:

[file or directory <text within denote values that change>]

  -- Definition


 [readme.txt]

     -- Description of data and output from celpp blastnfilter stage of
        processing.

 [new_release_crystallization_pH.tsv]
 [new_release_structure_nonpolymer.tsv]
 [new_release_structure_sequence.tsv]

     -- Tsv files downloaded from: http://www.wwpdb.org/files

 [<target id>]/
               [<target id>.txt]

                  -- Summary of Blastnfilter results for target protein
                     with PDBID.

               [LMCSS-<target id>_<candidate id>-<candidate ligand id>.pdb]

                  -- Candidate protein for docking which:
                      1) Passes the Blastnfilter criteria

                      2) Contains the Ligand with the largest maximum common
                         substructure (MCSS) to the Target Ligand.

                         Note:  If multiple proteins founded, the protein
                                with the highest resolution will be picked.

               [SMCSS-<target id>_<candidate id>-<candidate ligand id>.pdb]

                  -- Candidate protein for docking which:
                      1) Passes the Blastnfilter criteria.

                      2) Contains the Ligand with the smallest maximum common
                         substructure (MCSS) to the Target Ligand.

                         Note:  If multiple proteins founded, the protein
                                with the highest resolution will be picked.

               [hiResHolo-<target id>_<candidate id>-<candidate ligand id>.pdb]

                   -- Candidate protein for docking which:
                      1) Passes the Blastnfilter criteria.

                      2) Has the highest resolution among all holo proteins.

               [hiResApo-<target id>_<candidate id>-<candidate ligand id>.pdb]

                   -- Candidate protein for docking which:
                      1) Passes the Blastnfilter criteria.

                      2) Has the highest resolution among all apo proteins.

               [LMCSS-<target id>_<candidate id>-<candidate ligand id>                                                                       -lig.pdb]

                    -- Contains the 3D coordinate of the atoms for the ligand
                       in the MaxMCSS candidate (LMCSS) protein.

               [lig_<candidate ligand id>.smi]

                   -- Canonical smile string of the Target Ligand which will be
                      used in later docking.

               [lig_<candidate ligand id>.inchi]

                   -- Inchi string of the Target Ligand.

               [lig_<candidate ligand id>.mol]

                   -- 2D structure of the Target Ligand.

Blastnfilter Summary
====================

INPUT SUMMARY
  entries:                             1
  complexes:                           1
  dockable complexes:                  1
  monomers:                            1
  dockable monomers:                   1
  multimers:                           0
  dockable multimers:                  0

FILTERING CRITERIA
  No. of query sequences           <=    1
  No. of dockable ligands           =    1
  Percent identity                 >=    0.95
  Percent Coverage                 >=    0.9
  No. of hit sequences             <=    2
  Structure determination method:        x-ray diffraction

OUTPUT SUMMARY
  Targets found:                        33
  Target: 1fcz|Sequences: 1|Hits: 270|Candidates: 9|Elected:3|PDBids: 1fcy,2lbd,1fcz
