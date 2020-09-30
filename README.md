# Optimize.Bio
A Consensus Sequence Design Tool for Molecular Cloning Workflows and DNA Vaccine Design

Optimize.Bio is a sequence alignment and codon optimization tool designed to create multiple sequence alignments (MSA) for input amino acid sequences and generate a codon-optimized cDNA sequence for molecular cloning. The purpose of this program is to rapidly generate optimized sequences to synthetically design and produce proteins to clone into expression plasmids. An example use case would be optimization of the SARS-CoV-2 Spike Protein sequence from different strains to generate a human-centered sequence for designing a DNA vaccine. Optimize.Bio is an easy-to-use desktop GUI supporting manual file inputs or file uploads and processing of between 3-10 amino acid sequences at a time. The MSA algorithm is derived from the [MUSCLE algorithm](https://biopython.org/docs/dev/api/Bio.Align.Applications.html) developed by Robert C. Edgar and included in the Biopython module (1). The codon optimization algorithm used here was developed by the Ediburgh Genome Foundry called [DNAChisel](https://github.com/Edinburgh-Genome-Foundry/DnaChisel), consisting of a massive library with different tools from which the DNA optimization and reverse translation tools were obtained (2). The consensus sequence design algorithm was developed by me, and is a relatively simple implementation relying on nucleotide frequencies within a given set of input sequences from the MSA. 

<p align="center">
  <img src="https://i.imgur.com/iXgN8dn.gif" />
</p>

# Usage
Under the main application:
1) Sequence Count: The number of sequences you wish to manually enter for processing. This value MUST be filled in to see the final output regardless of whether you are manually entering your sequences or not.
2) Input Method: The method through which you plan to enter your sequences. Manual will enable n number of sequence cells as specified under sequence count. File upload will allow you to select a FASTA file from your computer to upload. Your code MUST be in the correct FASTA format, otherwise the program will be unable to process your file.
3) Sequence Type: Currently, Optimize.Bio only supports amino acid sequences (protein sequences). Future work will include DNA sequences.
4) Desired Species: Select the species for which you would like codon optimization to be performed on (your final output DNA sequence will be codon optimized for this species.)
5) Sequence Labels: Enter Descriptive Labels for your appropriate sequences. These can be exported to a file (detailed below).
6) Sequence Text: Enter your amino acid sequences WITHOUT any spaces in between or at the ends. 

Under the main menu:
1) Export Current Output: Creates a .txt log file with the input sequences, output sequence, and date/time of file creation for tracking and external use.
2) Clear and Reset: Resets all settings to default (as if the application was just opened)

# Installation
Install the entire repository locally or clone the repository using the Git client. An executable version of Optimize.Bio will be released soon, however to currently run Optimize.Bio, ensure that Python, PyQt5, re, webbrowser, datetime, DNAChisel, and Biopython are downloaded on your computer. This will not be necessary once an update in the form of an .exe is posted. 

Note: Optimize.Bio is currently designed to run on Windows OS. Functionality for MacOS is dependent on the muscle algorithm's executable file for the MacOS which is still being implemented for this application and will be released in the future.

The file hosting the application is called OptimizeBioGUI.py, containing all operations relevant to the GUI. Sequence alignment and optimization procedures are stored in the sequence_operations.py file. The MUSCLE algorithm is stored in the file muscle3.8.31_i86win32.exe and MUST be in the same directory as the GUI and sequence operations files. Finally, style.qss is the stylesheet used to create the dark theme for the application. 
unaligned.fasta, unaligned3.fasta, and unaligned4.fasta are sample file inputs that can be uploaded to Optimize.Bio to test functionality.


# Future Work
1) Currently Optimize.Bio only supports alignment and optimization of amino acid sequences. A future version will include support for alignment and optimization of DNA sequences, as well as support for further optimization tools present in the DNAChisel repository such as secondary structure optimization and removal of hairpin loops through integration with [NUPACK](http://www.nupack.org).
2) The current program is limited in handling alignment of sequences with significantly different lengths, where gaps are inserted by the MUSCLE algorithm. Codon optimization is challenging as the current program cannot predict whether a specific amino acid should be inserted at the site or gaps should be removed from the consensus sequence. A future version will include an option to separate alignment and codon optimization, to retrieve the aligned sequence and manipulate it separately and perform a separate codon optimization on it. In addition, alternative strategies may be employed to handle gap insertion.
3) The current program only generates the optimized sequence for a given protein but does not include a specific implementation for cloning. A future version will include the option to generate a sequence including restriction enzyme sites for cloning into specific plasmids, as well as optimize for mammalian or bacterial plasmid expression. Export formats may also be adapted for uploading sequences to [Benchling](https://www.benchling.com) or [SnapGene](https://www.snapgene.com) for further manipulation and processing.

# Relevant Credit
1) Thanks to the Edinburgh Genome Foundry for developing DNAChisel, an incredibly powerful bioinformatics platform that continues to grow everyday. Take a look at DNAChisel [here](https://github.com/Edinburgh-Genome-Foundry/DnaChisel).
2) Thanks to Colin Duquesnoy for the QDarkStyleSheet used as the theme for this application. The stylesheet can be found [here](https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/qdarkstyle/style.qss).
All other references to websites, packages, modules, etc. are not endorsements and are owned by their respective developers.

# License = MIT
Optimize.Bio is an open-source software developed by me (Gaurav Byagathvalli) and released on GitHub under the MIT license. Feel free to contribute or suggest improvements! 

# References 
1) Edgar R. C. (2004). MUSCLE: multiple sequence alignment with high accuracy and high throughput. Nucleic acids research, 32(5), 1792–1797. https://doi.org/10.1093/nar/gkh340
2) Zulkower, V., & Rosser, S. (2020). DNA Chisel, a versatile sequence optimizer. Bioinformatics (Oxford, England), btaa558. Advance online publication. https://doi.org/10.1093/bioinformatics/btaa558
